"""
TİD Veri Toplama Aracı (TİD Dataset Collector)
TÜBİTAK projesi için yeni Türk İşaret Dili kelimeleri ve jestlerini
kameradan kaydedip eğitim veri seti (.npy) oluşturan araç.
"""

import os
import sys
import time
import argparse
import numpy as np
import cv2

# Üst dizini sys.path'e ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.camera import CameraStream
from core.landmark_detector import HandLandmarkDetector


def collect_sign_data(label_name: str, sample_count: int = 60, output_dir: str = "dataset/data"):
    os.makedirs(output_dir, exist_ok=True)
    label_file = os.path.join(output_dir, f"{label_name}.npy")

    print(f"\n==========================================")
    print(f"  TİD Veri Toplama: '{label_name}'")
    print(f"  Hedef Örnek Sayısı: {sample_count}")
    print(f"==========================================\n")

    detector = HandLandmarkDetector()
    camera = CameraStream()

    if not camera.start():
        print("HATA: Kamera başlatılamadı!")
        return

    print("Kamera hazırlandı. Hazırlanmak için 3 saniyeniz var...")
    start_countdown = time.time()
    while time.time() - start_countdown < 3.0:
        ret, frame = camera.read()
        if ret and frame is not None:
            remaining = 3 - int(time.time() - start_countdown)
            cv2.putText(frame, f"BASLIYOR: {remaining}", (180, 240),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 255), 4)
            cv2.imshow("TID Veri Toplama", frame)
            cv2.waitKey(1)

    print("Kayıt başladı! Lütfen işareti kameraya doğru yapın...")
    samples = []

    while len(samples) < sample_count:
        ret, frame = camera.read()
        if not ret or frame is None:
            time.sleep(0.01)
            continue

        det_result = detector.detect(frame)
        hands = det_result.get("hands", [])

        if hands:
            # İlk tespit edilen elin 21 eklem noktasının bağıl koordinatlarını al
            rel_lms = hands[0]["relative_landmarks"]
            flat_features = []
            for pt in rel_lms:
                flat_features.extend([pt[0], pt[1], pt[2]])
            samples.append(flat_features)

            # Ekrandaki çizgileri çiz
            detector.draw_landmarks(frame, hands)

        # Bilgi paneli
        progress = len(samples)
        color = (0, 255, 0) if hands else (0, 0, 255)
        status_text = f"El Tespit Edildi ({progress}/{sample_count})" if hands else "El Bekleniyor..."

        cv2.putText(frame, f"Kelime: {label_name}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
        cv2.putText(frame, status_text, (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        # İlerleme çubuğu
        bar_width = int((progress / sample_count) * (frame.shape[1] - 40))
        cv2.rectangle(frame, (20, frame.shape[0] - 30),
                      (20 + bar_width, frame.shape[0] - 15), (0, 255, 0), -1)

        cv2.imshow("TID Veri Toplama", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Kullanıcı tarafından iptal edildi.")
            break

    camera.stop()
    cv2.destroyAllWindows()

    if samples:
        new_data = np.array(samples, dtype=np.float32)
        if os.path.exists(label_file):
            existing_data = np.load(label_file)
            combined_data = np.vstack([existing_data, new_data])
            np.save(label_file, combined_data)
            print(f"Mevcut veriye eklendi. Toplam örnek sayısı: {len(combined_data)}")
        else:
            np.save(label_file, new_data)
            print(f"Yeni veri kaydedildi: {label_file} ({len(new_data)} örnek)")
    else:
        print("Hiç örnek kaydedilmedi.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TİD Veri Toplayıcı")
    parser.add_argument("--label", type=str, default="MERHABA", help="Kaydedilecek kelime (örn: MERHABA, TESEKUKRLER)")
    parser.add_argument("--samples", type=int, default=60, help="Kaydedilecek kare sayısı")
    args = parser.parse_args()

    collect_sign_data(args.label, args.samples)
