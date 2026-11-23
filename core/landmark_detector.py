"""
El ve Parmak Eklem Noktaları Tespit Modülü (Landmark Detector)
MediaPipe Hand Landmarker kullanarak her bir el için 21 eklem noktasını
3 boyutlu olarak (x, y, z) çıkarır, normalize eder ve çizim araçları sunar.
"""

import os
import locale
# Türkçe locale kaynaklı regex/tolower çakışmasını önlemek için standart C locale
os.environ["LC_ALL"] = "C"
os.environ["LANG"] = "C"
try:
    locale.setlocale(locale.LC_ALL, "C")
except Exception:
    pass

from typing import List, Tuple, Dict, Any, Optional
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class HandLandmarkDetector:
    # 21 El Eklem Noktası İndeksleri
    WRIST = 0
    THUMB_CMC = 1
    THUMB_MCP = 2
    THUMB_IP = 3
    THUMB_TIP = 4
    INDEX_MCP = 5
    INDEX_PIP = 6
    INDEX_DIP = 7
    INDEX_TIP = 8
    MIDDLE_MCP = 9
    MIDDLE_PIP = 10
    MIDDLE_DIP = 11
    MIDDLE_TIP = 12
    RING_MCP = 13
    RING_PIP = 14
    RING_DIP = 15
    RING_TIP = 16
    PINKY_MCP = 17
    PINKY_PIP = 18
    PINKY_DIP = 19
    PINKY_TIP = 20

    # Parmak eklem bağlantıları (çizim için)
    CONNECTIONS = [
        (0, 1), (1, 2), (2, 3), (3, 4),        # Başparmak
        (0, 5), (5, 6), (6, 7), (7, 8),        # İşaret
        (5, 9), (9, 10), (10, 11), (11, 12),   # Orta
        (9, 13), (13, 14), (14, 15), (15, 16), # Yüzük
        (13, 17), (17, 18), (18, 19), (19, 20),# Serçe
        (0, 17)                                 # Avuç içi tabanı
    ]

    def __init__(self, model_path: str = "models/hand_landmarker.task", max_hands: int = 2):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"MediaPipe model dosyası bulunamadı: {model_path}")

        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.IMAGE,
            num_hands=max_hands,
            min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.detector = vision.HandLandmarker.create_from_options(options)

    def detect(self, bgr_frame: np.ndarray) -> Dict[str, Any]:
        """
        Kamera karesini işler ve tespit edilen elleri döndürür.
        :param bgr_frame: OpenCV BGR formatındaki görüntü
        :return: {'hands': [{'handedness': 'Right', 'landmarks': [(x,y,z),...], 'normalized': [...]}]}
        """
        rgb_frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        result = self.detector.detect(mp_image)

        hands_data = []
        if result.hand_landmarks:
            for i, hand_lms in enumerate(result.hand_landmarks):
                handedness = "Right"
                if result.handedness and i < len(result.handedness) and result.handedness[i]:
                    handedness = result.handedness[i][0].category_name

                # Orijinal normalize koordinatlar (0.0 - 1.0)
                raw_landmarks = [(lm.x, lm.y, lm.z) for lm in hand_lms]

                # Konum ve ölçekten bağımsız öznitelik çıkarımı (wrist merkezli normalize)
                wrist = raw_landmarks[0]
                # El boyutu (bilek ile orta parmak kökü mesafesi) referans ölçeği
                mid_mcp = raw_landmarks[self.MIDDLE_MCP]
                scale = np.linalg.norm(np.array(mid_mcp) - np.array(wrist))
                if scale < 1e-4:
                    scale = 1.0

                rel_landmarks = []
                for pt in raw_landmarks:
                    rel_pt = ((pt[0] - wrist[0]) / scale,
                              (pt[1] - wrist[1]) / scale,
                              (pt[2] - wrist[2]) / scale)
                    rel_landmarks.append(rel_pt)

                # Parmak durumları (açık/kapalı)
                finger_states = self._calculate_finger_states(raw_landmarks)

                hands_data.append({
                    "handedness": handedness,
                    "landmarks": raw_landmarks,
                    "relative_landmarks": rel_landmarks,
                    "finger_states": finger_states
                })

        return {"hands": hands_data}

    def _calculate_finger_states(self, landmarks: List[Tuple[float, float, float]]) -> Dict[str, bool]:
        """Her bir parmağın açık (True) veya bükük/kapalı (False) olup olmadığını hesaplar."""
        # Y ekseninde yukarı gitmek koordinatın küçülmesi demektir (ekran koordinatları)
        # İşaret, Orta, Yüzük, Serçe için uç nokta eklemden yukarıda mı?
        index_open = landmarks[self.INDEX_TIP][1] < landmarks[self.INDEX_PIP][1]
        middle_open = landmarks[self.MIDDLE_TIP][1] < landmarks[self.MIDDLE_PIP][1]
        ring_open = landmarks[self.RING_TIP][1] < landmarks[self.RING_PIP][1]
        pinky_open = landmarks[self.PINKY_TIP][1] < landmarks[self.PINKY_PIP][1]

        # Başparmak kontrolü: Başparmak ucu, CMC ekleminden uzakta mı?
        thumb_tip = np.array(landmarks[self.THUMB_TIP][:2])
        pinky_mcp = np.array(landmarks[self.PINKY_MCP][:2])
        thumb_ip = np.array(landmarks[self.THUMB_IP][:2])
        thumb_open = np.linalg.norm(thumb_tip - pinky_mcp) > np.linalg.norm(thumb_ip - pinky_mcp)

        return {
            "thumb": thumb_open,
            "index": index_open,
            "middle": middle_open,
            "ring": ring_open,
            "pinky": pinky_open
        }

    def draw_landmarks(self, frame: np.ndarray, hands_data: List[Dict[str, Any]]) -> np.ndarray:
        """Kare üzerine el iskeletini ve eklem noktalarını estetik olarak çizer."""
        h, w, _ = frame.shape
        for hand in hands_data:
            landmarks = hand["landmarks"]
            pixel_pts = [(int(pt[0] * w), int(pt[1] * h)) for pt in landmarks]

            # Bağlantı çizgileri
            for p1_idx, p2_idx in self.CONNECTIONS:
                p1 = pixel_pts[p1_idx]
                p2 = pixel_pts[p2_idx]
                cv2.line(frame, p1, p2, (46, 204, 113), 2, cv2.LINE_AA)

            # Eklem noktaları
            for idx, pt in enumerate(pixel_pts):
                # Parmak uçlarını belirgin yap
                if idx in (self.THUMB_TIP, self.INDEX_TIP, self.MIDDLE_TIP, self.RING_TIP, self.PINKY_TIP):
                    cv2.circle(frame, pt, 6, (231, 76, 60), -1, cv2.LINE_AA)
                    cv2.circle(frame, pt, 7, (255, 255, 255), 1, cv2.LINE_AA)
                else:
                    cv2.circle(frame, pt, 4, (52, 152, 219), -1, cv2.LINE_AA)

        return frame
