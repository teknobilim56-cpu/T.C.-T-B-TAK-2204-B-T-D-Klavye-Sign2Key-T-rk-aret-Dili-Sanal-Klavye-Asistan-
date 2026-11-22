# 🇹🇷 T.C. TÜBİTAK 2204-B Araştırma Projesi
# 🤟 TİD-Klavye (Sign2Key): Türk İşaret Dili Destekli Sanal Klavye ve Engelsiz İletişim Asistanı

Bu proje, **TÜBİTAK 2204-B Ortaokul Öğrencileri Araştırma Projeleri Yarışması (Yazılım / Erişilebilirlik Alanı)** kapsamında; işitme ve konuşma engelli bireylerin bilgisayar kullanımını ve mesajlaşma süreçlerini kolaylaştırmak amacıyla geliştirilmiş milli bir yapay zeka ve erişilebilirlik projesidir.

Kullanıcı **WhatsApp (Web/Masaüstü)**, Not Defteri, e-posta veya herhangi bir metin alanında sohbet ederken; web kamerası işaret dili hareketlerini eşzamanlı olarak algılar, kelimeye dönüştürür ve aktif metin alanına klavye vuruşları olarak yazar.

---

## 🌟 Öne Çıkan Özellikler

1. **🏛️ TÜBİTAK 2204-B Resmi Yönetim Paneli (Official Dashboard):**
   - Kurumsal TÜBİTAK rozeti, koyu lacivert & kırmızı resmi tasarım.
   - **4 Ana Bölüm:**
     - 🎥 **Canlı Klavye & Kamera:** Eşzamanlı 21 eklem takibi, güven skoru, kararlılık sayacı ve cümle havuzu.
     - 📖 **TİD Görsel Rehberi & Sözlük:** 70'ten fazla kelime ve 29 harfin resimli/vektörel anlatımı, arama motoru ve canlı test özelliği.
     - 📊 **TÜBİTAK 2204-B Proje Raporu:** Amacı, hedef kitlesi, bilimsel yöntemi ve yenilikçi yönünü özetleyen jüri paneli.
     - ⚙️ **Ayarlar & Kalibrasyon:** Kararlılık süresi, bekleme süresi ve donanım ayarları.

2. **📖 Kapsamlı TİD Görsel Rehberi:**
   - 🔤 **TİD Alfabesi (29 Harf):** A'dan Z'ye tüm harflerin parmak pozisyonları.
   - 👋 **Selamlaşma & İletişim:** Merhaba, Günaydın, İyi Akşamlar, Görüşürüz, Hoş Geldiniz...
   - 🤝 **Nezaket & İfadeler:** Teşekkür Ederim, Lütfen, Özür Dilerim, Rica Ederim, Kolay Gelsin...
   - ✅ **Onay & Temel Cevaplar:** Evet, Hayır, Tamam, Var, Yok, Doğru, Yanlış...
   - ❤️ **Duygular & Hâl Hatır:** Seni Seviyorum, İyiyim, Kötüyüm, Mutlu, Üzgün...
   - ❓ **Soru Kelimeleri:** Ne, Nerede, Nasıl, Ne Zaman, Kim, Neden...
   - 🍞 **Günlük Yaşam:** Su, Yemek, Çay, Ekmek, Tuvalet, Ev, Okul, Hastane, Para...
   - 🚨 **Acil Durum & Sağlık:** Yardım, Acil, Doktor, Polis, Ambulans, Dur...
   - ⌨️ **Klavye Kontrolleri:** Geri Sil (Backspace), Gönder (Enter), Boşluk (Space), Temizle...
   - **🎯 "Canlı Dene" Özelliği:** Rehberden istediğiniz kelimeye tıklayarak kamerada pratik yapabilirsiniz!

3. **🪟 Çift Modlu Çalışma (Full Dashboard & Yüzen WhatsApp Asistanı):**
   - **Resmi Panel:** Jüri sunumları, rehber inceleme ve alıştırma için geniş ekran.
   - **Yüzen Asistan (WhatsApp Modu):** Ekranın köşesinde duran, WhatsApp'ın odaklanmasını (focus) bozmayan kompakt kart (`WA_ShowWithoutActivating`). İstenildiği an tek tıkla tam ekran rehbere geri dönülebilir.

4. **🔬 Bilimsel Altyapı:**
   - MediaPipe Hand Landmarker (21 3B Eklem Noktası x 2 El).
   - Bilek merkezli ölçek ve konum normalizasyonu.
   - Debounce (Hold-to-confirm) kararlılık algoritması (hatalı ve mükerrer harf yazımını önleme).

---

## 🚀 Başlatma ve Kullanım

### 1. Uygulamayı Başlatma (Tam Yönetim Paneli & Rehber)
```bash
.venv/bin/python main.py
```

### 2. Doğrudan WhatsApp Yüzen Asistan Modunda Başlatma
```bash
.venv/bin/python main.py --overlay
```

### 3. Harici Kamera Kullanımı
```bash
.venv/bin/python main.py --camera 1
```

---

## 🎓 TÜBİTAK İçin Yeni Kelime Eğitme Stüdyosu

Proje kapsamında yeni kelimeler kaydedip kendi makine öğrenmesi modelinizi eğitmek isterseniz:

1. **Kelime Kaydetme:**
   ```bash
   .venv/bin/python dataset/collector.py --label GUNAYDIN --samples 60
   .venv/bin/python dataset/collector.py --label NASILSIN --samples 60
   ```

2. **Modeli Eğitme:**
   ```bash
   .venv/bin/python dataset/trainer.py
   ```
   Eğitilen model `models/tid_classifier.pkl` olarak kaydedilir ve sistem açıldığında otomatik devreye girer.

---

## 🧪 Birim Testleri
```bash
.venv/bin/python -m unittest tests/test_modules.py
```
