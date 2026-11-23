"""
TİD-Klavye - Klavye Enjeksiyonu
pynput kullanarak sistem klavyesine karakter gönderir.
X display yoksa (headless/CLI mod) simüle eder.
"""

import sys
import os
import time
import logging

logger = logging.getLogger(__name__)

class KeyboardInjector:
    def __init__(self):
        self.keyboard = None
        self.Key = None
        self._headless = False
        self._init_keyboard()

    def _init_keyboard(self):
        """pynput'u başlat; X yoksa headless moda geç."""
        try:
            from pynput.keyboard import Controller, Key
            self.keyboard = Controller()
            self.Key = Key
            if sys.platform == "win32":
                self._warmup()
            logger.info("Klavye enjektörü hazır.")
        except Exception as e:
            logger.warning(f"pynput başlatılamadı (headless mod): {e}")
            self._headless = True

    def _warmup(self):
        """Windows'ta pynput Controller'ı ön-ısıt."""
        try:
            import threading
            def _warm():
                time.sleep(0.1)
            t = threading.Thread(target=_warm, daemon=True)
            t.start()
        except Exception:
            pass

    def type_text(self, text: str):
        """Metni klavye aracılığıyla yaz."""
        if self._headless or self.keyboard is None:
            # Headless modda sadece logla
            logger.info(f"[HEADLESS] Klavye çıktısı: {repr(text)}")
            print(f"[Klavye] → {text}")
            return
        try:
            if sys.platform == "win32":
                self.keyboard.type(text)
            else:
                for char in text:
                    self.keyboard.type(char)
                    time.sleep(0.01)
        except Exception as e:
            logger.error(f"Yazma hatası: {e}")

    def press_key(self, key_name: str):
        """Özel tuş bas (backspace, enter, space vb.)."""
        if self._headless or self.keyboard is None or self.Key is None:
            logger.info(f"[HEADLESS] Tuş basıldı: {key_name}")
            print(f"[Klavye] → <{key_name}>")
            return
        key_map = {
            "backspace": self.Key.backspace,
            "enter":     self.Key.enter,
            "space":     self.Key.space,
            "tab":       self.Key.tab,
            "escape":    self.Key.esc,
        }
        key = key_map.get(key_name.lower())
        if key:
            try:
                self.keyboard.press(key)
                self.keyboard.release(key)
            except Exception as e:
                logger.error(f"Tuş basma hatası: {e}")
        else:
            logger.warning(f"Bilinmeyen tuş: {key_name}")
