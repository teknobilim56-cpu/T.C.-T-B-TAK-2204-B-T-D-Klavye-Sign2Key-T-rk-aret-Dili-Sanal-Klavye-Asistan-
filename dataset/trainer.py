"""
TİD Model Eğitici (TİD Model Trainer)
Toplanan işaret dili veri setlerini (dataset/data/*.npy) yükler,
RandomForest / MLP sınıflandırıcı ile modeli eğitir ve
models/tid_classifier.pkl olarak kaydeder.
"""

import os
import glob
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


def train_tid_model(data_dir: str = "dataset/data", output_model: str = "models/tid_classifier.pkl"):
    data_files = glob.glob(os.path.join(data_dir, "*.npy"))
    if not data_files:
        print(f"HATA: '{data_dir}' dizininde hiç .npy veri dosyası bulunamadı!")
        print("Lütfen önce 'python dataset/collector.py --label <KELIME>' komutuyla veri toplayın.")
        return

    if len(data_files) < 2:
        print("UYARI: Sınıflandırma modeli eğitmek için en az 2 farklı kelime verisi gereklidir.")
        print(f"Şu anda sadece {len(data_files)} sınıf var: {[os.path.basename(f) for f in data_files]}")
        return

    X_list = []
    y_list = []
    labels = []

    print("Veri setleri yükleniyor...")
    for idx, filepath in enumerate(data_files):
        label_name = os.path.splitext(os.path.basename(filepath))[0]
        labels.append(label_name)

        data = np.load(filepath)
        print(f"  - [{label_name}]: {len(data)} örnek yüklendi.")

        X_list.append(data)
        y_list.append(np.full(len(data), idx))

    X = np.vstack(X_list)
    y = np.concatenate(y_list)

    print(f"\nToplam Veri Sayısı: {len(X)}, Sınıf Sayısı: {len(labels)}")

    # Eğitim ve test bölmesi
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("Random Forest Sınıflandırıcı eğitiliyor...")
    clf = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\n✅ Eğitim Tamamlandı! Test Doğruluğu (Accuracy): %{acc * 100:.2f}")
    print("\nSınıflandırma Raporu:")
    print(classification_report(y_test, y_pred, target_names=labels))

    # Modeli kaydet
    os.makedirs(os.path.dirname(output_model), exist_ok=True)
    with open(output_model, "wb") as f:
        pickle.dump({"model": clf, "labels": labels}, f)

    print(f"💾 Model başarıyla kaydedildi: {output_model}")


if __name__ == "__main__":
    train_tid_model()
