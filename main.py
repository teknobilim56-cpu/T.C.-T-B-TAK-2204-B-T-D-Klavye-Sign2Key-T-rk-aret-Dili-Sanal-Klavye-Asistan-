"""
T.C. TÜBİTAK 2204-B Projesi
TİD-Klavye (Sign2Key) - Ana Uygulama
"""

import os
import sys
import time
import logging
import argparse

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("TIDKlavye")

def parse_args():
    parser = argparse.ArgumentParser(description="TİD-Klavye | TÜBİTAK 2204-B")
    parser.add_argument("--no-gui", action="store_true", help="GUI olmadan CLI modunda çalış")
    parser.add_argument("--camera", type=int, default=0, help="Kamera indeksi (varsayılan: 0)")
    return parser.parse_args()

def run_cli_loop(camera_index=0):
    import cv2
    from core.camera import CameraStream
    from core.landmark_detector import HandLandmarkDetector
    from core.gesture_recognizer import GestureRecognizer
    from core.keyboard_injector import KeyboardInjector

    print("=" * 60)
    print(" T.C. TÜBİTAK 2204-B: TİD-Klavye | CLI Modu")
    print("=" * 60)
    print("Sistem bileşenleri başlatılıyor...")

    detector = HandLandmarkDetector()
    recognizer = GestureRecognizer()
    injector = KeyboardInjector()

    print("Kamera başlatılıyor...")
    camera = CameraStream(src=camera_index)
    cam_ok = camera.start()
    if not cam_ok:
        print("[UYARI] Kamera açılamadı — demo modda çalışılıyor (kamera yok).")

    text_buffer = ""
    last_gesture = None
    gesture_start = 0.0
    last_action_time = 0.0
    HOLD_TIME = 0.4
    COOLDOWN = 1.0

    print("Sistem hazır. Çıkmak için Ctrl+C.")
    print("-" * 60)

    try:
        while True:
            ret, frame = camera.read()
            if not ret or frame is None:
                time.sleep(0.033)
                continue

            landmarks = detector.detect(frame)
            gesture = recognizer.recognize(landmarks) if landmarks else None

            now = time.time()

            if gesture and gesture == last_gesture:
                held = now - gesture_start
                if held >= HOLD_TIME and (now - last_action_time) > COOLDOWN:
                    last_action_time = now
                    print(f"[Jest] {gesture}")
                    if gesture == "<SİL>":
                        if text_buffer:
                            text_buffer = text_buffer[:-1]
                        injector.press_key("backspace")
                    elif gesture == "<BOŞLUK>":
                        text_buffer += " "
                        injector.press_key("space")
                    elif gesture == "<GÖNDER>":
                        injector.press_key("enter")
                        text_buffer = ""
                    elif gesture == "<TEMİZLE>":
                        text_buffer = ""
                    else:
                        text_buffer += gesture
                        injector.type_text(gesture)
                    print(f"[Tampon] {repr(text_buffer)}")
            elif gesture != last_gesture:
                last_gesture = gesture
                gesture_start = now

            try:
                disp = frame.copy()
                label = f"Jest: {gesture or '---'}"
                cv2.putText(disp, label, (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                cv2.putText(disp, f"Tampon: {text_buffer}", (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 1)
                cv2.imshow("TID-Klavye | Ctrl+C=cikis", disp)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except Exception:
                pass

    except KeyboardInterrupt:
        print("\nKapatılıyor...")
    finally:
        try:
            camera.stop()
        except Exception:
            pass
        try:
            cv2.destroyAllWindows()
        except Exception:
            pass

def run_gui():
    from PyQt6.QtWidgets import QApplication
    from ui.main_window import OfficialMainWindow
    app = QApplication(sys.argv)
    app.setApplicationName("TİD-Klavye | TÜBİTAK 2204-B")
    window = OfficialMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    args = parse_args()
    if args.no_gui:
        run_cli_loop(camera_index=args.camera)
    else:
        run_gui()
