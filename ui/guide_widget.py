"""
TİD Görsel Rehberi Widget
"""
from typing import List, Dict, Any, Optional
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QFrame, QComboBox)
from PyQt6.QtCore import Qt, pyqtSignal, QByteArray
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer
from core.tid_dictionary import TID_DICTIONARY, TID_CATEGORIES
from ui.svg_assets import get_hand_svg

def render_svg_to_pixmap(svg_string: str, width: int = 120, height: int = 120) -> QPixmap:
    renderer = QSvgRenderer(QByteArray(svg_string.encode("utf-8")))
    pixmap = QPixmap(width, height)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()
    return pixmap

class TIDSignCard(QFrame):
    try_sign_requested = pyqtSignal(str)
    def __init__(self, item: Dict[str, Any], parent=None):
        super().__init__(parent)
        self.item = item
        self._init_ui()
    def _init_ui(self):
        self.setStyleSheet("""
            TIDSignCard { background-color: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 6px; }
            TIDSignCard:hover { border: 1px solid #38bdf8; }
        """)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(14)
        svg_content = get_hand_svg(self.item.get("hand_shape", "general_sign"), width=110, height=110)
        pixmap = render_svg_to_pixmap(svg_content, 110, 110)
        img_label = QLabel(self)
        img_label.setPixmap(pixmap)
        img_label.setFixedSize(110, 110)
        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        img_label.setStyleSheet("background-color: #0f172a; border-radius: 10px; border: 1px solid #1e293b;")
        layout.addWidget(img_label)
        info_layout = QVBoxLayout()
        info_layout.setSpacing(4)
        top_row = QHBoxLayout()
        word_label = QLabel(self.item["word"], self)
        word_label.setStyleSheet("color: #f8fafc; font-size: 17px; font-weight: bold; border: none;")
        top_row.addWidget(word_label)
        cat_badge = QLabel(self.item["category"], self)
        cat_badge.setStyleSheet("background-color: #0284c7; color: #ffffff; font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 6px; border: none;")
        top_row.addWidget(cat_badge)
        top_row.addStretch()
        info_layout.addLayout(top_row)
        desc_label = QLabel(f"<b>Nasil Yapilir:</b> {self.item['description']}", self)
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("color: #cbd5e1; font-size: 12px; border: none;")
        info_layout.addWidget(desc_label)
        if self.item.get("tips"):
            tip_label = QLabel(f"<i>{self.item['tips']}</i>", self)
            tip_label.setWordWrap(True)
            tip_label.setStyleSheet("color: #38bdf8; font-size: 11px; border: none;")
            info_layout.addWidget(tip_label)
        layout.addLayout(info_layout, stretch=1)
        btn_layout = QVBoxLayout()
        btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        try_btn = QPushButton("Canli Dene", self)
        try_btn.setStyleSheet("QPushButton { background-color: #0ea5e9; color: #ffffff; font-weight: bold; font-size: 12px; padding: 8px 14px; border-radius: 8px; border: none; } QPushButton:hover { background-color: #0284c7; }")
        try_btn.clicked.connect(lambda: self.try_sign_requested.emit(self.item["word"]))
        btn_layout.addWidget(try_btn)
        layout.addLayout(btn_layout)

class TIDGuideWidget(QWidget):
    try_sign_selected = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.all_items = TID_DICTIONARY
        self._init_ui()
    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        filter_card = QFrame(self)
        filter_card.setStyleSheet("QFrame { background-color: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 6px; }")
        filter_layout = QHBoxLayout(filter_card)
        filter_layout.setContentsMargins(12, 10, 12, 10)
        filter_layout.setSpacing(12)
        self.search_input = QLineEdit(filter_card)
        self.search_input.setPlaceholderText("Kelime ara (ornek: Merhaba, Su, A)...")
        self.search_input.setStyleSheet("QLineEdit { background-color: #0f172a; color: #f8fafc; font-size: 13px; padding: 8px 14px; border: 1px solid #475569; border-radius: 8px; } QLineEdit:focus { border: 1px solid #38bdf8; }")
        self.search_input.textChanged.connect(self._filter_items)
        filter_layout.addWidget(self.search_input, stretch=2)
        self.cat_combo = QComboBox(filter_card)
        self.cat_combo.addItems(TID_CATEGORIES)
        self.cat_combo.setStyleSheet("QComboBox { background-color: #0f172a; color: #f8fafc; font-size: 13px; padding: 8px 14px; border: 1px solid #475569; border-radius: 8px; min-width: 220px; } QComboBox::drop-down { border: none; }")
        self.cat_combo.currentIndexChanged.connect(self._filter_items)
        filter_layout.addWidget(self.cat_combo)
        self.count_label = QLabel(filter_card)
        self.count_label.setStyleSheet("color: #94a3b8; font-size: 12px; font-weight: 600;")
        filter_layout.addWidget(self.count_label)
        layout.addWidget(filter_card)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { background-color: transparent; border: none; } QScrollBar:vertical { background-color: #0f172a; width: 10px; border-radius: 5px; border: none; } QScrollBar::handle:vertical { background-color: #334155; min-height: 25px; border-radius: 5px; }")
        self.cards_container = QWidget()
        self.cards_layout = QVBoxLayout(self.cards_container)
        self.cards_layout.setContentsMargins(0, 0, 8, 0)
        self.cards_layout.setSpacing(10)
        self.scroll_area.setWidget(self.cards_container)
        layout.addWidget(self.scroll_area)
        self._populate_cards(self.all_items)
    def _filter_items(self):
        query = self.search_input.text().strip().lower()
        selected_cat = self.cat_combo.currentText()
        filtered = []
        for item in self.all_items:
            if selected_cat != "Tumu" and item["category"] != selected_cat:
                continue
            if query:
                if not (query in item["word"].lower() or
                        query in item["description"].lower() or
                        query in item["category"].lower()):
                    continue
            filtered.append(item)
        self._populate_cards(filtered)
    def _populate_cards(self, items):
        while self.cards_layout.count():
            child = self.cards_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.count_label.setText(f"Toplam {len(items)} kelime")
        if not items:
            empty = QLabel("Arama sonucu bulunamadi.", self.cards_container)
            empty.setAlignment(Qt.AlignmentFlag.AlignCenter)
            empty.setStyleSheet("color: #64748b; font-size: 15px; padding: 40px;")
            self.cards_layout.addWidget(empty)
            return
        for item in items:
            card = TIDSignCard(item, self.cards_container)
            card.try_sign_requested.connect(self._on_try_sign)
            self.cards_layout.addWidget(card)
        self.cards_layout.addStretch()
    def _on_try_sign(self, word: str):
        self.try_sign_selected.emit(word)
