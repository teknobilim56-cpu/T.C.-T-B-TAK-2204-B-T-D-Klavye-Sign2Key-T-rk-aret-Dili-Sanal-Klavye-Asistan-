"""
El Eklem Noktasi Tespit Modulu
DUZELTME: hand_landmarker.task eksikse otomatik indirir.
"""
import os, locale
os.environ["LC_ALL"] = "C"; os.environ["LANG"] = "C"
try: locale.setlocale(locale.LC_ALL, "C")
except: pass

from typing import List, Tuple, Dict, Any, Optional
import cv2, numpy as np, mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

_MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/"
              "hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task")

def _ensure_model(model_path):
    if os.path.exists(model_path):
        return model_path
    os.makedirs(os.path.dirname(model_path) if os.path.dirname(model_path) else ".", exist_ok=True)
    print(f"[LandmarkDetector] Model indiriliyor...")
    try:
        import urllib.request
        urllib.request.urlretrieve(_MODEL_URL, model_path)
        print(f"[LandmarkDetector] Model indirildi: {model_path}")
        return model_path
    except Exception as e:
        raise FileNotFoundError(f"Model indirilemedi: {e}") from e

class HandLandmarkDetector:
    WRIST=0; THUMB_CMC=1; THUMB_MCP=2; THUMB_IP=3; THUMB_TIP=4
    INDEX_MCP=5; INDEX_PIP=6; INDEX_DIP=7; INDEX_TIP=8
    MIDDLE_MCP=9; MIDDLE_PIP=10; MIDDLE_DIP=11; MIDDLE_TIP=12
    RING_MCP=13; RING_PIP=14; RING_DIP=15; RING_TIP=16
    PINKY_MCP=17; PINKY_PIP=18; PINKY_DIP=19; PINKY_TIP=20
    CONNECTIONS = [(0,1),(1,2),(2,3),(3,4),(0,5),(5,6),(6,7),(7,8),
                   (5,9),(9,10),(10,11),(11,12),(9,13),(13,14),(14,15),(15,16),
                   (13,17),(17,18),(18,19),(19,20),(0,17)]

    def __init__(self, model_path="models/hand_landmarker.task", max_hands=2):
        model_path = _ensure_model(model_path)
        base_opts = python.BaseOptions(model_asset_path=model_path)
        opts = vision.HandLandmarkerOptions(
            base_options=base_opts, running_mode=vision.RunningMode.IMAGE,
            num_hands=max_hands, min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5, min_tracking_confidence=0.5)
        self.detector = vision.HandLandmarker.create_from_options(opts)

    def detect(self, bgr_frame):
        rgb = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2RGB)
        mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        result = self.detector.detect(mp_img)
        hands_data = []
        if result.hand_landmarks:
            for i, hand_lms in enumerate(result.hand_landmarks):
                handedness = "Right"
                if result.handedness and i < len(result.handedness) and result.handedness[i]:
                    handedness = result.handedness[i][0].category_name
                raw = [(lm.x, lm.y, lm.z) for lm in hand_lms]
                wrist = raw[0]; mid_mcp = raw[self.MIDDLE_MCP]
                scale = np.linalg.norm(np.array(mid_mcp) - np.array(wrist))
                if scale < 1e-4: scale = 1.0
                rel = [((p[0]-wrist[0])/scale,(p[1]-wrist[1])/scale,(p[2]-wrist[2])/scale) for p in raw]
                hands_data.append({"handedness": handedness, "landmarks": raw,
                                   "relative_landmarks": rel,
                                   "finger_states": self._finger_states(raw)})
        return {"hands": hands_data}

    def _finger_states(self, lms):
        idx_open    = lms[self.INDEX_TIP][1]  < lms[self.INDEX_PIP][1]
        mid_open    = lms[self.MIDDLE_TIP][1] < lms[self.MIDDLE_PIP][1]
        ring_open   = lms[self.RING_TIP][1]   < lms[self.RING_PIP][1]
        pinky_open  = lms[self.PINKY_TIP][1]  < lms[self.PINKY_PIP][1]
        tt = np.array(lms[self.THUMB_TIP][:2]); pm = np.array(lms[self.PINKY_MCP][:2])
        ti = np.array(lms[self.THUMB_IP][:2])
        thumb_open = np.linalg.norm(tt-pm) > np.linalg.norm(ti-pm)
        return {"thumb":thumb_open,"index":idx_open,"middle":mid_open,"ring":ring_open,"pinky":pinky_open}

    def draw_landmarks(self, frame, hands_data):
        h, w, _ = frame.shape
        for hand in hands_data:
            pts = [(int(p[0]*w), int(p[1]*h)) for p in hand["landmarks"]]
            for a, b in self.CONNECTIONS:
                cv2.line(frame, pts[a], pts[b], (46,204,113), 2, cv2.LINE_AA)
            tips = {self.THUMB_TIP,self.INDEX_TIP,self.MIDDLE_TIP,self.RING_TIP,self.PINKY_TIP}
            for i, pt in enumerate(pts):
                if i in tips:
                    cv2.circle(frame, pt, 6, (231,76,60), -1, cv2.LINE_AA)
                    cv2.circle(frame, pt, 7, (255,255,255), 1, cv2.LINE_AA)
                else:
                    cv2.circle(frame, pt, 4, (52,152,219), -1, cv2.LINE_AA)
        return frame
