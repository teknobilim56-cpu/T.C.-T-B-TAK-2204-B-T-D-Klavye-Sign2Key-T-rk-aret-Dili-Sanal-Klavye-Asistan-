"""
Kamera Akış Yöneticisi (Camera Stream Manager)
Arka planda thread olarak çalışır, sıfır gecikme (zero buffer lag) ile
en güncel kareleri sunar ve CPU tüketimini optimize eder.
"""

import cv2
import threading
import time
from typing import Optional, Tuple
import numpy as np


class CameraStream:
    def __init__(self, src: int = 0, width: int = 640, height: int = 480, fps: int = 30):
        self.src = src
        self.width = width
        self.height = height
        self.fps = fps

        self.cap: Optional[cv2.VideoCapture] = None
        self.frame: Optional[np.ndarray] = None
        self.is_running = False
        self._lock = threading.Lock()
        self._thread: Optional[threading.Thread] = None

    def start(self) -> bool:
        """Kamera akışını başlatır."""
        if self.is_running:
            return True

        self.cap = cv2.VideoCapture(self.src)
        if not self.cap.isOpened():
            # Alternatif kamera dene
            alt_src = 1 if self.src == 0 else 0
            self.cap = cv2.VideoCapture(alt_src)
            if not self.cap.isOpened():
                return False
            self.src = alt_src

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.cap.set(cv2.CAP_PROP_FPS, self.fps)

        # İlk kareyi oku
        ret, frame = self.cap.read()
        if not ret or frame is None:
            self.cap.release()
            return False

        self.frame = frame
        self.is_running = True

        self._thread = threading.Thread(target=self._capture_loop, daemon=True)
        self._thread.start()
        return True

    def _capture_loop(self):
        """Kamera karelerini aralıksız yakalayan döngü."""
        while self.is_running and self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret and frame is not None:
                # Aynalama (selfie modu) - kullanıcı işaret dili yaparken doğal görmesi için
                frame = cv2.flip(frame, 1)
                with self._lock:
                    self.frame = frame
            else:
                time.sleep(0.01)

    def read(self) -> Tuple[bool, Optional[np.ndarray]]:
        """En güncel kareyi döndürür."""
        with self._lock:
            if self.frame is None:
                return False, None
            return True, self.frame.copy()

    def stop(self):
        """Kamera akışını güvenli şekilde durdurur."""
        self.is_running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)
        if self.cap:
            self.cap.release()
            self.cap = None
        self.frame = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
