"""
T.C. TÜBİTAK 2204-B Projesi - SVG Assets
"""

def get_tubitak_badge_svg(width: int = 240, height: int = 50) -> str:
    return f"""<svg width="{width}" height="{height}" viewBox="0 0 240 50" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="tubitakGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b91c1c" />
      <stop offset="100%" stop-color="#991b1b" />
    </linearGradient>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f87171" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.3" />
    </linearGradient>
  </defs>
  <rect x="2" y="2" width="236" height="46" rx="10" fill="url(#tubitakGrad)" stroke="url(#borderGrad)" stroke-width="1.5" />
  <circle cx="26" cy="25" r="15" fill="#ffffff" />
  <circle cx="26" cy="25" r="11" fill="#b91c1c" />
  <circle cx="28" cy="25" r="9" fill="#ffffff" />
  <circle cx="29" cy="25" r="8" fill="#b91c1c" />
  <polygon points="23,23 24.5,21.5 25,23.5 23.5,24.5" fill="#ffffff" />
  <text x="50" y="21" font-family="Segoe UI,sans-serif" font-size="12" font-weight="900" fill="#ffffff" letter-spacing="1">TÜBİTAK 2204-B</text>
  <text x="50" y="36" font-family="Segoe UI,sans-serif" font-size="9" font-weight="600" fill="#fecaca" letter-spacing="0.5">ARAŞTIRMA PROJESİ</text>
</svg>"""


def get_hand_svg(hand_shape: str, width: int = 140, height: int = 140,
                 primary_color: str = "#38bdf8", accent_color: str = "#f43f5e") -> str:
    h = f'<svg width="{width}" height="{height}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
    f = '</svg>'
    if hand_shape in ("open_palm_wave","open_palm","flat_open_four","bye_wave"):
        c = f'''
  <g stroke="{primary_color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <path d="M35 50 Q35 78 50 78 Q65 78 65 50 Z" fill="{primary_color}" fill-opacity="0.2"/>
    <path d="M35 55 Q20 48 24 38 Q28 35 36 45"/>
    <path d="M38 45 L38 20 Q41 17 44 20 L44 45"/>
    <path d="M46 45 L46 15 Q49 12 52 15 L52 45"/>
    <path d="M54 45 L54 18 Q57 15 60 18 L60 45"/>
    <path d="M62 48 L62 26 Q65 23 68 26 L68 50"/>
    <line x1="42" y1="78" x2="42" y2="92"/><line x1="58" y1="78" x2="58" y2="92"/>
  </g>
  <path d="M16 28 Q20 22 16 16" stroke="{accent_color}" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M84 28 Q80 22 84 16" stroke="{accent_color}" stroke-width="2" fill="none" stroke-linecap="round"/>'''
    elif hand_shape in ("thumbs_up","fist_thumb_side","fist_thumb_front"):
        c = f'''
  <g stroke="{primary_color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <rect x="35" y="45" width="34" height="32" rx="8" fill="{primary_color}" fill-opacity="0.2"/>
    <path d="M35 55 L35 25 Q39 16 45 20 Q48 24 45 45" fill="{accent_color}" fill-opacity="0.25" stroke="{accent_color}" stroke-width="3.5"/>
    <line x1="45" y1="52" x2="65" y2="52"/><line x1="45" y1="60" x2="65" y2="60"/>
    <line x1="45" y1="68" x2="65" y2="68"/>
    <line x1="42" y1="77" x2="42" y2="92"/><line x1="62" y1="77" x2="62" y2="92"/>
  </g>
  <path d="M22 36 L22 20 M18 24 L22 20 L26 24" stroke="{accent_color}" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''
    elif hand_shape in ("thumbs_down","thumbs_down_frown"):
        c = f'''
  <g stroke="{primary_color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <rect x="35" y="24" width="34" height="32" rx="8" fill="{primary_color}" fill-opacity="0.2"/>
    <path d="M35 45 L35 75 Q39 84 45 80 Q48 76 45 55" fill="{accent_color}" fill-opacity="0.25" stroke="{accent_color}" stroke-width="3.5"/>
    <line x1="45" y1="32" x2="65" y2="32"/><line x1="45" y1="40" x2="65" y2="40"/>
    <line x1="45" y1="48" x2="65" y2="48"/>
    <line x1="42" y1="24" x2="42" y2="12"/><line x1="62" y1="24" x2="62" y2="12"/>
  </g>
  <path d="M22 64 L22 80 M18 76 L22 80 L26 76" stroke="{accent_color}" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''
    elif hand_shape in ("ok_sign","d_shape","o_shape"):
        c = f'''
  <g stroke="{primary_color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <path d="M40 55 Q40 76 56 76 Q70 76 68 55 Z" fill="{primary_color}" fill-opacity="0.2"/>
    <circle cx="34" cy="46" r="12" fill="{accent_color}" fill-opacity="0.2" stroke="{accent_color}" stroke-width="3"/>
    <path d="M48 45 L48 18 Q51 14 54 18 L54 48"/>
    <path d="M56 46 L56 22 Q59 18 62 22 L62 50"/>
    <path d="M64 48 L64 28 Q67 25 70 28 L70 55"/>
    <line x1="46" y1="76" x2="46" y2="92"/><line x1="62" y1="76" x2="62" y2="92"/>
  </g>
  <circle cx="34" cy="46" r="4" fill="{accent_color}"/>'''
    elif hand_shape in ("v_shape","victory_peace","two_fingers_horizontal"):
        c = f'''
  <g stroke="{primary_color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <path d="M35 50 Q35 76 52 76 Q65 76 65 50 Z" fill="{primary_color}" fill-opacity="0.2"/>
    <path d="M42 48 L32 18 Q35 14 39 16 L48 46" stroke="{accent_color}" stroke-width="3.5" fill="{accent_color}" fill-opacity="0.2"/>
    <path d="M50 46 L60 16 Q64 14 67 18 L57 48" stroke="{accent_color}" stroke-width="3.5" fill="{accent_color}" fill-opacity="0.2"/>
    <line x1="44" y1="76" x2="44" y2="92"/><line x1="58" y1="76" x2="58" y2="92"/>
  </g>'''
    elif hand_shape in ("index_wag","index_straight","point_search","chin_tap"):
        c = f'''
  <g stroke="{primary_color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <rect x="36" y="44" width="30" height="32" rx="8" fill="{primary_color}" fill-opacity="0.2"/>
    <path d="M42 44 L42 16 Q46 12 50 16 L50 44" stroke="{accent_color}" stroke-width="3.5" fill="{accent_color}" fill-opacity="0.25"/>
    <line x1="52" y1="62" x2="64" y2="62"/><line x1="52" y1="69" x2="64" y2="69"/>
    <line x1="42" y1="76" x2="42" y2="92"/><line x1="58" y1="76" x2="58" y2="92"/>
  </g>
  <path d="M30 22 L24 22 M26 19 L23 22 L26 25" stroke="{accent_color}" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M62 22 L68 22 M66 19 L69 22 L66 25" stroke="{accent_color}" stroke-width="2" fill="none" stroke-linecap="round"/>'''
    elif hand_shape == "ily_sign":
        c = f'''
  <g stroke="{primary_color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <path d="M36 48 Q36 74 52 74 Q64 74 64 48 Z" fill="{primary_color}" fill-opacity="0.2"/>
    <path d="M36 55 Q20 50 22 40 Q26 36 36 48" stroke="{accent_color}" stroke-width="3.5"/>
    <path d="M40 46 L40 16 Q44 12 48 16 L48 46" stroke="{accent_color}" stroke-width="3.5" fill="{accent_color}" fill-opacity="0.2"/>
    <path d="M58 46 L64 24 Q67 20 70 24 L68 50" stroke="{accent_color}" stroke-width="3.5" fill="{accent_color}" fill-opacity="0.2"/>
    <line x1="44" y1="74" x2="44" y2="92"/><line x1="58" y1="74" x2="58" y2="92"/>
  </g>
  <path d="M48 64 C48 60 42 56 38 60 C34 64 38 70 48 78 C58 70 62 64 58 60 C54 56 48 60 48 64 Z" fill="{accent_color}" opacity="0.8"/>'''
    else:
        c = f'''
  <g stroke="{primary_color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <path d="M35 48 Q35 74 50 74 Q65 74 65 48 Z" fill="{primary_color}" fill-opacity="0.2"/>
    <path d="M35 52 Q24 46 28 38 Q32 35 37 44"/>
    <path d="M39 44 L39 20 Q42 16 46 20 L46 44"/>
    <path d="M48 44 L48 16 Q51 12 55 16 L55 44"/>
    <path d="M57 44 L57 20 Q60 16 63 20 L63 46"/>
    <path d="M64 47 L64 28 Q67 24 70 28 L70 50"/>
    <line x1="42" y1="74" x2="42" y2="90"/><line x1="58" y1="74" x2="58" y2="90"/>
  </g>
  <circle cx="50" cy="56" r="6" fill="{accent_color}" opacity="0.8"/>'''
    return h + c + f
