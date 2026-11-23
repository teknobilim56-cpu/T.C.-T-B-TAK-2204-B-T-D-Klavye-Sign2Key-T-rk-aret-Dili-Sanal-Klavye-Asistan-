"""
TİD Jest Tanıma Motoru
DÜZELTME: Çakışan koşullar giderildi - MERHABA en sona taşındı.
"""
import os, time, pickle
from typing import List, Dict, Any, Optional, Tuple
import numpy as np

class GestureRecognizer:
    def __init__(self, model_path="models/tid_classifier.pkl",
                 hold_duration=0.4, cooldown=1.0):
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
                print(f"[GestureRecognizer] Model yüklendi: {len(self.class_labels)} sinif.")
            except Exception as e:
                print(f"[GestureRecognizer] Model yuklenemedi: {e}")
                self.ml_model = None

    def reload_model(self):
        self._load_ml_model()

    def process_hands(self, hands_data):
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
            if now - self.candidate_start_time >= self.hold_duration:
                if (detected_sign != self.last_triggered_sign) or                    (now - self.last_triggered_time >= self.cooldown):
                    should_type = True
                    self.last_triggered_sign = detected_sign
                    self.last_triggered_time = now
        else:
            self.current_candidate = detected_sign
            self.candidate_start_time = now
        return detected_sign, confidence, should_type

    def _rule_based_recognition(self, hands_data):
        hand = hands_data[0]
        f = hand["finger_states"]
        lms = hand["landmarks"]
        thumb  = f["thumb"];  index  = f["index"]
        middle = f["middle"]; ring   = f["ring"];  pinky = f["pinky"]
        p_thumb = np.array(lms[4][:2])
        p_index = np.array(lms[8][:2])
        thumb_index_dist = np.linalg.norm(p_thumb - p_index)

        # GRUP 1: Sadece basparmak - ONCE kontrol et
        if thumb and not index and not middle and not ring and not pinky:
            dy = lms[2][1] - lms[4][1]
            dx = abs(lms[4][0] - lms[2][0])
            if dx > abs(dy) * 1.2:
                return "<BOSLUK>", 0.85
            elif dy > 0.03:
                return "EVET", 0.92
            else:
                return "<SIL>", 0.90

        # GRUP 2: Sadece isaret
        if index and not middle and not ring and not pinky and not thumb:
            return "HAYIR", 0.90

        # GRUP 3: Isaret + Orta
        if index and middle and not ring and not pinky and not thumb:
            return "<GONDER>", 0.92

        # GRUP 4: OK jesti
        if thumb_index_dist < 0.06 and middle and ring and pinky:
            return "TAMAM", 0.95

        # GRUP 5: ILY
        if thumb and index and not middle and not ring and pinky:
            return "SENI SEVIYORUM", 0.95

        # GRUP 6: Tesekkur
        if index and middle and ring and pinky and not thumb:
            spread = np.linalg.norm(p_index - np.array(lms[20][:2]))
            if spread < 0.20:
                return "TESEKKUR EDERIM", 0.88

        # GRUP 7: MERHABA - EN SONA
        if thumb and index and middle and ring and pinky and thumb_index_dist > 0.08:
            return "MERHABA", 0.94

        return None, 0.0

    def _extract_ml_features(self, hand_data):
        rel_lms = hand_data.get("relative_landmarks", [])
        if len(rel_lms) != 21:
            return None
        fv = []
        for x, y, z in rel_lms:
            fv.extend([x, y, z])
        return np.array(fv, dtype=np.float32)
