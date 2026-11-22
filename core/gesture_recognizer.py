"""
Türk İşaret Dili (TİD) Jest & Kelime Tanıma Motoru (Gesture Recognizer)
DÜZELTMELER (v2): TEŞEKKÜR/MERHABA çakışması giderildi, jestler öncelik sırasına alındı
"""

import os
import time
import pickle
from typing import List, Dict, Any, Optional, Tuple
import numpy as np


class GestureRecognizer:
    def __init__(self, model_path: str = "models/tid_classifier.pkl", hold_duration: float = 0.4, cooldown: float = 1.0):
        self.model_path = model_path
        self.hold_duration = hold_duration
        self.cooldown = cooldown
        self.ml_model = None
        self.class_labels = []
        self._load_ml_model()
        self.current_candidate: Optional[str] = None
        self.candidate_start_time: float = 0.0
        self.last_triggered_sign: Optional[str] = None
        self.last_triggered_time: float = 0.0

    def _load_ml_model(self):
        if os.path.exists(self.model_path):
            try:
                with open(self.model_path, "rb") as f:
                    data = pickle.load(f)
                self.ml_model = data.get("model")
                self.class_labels = data.get("labels", [])
                print(f"[GestureRecognizer] Eğitilmiş model yüklendi: {len(self.class_labels)} sınıf.")
            except Exception as e:
                print(f"[GestureRecognizer] Model yüklenirken hata: {e}")
                self.ml_model = None

    def reload_model(self):
        self._load_ml_model()

    def process_hands(self, hands_data: List[Dict[str, Any]]) -> Tuple[Optional[str], float, bool]:
        if not hands_data:
            self.current_candidate = None
            return None, 0.0, False

        detected_sign = None
        confidence = 0.0

        if self.ml_model is not None:
            features = self._extract_ml_features(hands_data[0])
            if features is not None:
                probs = self.ml_model.predict_proba([features])[0]
                best_idx = int(np.argmax(probs))
                confidence = float(probs[best_idx])
                if confidence > 0.65:
                    detected_sign = self.class_labels[best_idx]

        if detected_sign is None:
            rule_sign, rule_conf = self._rule_based_recognition(hands_data)
            if rule_sign:
                detected_sign = rule_sign
                confidence = rule_conf

        if detected_sign is None:
            self.current_candidate = None
            return None, 0.0, False

        now = time.time()
        should_type = False

        if detected_sign == self.current_candidate:
            held_time = now - self.candidate_start_time
            if held_time >= self.hold_duration:
                if (detected_sign != self.last_triggered_sign) or (now - self.last_triggered_time >= self.cooldown):
                    should_type = True
                    self.last_triggered_sign = detected_sign
                    self.last_triggered_time = now
        else:
            self.current_candidate = detected_sign
            self.candidate_start_time = now

        return detected_sign, confidence, should_type

    def _rule_based_recognition(self, hands_data: List[Dict[str, Any]]) -> Tuple[Optional[str], float]:
        hand = hands_data[0]
        f = hand["finger_states"]
        lms = hand["landmarks"]

        thumb  = f["thumb"]
        index  = f["index"]
        middle = f["middle"]
        ring   = f["ring"]
        pinky  = f["pinky"]

        p_thumb  = np.array(lms[4][:2])
        p_index  = np.array(lms[8][:2])
        p_pinky  = np.array(lms[20][:2])

        thumb_index_dist = np.linalg.norm(p_thumb - p_index)

        # --- ÖZEL JESTLER (en önce) ---

        # <GÖNDER>: index + middle açık, diğerleri KAPALI
        if index and middle and not ring and not pinky and not thumb:
            return "<GÖNDER>", 0.92

        # <SİL>: SADECE başparmak açık + AŞAĞI
        if thumb and not index and not middle and not ring and not pinky:
            if lms[4][1] > lms[2][1]:
                return "<SİL>", 0.90

        # <BOŞLUK>: SADECE başparmak açık + YATAY
        if thumb and not index and not middle and not ring and not pinky:
            if abs(lms[4][1] - lms[2][1]) < 0.04:
                return "<BOŞLUK>", 0.85

        # --- KELİME JESTLERİ ---

        # TAMAM: başparmak + işaret halka (yakın), orta+yüzük+serçe açık
        if thumb_index_dist < 0.06 and middle and ring and pinky:
            return "TAMAM", 0.95

        # TEŞEKKÜR EDERİM: 4 parmak bitişik açık, başparmak ile işaret UZAK (halka yok)
        if index and middle and ring and pinky and thumb_index_dist > 0.08:
            finger_spread = np.linalg.norm(p_index - p_pinky)
            if finger_spread < 0.18:
                return "TEŞEKKÜR EDERİM", 0.88

        # MERHABA: tüm 5 parmak açık + parmaklar GENİŞ aralıklı
        if thumb and index and middle and ring and pinky:
            finger_spread = np.linalg.norm(p_index - p_pinky)
            if finger_spread >= 0.18 and thumb_index_dist > 0.08:
                return "MERHABA", 0.94

        # EVET: SADECE başparmak açık + YUKARI
        if thumb and not index and not middle and not ring and not pinky:
            if lms[4][1] < lms[2][1]:
                return "EVET", 0.92

        # HAYIR: SADECE işaret parmağı açık
        if index and not middle and not ring and not pinky and not thumb:
            return "HAYIR", 0.90

        # SENİ SEVİYORUM: başparmak + işaret + serçe açık, orta + yüzük KAPALI
        if thumb and index and not middle and not ring and pinky:
            return "SENİ SEVİYORUM", 0.95

        return None, 0.0

    def _extract_ml_features(self, hand_data: Dict[str, Any]) -> Optional[np.ndarray]:
        rel_lms = hand_data.get("relative_landmarks", [])
        if len(rel_lms) != 21:
            return None
        feature_vector = []
        for x, y, z in rel_lms:
            feature_vector.extend([x, y, z])
        return np.array(feature_vector, dtype=np.float32)
