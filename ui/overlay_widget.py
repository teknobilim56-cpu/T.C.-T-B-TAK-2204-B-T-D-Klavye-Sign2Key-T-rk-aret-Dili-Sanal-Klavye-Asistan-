"""
Yuzen Mini Asistan Karti (Floating Overlay Widget)
"""
from typing import Optional
import cv2, numpy as np
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QCheckBox, QFrame, QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt, pyqtSignal, QPoint
from PyQt6.QtGui import QImage, QPixmap, QColor

class SignOverlayWidget(QWidget):
    open_main_window_requested = pyqtSignal()
    def __init__(self, on_toggle_active=None, on_toggle_autosend=None):
        super().__init__()
        self.on_toggle_active = on_toggle_active
        self.on_toggle_autosend = on_toggle_autosend
        self.is_active = True
        self.auto_send = False
        self.drag_position = QPoint()
        self._init_window_flags()
        self._init_ui()
    def _init_window_flags(self):
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool |
            Qt.WindowType.WindowDoesNotAcceptFocus)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating, True)
        self.setFixedSize(320, 390)
    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        self.card = QFrame(self)
        self.card.setStyleSheet("QFrame { background-color: #0f172a; border-radius: 16px; border: 1px solid #334155; }")
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(24)
        shadow.setColor(QColor(0, 0, 0, 180))
        shadow.setOffset(0, 4)
        self.card.setGraphicsEffect(shadow)
        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(12, 10, 12, 12)
        card_layout.setSpacing(6)
        header_layout = QHBoxLayout()
        title_box = QVBoxLayout()
        title_box.setSpacing(1)
        t_lbl = QLabel("TUBITAK 2204-B", self.card)
        t_lbl.setStyleSheet("color: #ef4444; font-size: 10px; font-weight: 900; border: none;")
        app_lbl = QLabel("TID-Klavye", self.card)
        app_lbl.setStyleSheet("color: #f8fafc; font-size: 13px; font-weight: bold; border: none;")
        title_box.addWidget(t_lbl); title_box.addWidget(app_lbl)
        header_layout.addLayout(title_box); header_layout.addStretch()
        guide_btn = QPushButton("Rehber", self.card)
        guide_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        guide_btn.setStyleSheet("QPushButton { background-color: #1e293b; color: #38bdf8; font-size: 11px; font-weight: bold; padding: 4px 8px; border-radius: 6px; border: 1px solid #38bdf8; } QPushButton:hover { background-color: #0284c7; color: #ffffff; }")
        guide_btn.clicked.connect(self._open_main_window)
        header_layout.addWidget(guide_btn)
        self.status_pill = QLabel("AKTIF", self.card)
        self.status_pill.setStyleSheet("background-color: #10b981; color: #0f172a; font-size: 10px; font-weight: bold; padding: 3px 8px; border-radius: 6px; border: none;")
        header_layout.addWidget(self.status_pill)
        card_layout.addLayout(header_layout)
        self.cam_label = QLabel(self.card)
        self.cam_label.setFixedSize(296, 160)
        self.cam_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cam_label.setStyleSheet("background-color: #020617; border-radius: 10px; color: #64748b; font-size: 11px; border: 1px solid #1e293b;")
        self.cam_label.setText("Kamera Baslatiliyor...")
        card_layout.addWidget(self.cam_label)
        detect_box = QFrame(self.card)
        detect_box.setStyleSheet("background-color: #1e293b; border-radius: 10px; border: 1px solid #334155; padding: 4px;")
        detect_layout = QVBoxLayout(detect_box)
        detect_layout.setContentsMargins(8, 4, 8, 4); detect_layout.setSpacing(2)
        self.word_label = QLabel("Bekleniyor...", detect_box)
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_label.setStyleSheet("color: #38bdf8; font-size: 17px; font-weight: bold; border: none;")
        self.conf_label = QLabel("Guven: %0", detect_box)
        self.conf_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.conf_label.setStyleSheet("color: #94a3b8; font-size: 10px; border: none;")
        detect_layout.addWidget(self.word_label); detect_layout.addWidget(self.conf_label)
        card_layout.addWidget(detect_box)
        ctrl_layout = QHBoxLayout()
        self.toggle_btn = QPushButton("Durdur", self.card)
        self.toggle_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.toggle_btn.setStyleSheet("QPushButton { background-color: #ef4444; color: #ffffff; font-weight: bold; font-size: 11px; padding: 6px 12px; border-radius: 8px; border: none; } QPushButton:hover { background-color: #dc2626; }")
        self.toggle_btn.clicked.connect(self._toggle_active)
        self.autosend_cb = QCheckBox("Otomatik Enter", self.card)
        self.autosend_cb.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.autosend_cb.setStyleSheet("QCheckBox { color: #cbd5e1; font-size: 11px; border: none; }")
        self.autosend_cb.toggled.connect(self._toggle_autosend)
        ctrl_layout.addWidget(self.toggle_btn); ctrl_layout.addStretch(); ctrl_layout.addWidget(self.autosend_cb)
        card_layout.addLayout(ctrl_layout)
        main_layout.addWidget(self.card)
    def _open_main_window(self):
        self.open_main_window_requested.emit()
    def _toggle_active(self):
        self.is_active = not self.is_active
        if self.is_active:
            self.toggle_btn.setText("Durdur")
            self.toggle_btn.setStyleSheet("background-color: #ef4444; color: #ffffff; font-weight: bold; font-size: 11px; padding: 6px 12px; border-radius: 8px; border: none;")
            self.status_pill.setText("AKTIF")
            self.status_pill.setStyleSheet("background-color: #10b981; color: #0f172a; font-size: 10px; font-weight: bold; padding: 3px 8px; border-radius: 6px; border: none;")
        else:
            self.toggle_btn.setText("Basla")
            self.toggle_btn.setStyleSheet("background-color: #10b981; color: #0f172a; font-weight: bold; font-size: 11px; padding: 6px 12px; border-radius: 8px; border: none;")
            self.status_pill.setText("DURDURULDU")
            self.status_pill.setStyleSheet("background-color: #64748b; color: #ffffff; font-size: 10px; font-weight: bold; padding: 3px 8px; border-radius: 6px; border: none;")
        if self.on_toggle_active:
            self.on_toggle_active(self.is_active)
    def _toggle_autosend(self, checked: bool):
        self.auto_send = checked
        if self.on_toggle_autosend:
            self.on_toggle_autosend(checked)
    def update_frame(self, bgr_frame):
        if bgr_frame is None or not self.isVisible(): return
        scaled = cv2.resize(bgr_frame, (296, 160), interpolation=cv2.INTER_AREA)
        rgb = cv2.cvtColor(scaled, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        q_img = QImage(rgb.data, w, h, ch*w, QImage.Format.Format_RGB888)
        self.cam_label.setPixmap(QPixmap.fromImage(q_img))
    def update_detection(self, word, confidence, status_msg=""):
        if not self.isVisible(): return
        if word:
            self.word_label.setText(word)
            self.conf_label.setText(f"Guven: %{int(confidence*100)} {status_msg}")
            self.word_label.setStyleSheet("color: #10b981; font-size: 17px; font-weight: bold; border: none;")
        else:
            self.word_label.setText("El Bekleniyor...")
            self.conf_label.setText("Isaret yapin")
            self.word_label.setStyleSheet("color: #64748b; font-size: 14px; font-weight: normal; border: none;")
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()
