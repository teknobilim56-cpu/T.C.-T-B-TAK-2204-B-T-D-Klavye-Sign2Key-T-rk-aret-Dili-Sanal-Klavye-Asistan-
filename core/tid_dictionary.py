"""
T.C. TÜBİTAK 2204-B Projesi
Türk İşaret Dili (TİD) Kapsamlı Sözlük ve Rehber Veritabanı
100'den fazla TİD kelimesi, el alfabesi ve sistem kontrol jestleri.
"""

from typing import List, Dict, Any, Optional

TID_CATEGORIES = [
    "Tümü",
    "🔤 TİD Alfabesi (29 Harf)",
    "👋 Selamlaşma & İletişim",
    "🤝 Nezaket & İfadeler",
    "✅ Onay & Temel Cevaplar",
    "❤️ Duygular & Hâl Hatır",
    "❓ Soru Kelimeleri",
    "🍞 Günlük Yaşam & İhtiyaçlar",
    "🚨 Acil Durum & Sağlık",
    "⌨️ Klavye & Sistem Komutları"
]

TID_DICTIONARY: List[Dict[str, Any]] = [
    # -------------------------------------------------------------
    # 🔤 TİD EL ALFABESİ (29 HARF)
    # -------------------------------------------------------------
    {
        "word": "A Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "fist_thumb_side",
        "description": "Yumruk yapılır, başparmak işaret parmağının yanına dik veya hafif yana açık şekilde yerleştirilir.",
        "tips": "Avuç içi karşıya veya hafif yana bakar. TİD alfabesinin başlangıç harfidir.",
        "keyboard_char": "A"
    },
    {
        "word": "B Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "flat_open_four",
        "description": "Dört parmak bitişik ve yukarı doğru dik durur, başparmak avuç içine doğru hafifçe kıvrılır.",
        "tips": "Avuç içi doğrudan karşıya bakar. Parmakların bitişik olması önemlidir.",
        "keyboard_char": "B"
    },
    {
        "word": "C Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "c_shape",
        "description": "Elin tüm parmakları 'C' harfi oluşturacak şekilde kavisli ve açık tutulur.",
        "tips": "Profil görünümünde net bir hilal veya 'C' şekli oluşturulmalıdır.",
        "keyboard_char": "C"
    },
    {
        "word": "Ç Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "c_shape_shake",
        "description": "'C' harfi pozisyonundaki el bilekten aşağı doğru hafifçe bir veya iki kez sallanır/çentik atılır.",
        "tips": "Çentiği simgelemek için el hafifçe aşağı oynatılır.",
        "keyboard_char": "Ç"
    },
    {
        "word": "D Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "d_shape",
        "description": "İşaret parmağı dimdik yukarı bakar; başparmak, orta, yüzük ve serçe parmak uçlarıyla birleşerek daire oluşturur.",
        "tips": "'D' harfinin dikey çizgisi işaret parmağı, yuvarlağı ise diğer parmaklardır.",
        "keyboard_char": "D"
    },
    {
        "word": "E Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "e_shape",
        "description": "Tüm parmaklar ikinci eklemlerinden bükülür, parmak uçları başparmağın üstüne doğru toplanır.",
        "tips": "Kavisli parmaklar avuç içine doğru hafif kapalıdır.",
        "keyboard_char": "E"
    },
    {
        "word": "F Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "ok_sign",
        "description": "İşaret parmağı ve başparmak uçları birleştirilerek halka yapılır; orta, yüzük ve serçe parmaklar dik ve açık kalır.",
        "tips": "Standart 'OK' jestine benzer, yukarı doğru 3 açık parmak görünür.",
        "keyboard_char": "F"
    },
    {
        "word": "G Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "pinch_horizontal",
        "description": "İşaret ve başparmak birbirine paralel olarak yatay uzatılır (aralarında 2-3 cm mesafe), diğer parmaklar kapalıdır.",
        "tips": "İşaret parmağı yana/karşıya doğru yatay bir çizgi çizer.",
        "keyboard_char": "G"
    },
    {
        "word": "Ğ Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "pinch_horizontal_wave",
        "description": "'G' harfi pozisyonundaki el hafifçe sağa sola veya yukarı doğru dalgalandırılır.",
        "tips": "Ğ üzerindeki yumuşatma şapkasını simgeler.",
        "keyboard_char": "Ğ"
    },
    {
        "word": "H Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "two_fingers_horizontal",
        "description": "İşaret ve orta parmak bitişik olarak yana doğru yatay uzatılır; başparmak, yüzük ve serçe kapalıdır.",
        "tips": "İki parmak yatay doğrultuda tutulur.",
        "keyboard_char": "H"
    },
    {
        "word": "I Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "pinky_only",
        "description": "Sadece serçe parmak dimdik yukarı bakar; başparmak diğer kapalı parmakların üzerindedir.",
        "tips": "İnce dikey çizgiyi serçe parmak temsil eder.",
        "keyboard_char": "I"
    },
    {
        "word": "İ Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "pinky_dot",
        "description": "Serçe parmak yukarıdayken (I harfi), diğer elin işaret parmağıyla serçe parmağın ucuna nokta koyar gibi dokunulur.",
        "tips": "Noktalı İ'nin noktasını diğer el belirler.",
        "keyboard_char": "İ"
    },
    {
        "word": "J Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "pinky_draw_j",
        "description": "Serçe parmak açıkken havada 'J' harfinin kancası çizilir.",
        "tips": "Bilek hareketiyle havada zarif bir kavis oluşturulur.",
        "keyboard_char": "J"
    },
    {
        "word": "K Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "v_thumb_between",
        "description": "İşaret ve orta parmak 'V' şeklinde açık; başparmak aralarına dik olarak yerleştirilir.",
        "tips": "'K' harfinin iki eğik kolunu işaret ve orta parmak oluşturur.",
        "keyboard_char": "K"
    },
    {
        "word": "L Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "l_shape",
        "description": "Başparmak yana, işaret parmağı yukarı açılarak tam 90 derecelik dik bir 'L' açısı oluşturulur.",
        "tips": "Diğer üç parmak avuç içine kapatılır. Çok belirgin ve kolay bir işarettir.",
        "keyboard_char": "L"
    },
    {
        "word": "M Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "three_fingers_down",
        "description": "İşaret, orta ve yüzük parmakları aşağı doğru sarkar; başparmak serçe parmağın altında saklanır.",
        "tips": "'M' harfinin üç bacağını simgeler.",
        "keyboard_char": "M"
    },
    {
        "word": "N Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "two_fingers_down",
        "description": "İşaret ve orta parmak aşağı doğru sarkar; başparmak yüzük parmağının altında saklanır.",
        "tips": "'N' harfinin iki bacağını simgeler.",
        "keyboard_char": "N"
    },
    {
        "word": "O Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "o_shape",
        "description": "Tüm parmak uçları başparmak ucuyla birleşerek tam bir yuvarlak 'O' şekli oluşturur.",
        "tips": "Elin içi boş bir çember gibi görünür.",
        "keyboard_char": "O"
    },
    {
        "word": "Ö Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "o_shape_dots",
        "description": "'O' harfi yapıldıktan sonra diğer elin iki parmağıyla halkanın üzerine iki nokta hareketi yapılır.",
        "tips": "Noktalı sesli harfler için üstten iki vuruş uygulanır.",
        "keyboard_char": "Ö"
    },
    {
        "word": "P Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "k_down",
        "description": "'K' harfi pozisyonundaki el bilekten aşağı doğru 90 derece eğilir.",
        "tips": "İşaret parmağı yatay, orta parmak aşağı sarkar.",
        "keyboard_char": "P"
    },
    {
        "word": "R Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "crossed_fingers",
        "description": "İşaret ve orta parmak birbirinin üzerine çaprazlanır (şans işareti gibi).",
        "tips": "Diğer parmaklar kapalıdır.",
        "keyboard_char": "R"
    },
    {
        "word": "S Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "fist_thumb_front",
        "description": "Sıkı bir yumruk yapılır; başparmak diğer bükülü parmakların önünü sıkıca sarar.",
        "tips": "Avuç içi karşıya bakar.",
        "keyboard_char": "S"
    },
    {
        "word": "Ş Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "fist_thumb_front_shake",
        "description": "'S' harfi yumruğu aşağı doğru hafifçe sallanır veya işaret parmağıyla alt çentik yapılır.",
        "tips": "Çentik hareketi S harfini Ş yapar.",
        "keyboard_char": "Ş"
    },
    {
        "word": "T Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "t_shape",
        "description": "Başparmak, işaret ve orta parmağın arasından dışarı çıkartılarak yumruk sıkılır.",
        "tips": "Başparmak ucu işaret parmağının hemen üstünden görünür.",
        "keyboard_char": "T"
    },
    {
        "word": "U Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "u_shape",
        "description": "İşaret ve orta parmak dimdik ve bitişik olarak yukarı uzatılır; diğer parmaklar kapalıdır.",
        "tips": "'U' harfinin düz paralel kollarını temsil eder.",
        "keyboard_char": "U"
    },
    {
        "word": "Ü Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "u_shape_dots",
        "description": "'U' harfi pozisyonundayken diğer elin iki parmağıyla üst tarafa iki nokta dokunulur.",
        "tips": "Noktalar havada veya parmak uçlarının üstünde gösterilir.",
        "keyboard_char": "Ü"
    },
    {
        "word": "V Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "v_shape",
        "description": "İşaret ve orta parmak açıkça iki yana ayrılarak 'V' zafer işareti oluşturulur.",
        "tips": "Parmaklar arasında belirgin bir açı olmalıdır.",
        "keyboard_char": "V"
    },
    {
        "word": "Y Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "y_shape",
        "description": "Sadece başparmak ve serçe parmak iki yana açık uzatılır; ortadaki 3 parmak avuç içine kapatılır (telefon ahizesi gibi).",
        "tips": "'Y' harfinin iki çatallı kolunu simgeler.",
        "keyboard_char": "Y"
    },
    {
        "word": "Z Harfi",
        "category": "🔤 TİD Alfabesi (29 Harf)",
        "hand_shape": "z_draw",
        "description": "İşaret parmağıyla havada zikzak çizilerek 'Z' harfi resmedilir.",
        "tips": "Soldan sağa, çapraz aşağı ve tekrar sağa doğru hızlı bir çizimdir.",
        "keyboard_char": "Z"
    },

    # -------------------------------------------------------------
    # 👋 SELAMLAŞMA & İLETİŞİM
    # -------------------------------------------------------------
    {
        "word": "MERHABA",
        "category": "👋 Selamlaşma & İletişim",
        "hand_shape": "open_palm_wave",
        "description": "Sağ el açık, parmaklar aralıklı şekilde şakak veya göğüs hizasında tutularak hafifçe sağa-sola sallanır veya öne açılır.",
        "tips": "Güler yüzlü bir mimikle karşı tarafa selam verilir. TİD'in en temel selamlama jestidir.",
        "keyboard_char": "MERHABA"
    },
    {
        "word": "GÜNAYDIN",
        "category": "👋 Selamlaşma & İletişim",
        "hand_shape": "sun_rise",
        "description": "Sağ el göğüs hizasından yukarıya doğru açılarak yükselir (doğan güneş metaforu), ardından açık elle selamlama yapılır.",
        "tips": "Göz teması ve tebessüm eşlik eder.",
        "keyboard_char": "GÜNAYDIN"
    },
    {
        "word": "İYİ AKŞAMLAR",
        "category": "👋 Selamlaşma & İletişim",
        "hand_shape": "sun_set",
        "description": "Önce başparmak yukarıda 'İYİ' işareti yapılır, ardından açık el göğüs önünden aşağı doğru kavisle kapanarak indirilir.",
        "tips": "Akşam vaktinin inişini simgeler.",
        "keyboard_char": "İYİ AKŞAMLAR"
    },
    {
        "word": "İYİ GECELER",
        "category": "👋 Selamlaşma & İletişim",
        "hand_shape": "night_sleep",
        "description": "'İYİ' jestinden sonra sağ el baş hizasına getirilip gözler hafif kısılarak uyku metaforu verilir.",
        "tips": "Yatma/gece vaktini anlatır.",
        "keyboard_char": "İYİ GECELER"
    },
    {
        "word": "GÖRÜŞÜRÜZ",
        "category": "👋 Selamlaşma & İletişim",
        "hand_shape": "two_fingers_eyes_forward",
        "description": "İşaret ve orta parmak ('V') göz hizasına getirilir, ardından karşı tarafa doğru yönlendirilir (göz göze gelmek).",
        "tips": "'Tekrar görüşmek üzere' anlamındadır.",
        "keyboard_char": "GÖRÜŞÜRÜZ"
    },
    {
        "word": "HOŞ GELDİNİZ",
        "category": "👋 Selamlaşma & İletişim",
        "hand_shape": "welcome_sweep",
        "description": "İki el açık avuç içleri yukarı bakacak şekilde dışarıdan içeriye/göğse doğru davet edercesine çekilir.",
        "tips": "Sıcak bir karşılama jestidir.",
        "keyboard_char": "HOŞ GELDİNİZ"
    },
    {
        "word": "GÜLE GÜLE",
        "category": "👋 Selamlaşma & İletişim",
        "hand_shape": "bye_wave",
        "description": "Açık el karşıya dönük parmaklar yukarıda öne-arkaya hafifçe sallanır.",
        "tips": "Ayrılırken kullanılan veda hareketidir.",
        "keyboard_char": "GÜLE GÜLE"
    },
    {
        "word": "ADIN NE?",
        "category": "👋 Selamlaşma & İletişim",
        "hand_shape": "name_ask",
        "description": "İşaret ve orta parmak göğüs hizasında çapraz vuruş yapar, ardından soru mimiğiyle karşıya bakılır.",
        "tips": "Kaşlar hafif kaldırılarak soru sorulduğu vurgulanır.",
        "keyboard_char": "ADIN NE?"
    },
    {
        "word": "BENİM ADIM",
        "category": "👋 Selamlaşma & İletişim",
        "hand_shape": "my_name",
        "description": "Sağ el işaret parmağı önce göğse dokunur (BEN), sonra iki parmak göğüs önünde 'isim' işareti yapar.",
        "tips": "Ardından kişi kendi isminin harflerini kodlar.",
        "keyboard_char": "BENİM ADIM"
    },

    # -------------------------------------------------------------
    # 🤝 NEZAKET & İFADELER
    # -------------------------------------------------------------
    {
        "word": "TEŞEKKÜR EDERİM",
        "category": "🤝 Nezaket & İfadeler",
        "hand_shape": "chin_to_front",
        "description": "Düz açık elin parmak uçları çeneye veya dudağa hafifçe dokundurulur, ardından saygıyla karşıya doğru uzatılır.",
        "tips": "Baş hafifçe öne eğilerek nezaket hissettirilir.",
        "keyboard_char": "TEŞEKKÜR EDERİM"
    },
    {
        "word": "LÜTFEN",
        "category": "🤝 Nezaket & İfadeler",
        "hand_shape": "chest_circle",
        "description": "Açık sağ el göğsün üzerinde dairesel hareketle hafifçe ovulur.",
        "tips": "Yalvarma veya rica ifadesi katan içten bir harekettir.",
        "keyboard_char": "LÜTFEN"
    },
    {
        "word": "ÖZÜR DİLERİM",
        "category": "🤝 Nezaket & İfadeler",
        "hand_shape": "fist_chest_circle",
        "description": "Yumruk yapılmış sağ el göğüs hizasında dairesel olarak gezdirilir, yüz ifadesinde mahcubiyet vardır.",
        "tips": "Kaşlar çatık veya hafif üzgün bir yüz ifadesiyle tamamlanır.",
        "keyboard_char": "ÖZÜR DİLERİM"
    },
    {
        "word": "RİCA EDERİM",
        "category": "🤝 Nezaket & İfadeler",
        "hand_shape": "open_hands_down",
        "description": "İki el açık avuçlar yukarı bakarken hafifçe öne doğru açılır.",
        "tips": "'Bir şey değil, memnuniyetle' anlamını taşır.",
        "keyboard_char": "RİCA EDERİM"
    },
    {
        "word": "KOLAY GELSİN",
        "category": "🤝 Nezaket & İfadeler",
        "hand_shape": "work_easy",
        "description": "İki elin işaret ve başparmakları hafif yaylanır gibi öne doğru ritmik hareket ettirilir.",
        "tips": "Çalışan birine başarı ve kolaylık dileğidir.",
        "keyboard_char": "KOLAY GELSİN"
    },
    {
        "word": "GEÇMİŞ OLSUN",
        "category": "🤝 Nezaket & İfadeler",
        "hand_shape": "pass_away",
        "description": "Sağ el göğüs önünden hızla ileri ve yana doğru savrularak hastalığın/zorluğun geçip gitmesi anlatılır.",
        "tips": "Üzüntü ve şifa dileği barındırır.",
        "keyboard_char": "GEÇMİŞ OLSUN"
    },

    # -------------------------------------------------------------
    # ✅ ONAY & TEMEL CEVAPLAR
    # -------------------------------------------------------------
    {
        "word": "EVET",
        "category": "✅ Onay & Temel Cevaplar",
        "hand_shape": "thumbs_up",
        "description": "Sağ el yumruk yapılır, başparmak dimdik yukarı kalkar (Thumbs Up) veya yumruk yukarı-aşağı baş sallar gibi hareket eder.",
        "tips": "Başla da onaylama hareketi yapılır. En evrensel onaylama jestidir.",
        "keyboard_char": "EVET"
    },
    {
        "word": "HAYIR",
        "category": "✅ Onay & Temel Cevaplar",
        "hand_shape": "index_wag",
        "description": "İşaret parmağı yukarı dik, diğer parmaklar kapalıdır; işaret parmağı ve bilek iki yana 'cık cık' der gibi sallanır.",
        "tips": "Baş da iki yana sallanarak red ifadesi güçlendirilir.",
        "keyboard_char": "HAYIR"
    },
    {
        "word": "TAMAM",
        "category": "✅ Onay & Temel Cevaplar",
        "hand_shape": "ok_sign",
        "description": "Başparmak ve işaret parmağı uçları birleşerek halka oluşturur, diğer 3 parmak dik ve açıktır.",
        "tips": "Anlaşıldı, her şey yolunda anlamında kullanılır.",
        "keyboard_char": "TAMAM"
    },
    {
        "word": "VAR",
        "category": "✅ Onay & Temel Cevaplar",
        "hand_shape": "hand_grab_down",
        "description": "Açık el hafifçe bükülerek göğüs önünde aşağı doğru indirilir, sanki bir şeyi tutmuş gibi.",
        "tips": "Mevcudiyeti bildirir.",
        "keyboard_char": "VAR"
    },
    {
        "word": "YOK",
        "category": "✅ Onay & Temel Cevaplar",
        "hand_shape": "hand_flip_away",
        "description": "Avuç içi yukarıdayken bilek hızla ters çevrilerek avuç dışarı bakar şekilde savrulur.",
        "tips": "'Hiç kalmadı / bulunmuyor' jestidir.",
        "keyboard_char": "YOK"
    },
    {
        "word": "DOĞRU",
        "category": "✅ Onay & Temel Cevaplar",
        "hand_shape": "index_straight",
        "description": "İşaret parmağı öne doğru düz uzatılıp onaylar gibi tek bir net vuruşla indirilir.",
        "tips": "Haklısın / kesinlikle doğru anlamındadır.",
        "keyboard_char": "DOĞRU"
    },
    {
        "word": "YANLIŞ",
        "category": "✅ Onay & Temel Cevaplar",
        "hand_shape": "cross_hands",
        "description": "İki elin işaret parmakları veya eller çarpı (X) oluşturacak şekilde birbirinin önüne geçer.",
        "tips": "Hata veya yanlışlık belirtir.",
        "keyboard_char": "YANLIŞ"
    },

    # -------------------------------------------------------------
    # ❤️ DUYGULAR & HÂL HATIR
    # -------------------------------------------------------------
    {
        "word": "SENİ SEVİYORUM",
        "category": "❤️ Duygular & Hâl Hatır",
        "hand_shape": "ily_sign",
        "description": "Başparmak, işaret ve serçe parmak dimdik açık; orta ve yüzük parmakları avuç içine kapalıdır (ILY Jesti).",
        "tips": "Sevgi ve bağlılığı ifade eden çok güçlü bir TİD/uluslararası işarettir.",
        "keyboard_char": "SENİ SEVİYORUM"
    },
    {
        "word": "NASILSIN?",
        "category": "❤️ Duygular & Hâl Hatır",
        "hand_shape": "chest_question",
        "description": "İki el açık göğse dokundurulup ardından avuçlar yukarı bakar şekilde öne açılır.",
        "tips": "Kaşlar kaldırılarak meraklı bir yüz ifadesi takınılır.",
        "keyboard_char": "NASILSIN?"
    },
    {
        "word": "İYİYİM",
        "category": "❤️ Duygular & Hâl Hatır",
        "hand_shape": "chest_good",
        "description": "Sağ elin başparmağı dik yukarıda veya açık el göğüste kalbin üzerine konarak gülümsenir.",
        "tips": "Rahat ve memnun bir yüz ifadesi şarttır.",
        "keyboard_char": "İYİYİM"
    },
    {
        "word": "KÖTÜYÜM",
        "category": "❤️ Duygular & Hâl Hatır",
        "hand_shape": "thumbs_down_frown",
        "description": "Başparmak aşağı dönük (Thumbs Down) tutulur ve yüz ifadesi asık, üzgün yapılır.",
        "tips": "Halsizlik, mutsuzluk veya hastalık durumunda kullanılır.",
        "keyboard_char": "KÖTÜYÜM"
    },
    {
        "word": "MUTLU",
        "category": "❤️ Duygular & Hâl Hatır",
        "hand_shape": "happy_flutter",
        "description": "İki el açık göğüs hizasında hafif dairesel yukarı doğru dalgalandırılır ve geniş gülümseme yapılır.",
        "tips": "Mimikler sevincin büyüklüğünü gösterir.",
        "keyboard_char": "MUTLU"
    },
    {
        "word": "ÜZGÜN",
        "category": "❤️ Duygular & Hâl Hatır",
        "hand_shape": "sad_tear",
        "description": "İşaret parmağı göz altından yanağa doğru gözyaşı süzülür gibi yavaşça indirilir.",
        "tips": "Hüzünlü bir yüz ifadesi ile desteklenir.",
        "keyboard_char": "ÜZGÜN"
    },

    # -------------------------------------------------------------
    # ❓ SORU KELİMELERİ
    # -------------------------------------------------------------
    {
        "word": "NE?",
        "category": "❓ Soru Kelimeleri",
        "hand_shape": "shrug_hands",
        "description": "İki el dirseklerden bükülü, avuç içleri yukarı bakar vaziyette iki yana hafifçe açılır.",
        "tips": "Omuzlar hafif kalkar, kaşlar çatılır.",
        "keyboard_char": "NE?"
    },
    {
        "word": "NEREDE?",
        "category": "❓ Soru Kelimeleri",
        "hand_shape": "point_search",
        "description": "İşaret parmağı karşıya bakar vaziyette el sağa-sola arar gibi taranır.",
        "tips": "Konum sormak için kullanılır.",
        "keyboard_char": "NEREDE?"
    },
    {
        "word": "NASIL?",
        "category": "❓ Soru Kelimeleri",
        "hand_shape": "how_turn",
        "description": "Bitişik eller göğüs hizasında birbirine paralelken bileklerden öne doğru çevrilir.",
        "tips": "Yöntem veya durum sorma jestidir.",
        "keyboard_char": "NASIL?"
    },
    {
        "word": "NE ZAMAN?",
        "category": "❓ Soru Kelimeleri",
        "hand_shape": "wrist_tap",
        "description": "İşaret parmağıyla diğer kolun bileğine (saat yerine) iki kez vurulur veya parmaklar açılır.",
        "tips": "Zaman sormak için kullanılır.",
        "keyboard_char": "NE ZAMAN?"
    },
    {
        "word": "KİM?",
        "category": "❓ Soru Kelimeleri",
        "hand_shape": "chin_tap",
        "description": "İşaret parmağı çeneye bir iki kez dokundurulur, kaşlar çatılarak kişi sorulur.",
        "tips": "Birisini tanımak veya sormak içindir.",
        "keyboard_char": "KİM?"
    },
    {
        "word": "NEDEN? / NİÇİN?",
        "category": "❓ Soru Kelimeleri",
        "hand_shape": "forehead_why",
        "description": "İşaret parmağı alnın yanına götürülür ve hafif bükülerek soru mimiği yapılır.",
        "tips": "Sebep arayışını gösterir.",
        "keyboard_char": "NEDEN?"
    },

    # -------------------------------------------------------------
    # 🍞 GÜNLÜK YAŞAM & İHTİYAÇLAR
    # -------------------------------------------------------------
    {
        "word": "SU",
        "category": "🍞 Günlük Yaşam & İhtiyaçlar",
        "hand_shape": "water_cup",
        "description": "El 'C' şeklinde avuç içi ağıza doğru tutulup baş hafifçe arkaya eğilerek su içme taklidi yapılır.",
        "tips": "Temel yaşamsal ihtiyaçtır, çok sık kullanılır.",
        "keyboard_char": "SU"
    },
    {
        "word": "YEMEK",
        "category": "🍞 Günlük Yaşam & İhtiyaçlar",
        "hand_shape": "eat_fingers",
        "description": "Tüm parmak uçları birleştirilerek ağıza doğru bir iki kez götürülüp getirilir.",
        "tips": "Yemek yeme eylemini simgeler.",
        "keyboard_char": "YEMEK"
    },
    {
        "word": "ÇAY",
        "category": "🍞 Günlük Yaşam & İhtiyaçlar",
        "hand_shape": "tea_stir",
        "description": "Bir el fincan tabağı gibi açık dururken diğer el çay kaşığı tutar gibi dairesel karıştırma yapar.",
        "tips": "Türk kültürünün ayrılmaz işaretidir.",
        "keyboard_char": "ÇAY"
    },
    {
        "word": "EKMEK",
        "category": "🍞 Günlük Yaşam & İhtiyaçlar",
        "hand_shape": "bread_slice",
        "description": "Sol kol yatay tutulur (somun ekmek), sağ el bıçak gibi dilimleme hareketi yapar.",
        "tips": "Ekmek kesme simülasyonudur.",
        "keyboard_char": "EKMEK"
    },
    {
        "word": "TUVALET",
        "category": "🍞 Günlük Yaşam & İhtiyaçlar",
        "hand_shape": "wc_shake",
        "description": "'T' harfi yapılan el hafifçe iki yana sallanır (İngilizcedeki Toilet benzeri) veya işaret parmağı burun altına götürülür.",
        "tips": "Acil ihtiyaç anlarında hayat kurtarır.",
        "keyboard_char": "TUVALET"
    },
    {
        "word": "EV",
        "category": "🍞 Günlük Yaşam & İhtiyaçlar",
        "hand_shape": "roof_shape",
        "description": "İki elin parmak uçları yukarıda üçgen çatı oluşturacak şekilde birbirine değdirilir.",
        "tips": "Ev çatısı şeklidir.",
        "keyboard_char": "EV"
    },
    {
        "word": "OKUL",
        "category": "🍞 Günlük Yaşam & İhtiyaçlar",
        "hand_shape": "book_open",
        "description": "İki el avuçları yukarı bakacak şekilde bitişiktir, sanki bir kitap açılır gibi iki yana ayrılır.",
        "tips": "Eğitim ve kitap metaforu içerir.",
        "keyboard_char": "OKUL"
    },
    {
        "word": "HASTANE",
        "category": "🍞 Günlük Yaşam & İhtiyaçlar",
        "hand_shape": "red_cross",
        "description": "İşaret parmağıyla sol omuz/kol üzerine artı (+) işareti çizilir.",
        "tips": "Kızılay/Kızılhaç sembolüne atıftır.",
        "keyboard_char": "HASTANE"
    },
    {
        "word": "PARA",
        "category": "🍞 Günlük Yaşam & İhtiyaçlar",
        "hand_shape": "money_rub",
        "description": "Başparmak, işaret ve orta parmak uçları birbirine sürtülerek para sayma hareketi yapılır.",
        "tips": "Maddi ödeme veya satın alma anlatır.",
        "keyboard_char": "PARA"
    },

    # -------------------------------------------------------------
    # 🚨 ACİL DURUM & SAĞLIK
    # -------------------------------------------------------------
    {
        "word": "YARDIM",
        "category": "🚨 Acil Durum & Sağlık",
        "hand_shape": "help_lift",
        "description": "Sol el yumruk yapılmış sağ elin altına destek gibi girer ve iki el birden yukarı doğru kaldırılır.",
        "tips": "Destek olma, kaldırma anlamındadır. Çok önemlidir.",
        "keyboard_char": "YARDIM"
    },
    {
        "word": "ACİL",
        "category": "🚨 Acil Durum & Sağlık",
        "hand_shape": "urgent_wave",
        "description": "İki el açıkça hızla aşağı yukarı hareket ettirilir, yüz ifadesinde endişe ve telaş vardır.",
        "tips": "Hemen müdahale gerektiren durumlardır.",
        "keyboard_char": "ACİL"
    },
    {
        "word": "DOKTOR",
        "category": "🚨 Acil Durum & Sağlık",
        "hand_shape": "pulse_check",
        "description": "İki parmakla bilekteki nabız noktasına dokunarak nabız ölçme taklidi yapılır.",
        "tips": "Tıbbi personeli simgeler.",
        "keyboard_char": "DOKTOR"
    },
    {
        "word": "POLİS",
        "category": "🚨 Acil Durum & Sağlık",
        "hand_shape": "police_cap",
        "description": "Sağ elin başparmak ve işaret parmağı alnın üzerine şapka siperliği gibi konur.",
        "tips": "Polis şapkasını temsil eder.",
        "keyboard_char": "POLİS"
    },
    {
        "word": "AMBULANS",
        "category": "🚨 Acil Durum & Sağlık",
        "hand_shape": "siren_rotate",
        "description": "Açık sağ el baş üstünde tepe lambası gibi döndürülür.",
        "tips": "Acil durum aracı çağrısıdır.",
        "keyboard_char": "AMBULANS"
    },
    {
        "word": "DUR",
        "category": "🚨 Acil Durum & Sağlık",
        "hand_shape": "stop_palm",
        "description": "Açık el avuç içi dimdik karşıya bakar şekilde sert ve kararlı biçimde ileri uzatılır.",
        "tips": "Net ve evrensel bir durdurma işaretidir.",
        "keyboard_char": "DUR"
    },

    # -------------------------------------------------------------
    # ⌨️ KLAVYE & SİSTEM KOMUTLARI
    # -------------------------------------------------------------
    {
        "word": "<SİL> (Backspace)",
        "category": "⌨️ Klavye & Sistem Komutları",
        "hand_shape": "thumbs_down",
        "description": "Başparmak açık ve net biçimde aşağı doğru tutulur (Thumbs Down).",
        "tips": "Son yazılan kelimeyi veya karakteri anında siler.",
        "keyboard_char": "<SİL>"
    },
    {
        "word": "<GÖNDER> (Enter)",
        "category": "⌨️ Klavye & Sistem Komutları",
        "hand_shape": "victory_peace",
        "description": "İşaret ve orta parmak açık zafer (Peace/V) işareti yapılır.",
        "tips": "WhatsApp'ta veya mesajlaşma uygulamasında Enter tuşuna basarak mesajı gönderir.",
        "keyboard_char": "<GÖNDER>"
    },
    {
        "word": "<BOŞLUK> (Space)",
        "category": "⌨️ Klavye & Sistem Komutları",
        "hand_shape": "flat_horizontal",
        "description": "Sağ el yatay tutulup başparmak yana açılır veya açık el yatay bir çizgi çizer.",
        "tips": "Kelimeler arasına bir adet boşluk karakteri ekler.",
        "keyboard_char": "<BOŞLUK>"
    },
    {
        "word": "<TEMİZLE> (Clear)",
        "category": "⌨️ Klavye & Sistem Komutları",
        "hand_shape": "wipe_surface",
        "description": "İki el avuçları aşağı bakacak şekilde göğüs hizasından yanlara doğru açılarak silme yapılır.",
        "tips": "Metin tamponunu tamamen temizler.",
        "keyboard_char": "<TEMİZLE>"
    }
]
