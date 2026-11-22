"""
Klavye Enjeksiyon Modülü (Keyboard Injector)
Linux ve Windows ortamlarında sanal tuş vuruşları üreterek
WhatsApp, Not Defteri veya aktif olan herhangi bir metin alanına metin yazar.
"""

import time
import threading
from typing import Optional
from pynput.keyboard import Controller, Key


class KeyboardInjector:
    def __init__(self, char_delay: float = 0.03, word_delay: float = 0.2):
        """
        :param char_delay: Harfler arasındaki yazım gecikmesi (saniye)
        :param word_delay: Kelimeler arasındaki minimum bekleme süresi (spam engelleme)
        """
        self.keyboard = Controller()
        self.char_delay = char_delay
        self.word_delay = word_delay
        self.last_typed_time = 0.0
        self.last_text: Optional[str] = None
        self._lock = threading.Lock()
        self.enabled = True

    def set_enabled(self, enabled: bool):
        """Klavye yazma özelliğini aktif veya pasif yapar."""
        self.enabled = enabled

    def type_text(self, text: str, append_space: bool = True, auto_send: bool = False) -> bool:
        """
        Verilen metni o anda imlecin bulunduğu aktif alana yazar.
        :param text: Yazılacak kelime veya harf
        :param append_space: Kelime sonuna otomatik boşluk eklensin mi?
        :param auto_send: Metin yazıldıktan sonra 'Enter' basılıp gönderilsin mi? (örn. WhatsApp mesajı)
        :return: Başarılı yazıldıysa True, bekleme süresine takıldıysa False
        """
        if not self.enabled or not text:
            return False

        current_time = time.time()
        with self._lock:
            # Aynı kelimenin istenmeden art arda yazılmasını önle
            if current_time - self.last_typed_time < self.word_delay:
                return False

            self.last_typed_time = current_time
            self.last_text = text

            to_type = text + (" " if append_space else "")

            # Karakter karakter doğal yazım simülasyonu
            for char in to_type:
                self.keyboard.type(char)
                if self.char_delay > 0:
                    time.sleep(self.char_delay)

            if auto_send:
                time.sleep(0.05)
                self.keyboard.press(Key.enter)
                self.keyboard.release(Key.enter)

            return True

    def backspace(self):
        """Son yazılan karakteri siler."""
        if not self.enabled:
            return
        self.keyboard.press(Key.backspace)
        self.keyboard.release(Key.backspace)

    def press_enter(self):
        """Enter tuşuna basarak mesajı gönderir veya yeni satıra geçer."""
        if not self.enabled:
            return
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def press_space(self):
        """Boşluk tuşuna basar."""
        if not self.enabled:
            return
        self.keyboard.press(Key.space)
        self.keyboard.release(Key.space)


# Modül testi
if __name__ == "__main__":
    injector = KeyboardInjector()
    print("Klavye test ediliyor: 3 saniye sonra odaklanılan yere 'TİD Test' yazılacak...")
    time.sleep(3)
    injector.type_text("TİD Test Başarılı!", append_space=True)
