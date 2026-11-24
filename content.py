# -*- coding: utf-8 -*-
"""Texts of the Nailgoal legal pages, one block per language.

A section is (heading, [paragraph, ...]). A paragraph is a string, or a list of
strings for a bullet list. {NAME}, {ADDRESS}, {EMAIL} are filled in by build.py,
{G1} and {G2} become links to Google's policies.

Keep this in line with what the app really does (nailsoccer repo: AdMob interstitial
after matches only, UMP consent, ATT on iOS, "Play Ad-Free" purchase, local storage
only, no analytics). If the app starts collecting something new, update every
language here, the App Store privacy answers and the Play Data safety form.
"""

PRIVACY_URL_GOOGLE = "https://policies.google.com/privacy"
GOOGLE_ADS_URL = "https://policies.google.com/technologies/partner-sites"

LANGS = {}

# ---------------------------------------------------------------- English
LANGS["en"] = dict(
    name="English", dir="ltr",
    nav=dict(home="Home", privacy="Privacy", support="Support", legal="Legal notice"),
    updated_label="Last updated",
    privacy_title="Privacy Policy – Nailgoal",
    privacy=[
        ("1. Who is responsible", [
            "The publisher of the game “Nailgoal” and controller of personal data is: {NAME}, {ADDRESS}. Email: {EMAIL}",
        ]),
        ("2. In short", [
            "Nailgoal needs no account and no registration, and we never ask for your name, email address or phone number. Your settings stay on your device. The game uses one outside service: Google AdMob, for ads shown after some matches. In the European Economic Area, the United Kingdom and Switzerland, personalised ads are only used with your consent. If you buy “Play Ad-Free”, the payment is handled by Apple or Google. The game has no analytics and no crash reporting of its own.",
        ]),
        ("3. Data on your device", [
            "Your settings (language, volume, field, game type, goals to win), a counter of matches played since the last ad, and whether you bought “Play Ad-Free” are stored only in the game's local storage on your device. We do not receive them. If you delete the game, this data is deleted too.",
        ]),
        ("4. Ads (Google AdMob)", [
            "After some matches the game shows a full-screen ad. There are no banners and no ads during play. For this, the Google Mobile Ads SDK (Google Ireland Limited / Google LLC) may process data such as your IP address, device identifiers (for example the advertising ID), device and app information and your interaction with the ad, in order to deliver and measure ads and to prevent fraud.",
            "In the European Economic Area, the United Kingdom and Switzerland we ask for your consent first (Google's consent form). You can review or change your choice at any time in the game under Settings → “Privacy options”. Whether ads are personalised depends on your choice and your device settings. You can also reset or delete your advertising ID in your phone's settings.",
            "On iPhone and iPad, the game may also show Apple's “Allow to track” prompt (App Tracking Transparency). If you choose “Ask App Not to Track”, your advertising identifier (IDFA) is not used for ads. You can change this at any time in your device settings under Privacy & Security → Tracking.",
            "More: Google's privacy policy ({G1}) and “How Google uses information from sites or apps that use our services” ({G2}).",
        ]),
        ("5. Purchases (Play Ad-Free)", [
            "You can buy “Play Ad-Free” once in the game (Settings → “Play Ad-Free”). It removes the ads after matches for good. The payment is handled entirely by Apple (App Store) or Google (Google Play) under their own terms and privacy policies. We do not receive your name, email address or payment details. The store only tells the game whether you own the purchase, and the game stores this on your device. On a new iPhone or iPad you can restore it under Settings → “Restore Purchases”; on Android it is restored automatically.",
        ]),
        ("6. What we do not do", [
            "We do not create user accounts, sell data, run our own analytics, or access your location, contacts, photos, camera or microphone. Besides internet access, the game only uses the app store's purchase service and, on iPhone and iPad, Apple's tracking prompt for ads. The game itself works offline; the internet is only used for ads and purchases.",
        ]),
        ("7. Legal bases (GDPR)", [
            ["Ads in the EEA, the UK and Switzerland: your consent (Art. 6(1)(a) GDPR, § 25(1) TDDDG).",
             "Elsewhere: our legitimate interest in financing the free game with ads (Art. 6(1)(f) GDPR).",
             "Purchases: performance of the contract (Art. 6(1)(b) GDPR).",
             "Answering your emails: Art. 6(1)(f) GDPR."],
        ]),
        ("8. Transfers to third countries", [
            "Google may process data outside the European Economic Area (including the USA) on the basis of EU Standard Contractual Clauses or the EU-US Data Privacy Framework.",
        ]),
        ("9. Your rights", [
            "You have the right of access, rectification, erasure, restriction of processing, data portability and objection, and the right to withdraw consent at any time with effect for the future (Settings → “Privacy options”). You can also complain to a data protection supervisory authority. Write to us at {EMAIL}. Because we store no personal data on our own servers, most of this is settled by deleting the game and through Google's settings.",
        ]),
        ("10. Age", [
            "Nailgoal is a game for a general audience aged 13 and over. It is not directed at children under 13.",
        ]),
        ("11. Changes", [
            "We may update this policy, for example when the game changes. The current date is shown at the top.",
        ]),
    ],
    support_title="Support – Nailgoal",
    support=[
        ("Contact", ["Questions, problems or ideas? Write to us: {EMAIL}"]),
        ("Frequently asked questions", [
            ["How to play: drag back from anywhere on the board to aim the coin like a slingshot, then let go. The “?” button on the main menu explains the rules.",
             "Play Ad-Free: Settings → “Play Ad-Free”. On a new iPhone or iPad or after reinstalling, tap Settings → “Restore Purchases”. On Android the purchase is restored automatically.",
             "Ad privacy: Settings → “Privacy options” (shown where consent is required).",
             "The game froze or crashed: please write to us with your device model and what you were doing."],
        ]),
    ],
    legal_title="Legal notice",
    legal=[
        ("Information according to § 5 DDG", ["{NAME}", "{ADDRESS}"]),
        ("Contact", ["Email: {EMAIL}"]),
    ],
)

# ---------------------------------------------------------------- Deutsch
LANGS["de"] = dict(
    name="Deutsch", dir="ltr",
    nav=dict(home="Start", privacy="Datenschutz", support="Support", legal="Impressum"),
    updated_label="Stand",
    privacy_title="Datenschutzerklärung – Nailgoal",
    privacy=[
        ("1. Verantwortlicher", [
            "Anbieter des Spiels „Nailgoal“ und Verantwortlicher für personenbezogene Daten ist: {NAME}, {ADDRESS}. E-Mail: {EMAIL}",
        ]),
        ("2. Kurz gesagt", [
            "Nailgoal braucht kein Konto und keine Registrierung, und wir fragen nie nach deinem Namen, deiner E-Mail-Adresse oder Telefonnummer. Deine Einstellungen bleiben auf deinem Gerät. Das Spiel nutzt einen externen Dienst: Google AdMob für Werbung nach einigen Spielen. Im Europäischen Wirtschaftsraum, im Vereinigten Königreich und in der Schweiz wird personalisierte Werbung nur mit deiner Einwilligung genutzt. Wenn du „Werbefrei spielen“ kaufst, wickeln Apple oder Google die Zahlung ab. Das Spiel hat keine eigene Analyse und keine eigenen Absturzberichte.",
        ]),
        ("3. Daten auf deinem Gerät", [
            "Deine Einstellungen (Sprache, Lautstärke, Spielfeld, Spielart, Tore zum Sieg), ein Zähler der Spiele seit der letzten Werbung und ob du „Werbefrei spielen“ gekauft hast, werden nur im lokalen Speicher des Spiels auf deinem Gerät gespeichert. Wir erhalten diese Daten nicht. Wenn du das Spiel löschst, werden auch diese Daten gelöscht.",
        ]),
        ("4. Werbung (Google AdMob)", [
            "Nach einigen Spielen zeigt das Spiel eine Vollbildwerbung. Es gibt keine Banner und keine Werbung während des Spielens. Dafür kann das Google Mobile Ads SDK (Google Ireland Limited / Google LLC) Daten wie deine IP-Adresse, Gerätekennungen (zum Beispiel die Werbe-ID), Geräte- und App-Informationen und deine Interaktion mit der Werbung verarbeiten, um Werbung auszuliefern, zu messen und Betrug zu verhindern.",
            "Im Europäischen Wirtschaftsraum, im Vereinigten Königreich und in der Schweiz fragen wir zuerst nach deiner Einwilligung (Einwilligungsformular von Google). Du kannst deine Auswahl jederzeit im Spiel unter Einstellungen → „Datenschutzoptionen“ prüfen oder ändern. Ob Werbung personalisiert wird, hängt von deiner Auswahl und deinen Geräteeinstellungen ab. Deine Werbe-ID kannst du außerdem in den Einstellungen deines Telefons zurücksetzen oder löschen.",
            "Auf iPhone und iPad kann das Spiel außerdem Apples Abfrage „Tracking erlauben“ anzeigen (App Tracking Transparency). Wenn du „App bitten, kein Tracking durchzuführen“ wählst, wird deine Werbe-ID (IDFA) nicht für Werbung genutzt. Das kannst du jederzeit in den Geräteeinstellungen unter Datenschutz & Sicherheit → Tracking ändern.",
            "Mehr: Datenschutzerklärung von Google ({G1}) und „Wie Google Daten von Websites oder Apps verwendet, die Google-Dienste nutzen“ ({G2}).",
        ]),
        ("5. Käufe (Werbefrei spielen)", [
            "Du kannst „Werbefrei spielen“ einmalig im Spiel kaufen (Einstellungen → „Werbefrei spielen“). Damit entfällt die Werbung nach den Spielen dauerhaft. Die Zahlung wickeln ausschließlich Apple (App Store) oder Google (Google Play) nach ihren eigenen Bedingungen und Datenschutzerklärungen ab. Wir erhalten weder deinen Namen noch deine E-Mail-Adresse noch Zahlungsdaten. Der Store teilt dem Spiel nur mit, ob du den Kauf besitzt; das Spiel speichert das auf deinem Gerät. Auf einem neuen iPhone oder iPad kannst du ihn unter Einstellungen → „Käufe wiederherstellen“ wiederherstellen; auf Android geschieht das automatisch.",
        ]),
        ("6. Was wir nicht tun", [
            "Wir legen keine Benutzerkonten an, verkaufen keine Daten, betreiben keine eigene Analyse und greifen nicht auf deinen Standort, deine Kontakte, Fotos, Kamera oder dein Mikrofon zu. Neben dem Internetzugang nutzt das Spiel nur den Kaufdienst des App-Stores und auf iPhone und iPad Apples Tracking-Abfrage für Werbung. Das Spiel selbst funktioniert offline; das Internet wird nur für Werbung und Käufe genutzt.",
        ]),
        ("7. Rechtsgrundlagen (DSGVO)", [
            ["Werbung im EWR, im Vereinigten Königreich und in der Schweiz: deine Einwilligung (Art. 6 Abs. 1 lit. a DSGVO, § 25 Abs. 1 TDDDG).",
             "Anderswo: unser berechtigtes Interesse, das kostenlose Spiel durch Werbung zu finanzieren (Art. 6 Abs. 1 lit. f DSGVO).",
             "Käufe: Vertragserfüllung (Art. 6 Abs. 1 lit. b DSGVO).",
             "Beantwortung deiner E-Mails: Art. 6 Abs. 1 lit. f DSGVO."],
        ]),
        ("8. Übermittlung in Drittländer", [
            "Google kann Daten außerhalb des Europäischen Wirtschaftsraums (auch in den USA) verarbeiten, auf Grundlage der EU-Standardvertragsklauseln oder des EU-US Data Privacy Framework.",
        ]),
        ("9. Deine Rechte", [
            "Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht, eine Einwilligung jederzeit mit Wirkung für die Zukunft zu widerrufen (Einstellungen → „Datenschutzoptionen“). Du kannst dich außerdem bei einer Datenschutz-Aufsichtsbehörde beschweren. Schreib uns an {EMAIL}. Da wir keine personenbezogenen Daten auf eigenen Servern speichern, erledigt sich das meiste durch Löschen des Spiels und über die Einstellungen von Google.",
        ]),
        ("10. Alter", [
            "Nailgoal ist ein Spiel für ein allgemeines Publikum ab 13 Jahren. Es richtet sich nicht an Kinder unter 13 Jahren.",
        ]),
        ("11. Änderungen", [
            "Wir können diese Erklärung anpassen, zum Beispiel wenn sich das Spiel ändert. Das aktuelle Datum steht oben.",
        ]),
    ],
    support_title="Support – Nailgoal",
    support=[
        ("Kontakt", ["Fragen, Probleme oder Ideen? Schreib uns: {EMAIL}"]),
        ("Häufige Fragen", [
            ["So wird gespielt: Zieh irgendwo auf dem Brett zurück, um die Münze wie mit einer Steinschleuder zu zielen, und lass los. Die Schaltfläche „?“ im Hauptmenü erklärt die Regeln.",
             "Werbefrei spielen: Einstellungen → „Werbefrei spielen“. Auf einem neuen iPhone oder iPad oder nach einer Neuinstallation: Einstellungen → „Käufe wiederherstellen“. Auf Android wird der Kauf automatisch wiederhergestellt.",
             "Datenschutz bei Werbung: Einstellungen → „Datenschutzoptionen“ (wird angezeigt, wo eine Einwilligung nötig ist).",
             "Das Spiel hängt oder stürzt ab: Bitte schreib uns dein Gerätemodell und was du gerade gemacht hast."],
        ]),
    ],
    legal_title="Impressum",
    legal=[
        ("Angaben gemäß § 5 DDG", ["{NAME}", "{ADDRESS}"]),
        ("Kontakt", ["E-Mail: {EMAIL}"]),
    ],
)

# ---------------------------------------------------------------- Türkçe
LANGS["tr"] = dict(
    name="Türkçe", dir="ltr",
    nav=dict(home="Ana sayfa", privacy="Gizlilik", support="Destek", legal="Künye"),
    updated_label="Son güncelleme",
    privacy_title="Gizlilik Politikası – Nailgoal",
    privacy=[
        ("1. Sorumlu", [
            "“Nailgoal” oyununun yayıncısı ve kişisel verilerden sorumlu kişi: {NAME}, {ADDRESS}. E-posta: {EMAIL}",
        ]),
        ("2. Kısaca", [
            "Nailgoal hesap ya da kayıt gerektirmez; adınızı, e-posta adresinizi veya telefon numaranızı asla sormayız. Ayarlarınız cihazınızda kalır. Oyun tek bir dış hizmet kullanır: bazı maçlardan sonra gösterilen reklamlar için Google AdMob. Avrupa Ekonomik Alanı, Birleşik Krallık ve İsviçre'de kişiselleştirilmiş reklamlar yalnızca izninizle kullanılır. “Reklamsız Oyna”yı satın alırsanız ödemeyi Apple veya Google işler. Oyunun kendine ait analiz veya çökme raporlaması yoktur.",
        ]),
        ("3. Cihazınızdaki veriler", [
            "Ayarlarınız (dil, ses düzeyi, zemin, oyun türü, hedef gol), son reklamdan beri oynanan maç sayacı ve “Reklamsız Oyna”yı satın alıp almadığınız yalnızca oyunun cihazınızdaki yerel depolamasında tutulur. Bu verileri biz almayız. Oyunu silerseniz bu veriler de silinir.",
        ]),
        ("4. Reklamlar (Google AdMob)", [
            "Oyun bazı maçlardan sonra tam ekran bir reklam gösterir. Banner yoktur, oyun sırasında reklam yoktur. Bunun için Google Mobile Ads SDK (Google Ireland Limited / Google LLC), reklamları sunmak, ölçmek ve dolandırıcılığı önlemek amacıyla IP adresiniz, cihaz tanımlayıcıları (örneğin reklam kimliği), cihaz ve uygulama bilgileri ve reklamla etkileşiminiz gibi verileri işleyebilir.",
            "Avrupa Ekonomik Alanı, Birleşik Krallık ve İsviçre'de önce izninizi isteriz (Google'ın izin formu). Seçiminizi oyunda Ayarlar → “Gizlilik seçenekleri” altında istediğiniz zaman görebilir veya değiştirebilirsiniz. Reklamların kişiselleştirilip kişiselleştirilmeyeceği seçiminize ve cihaz ayarlarınıza bağlıdır. Reklam kimliğinizi telefonunuzun ayarlarından sıfırlayabilir veya silebilirsiniz.",
            "iPhone ve iPad'de oyun ayrıca Apple'ın “İzlemeye izin ver” penceresini gösterebilir (App Tracking Transparency). “Uygulamadan İzlememesini İste”yi seçerseniz reklam kimliğiniz (IDFA) reklamlar için kullanılmaz. Bunu istediğiniz zaman cihaz ayarlarında Gizlilik ve Güvenlik → İzleme altından değiştirebilirsiniz.",
            "Daha fazlası: Google'ın gizlilik politikası ({G1}) ve “Google, hizmetlerimizi kullanan site veya uygulamalardan gelen bilgileri nasıl kullanır” ({G2}).",
        ]),
        ("5. Satın alma (Reklamsız Oyna)", [
            "“Reklamsız Oyna”yı oyunda bir kez satın alabilirsiniz (Ayarlar → “Reklamsız Oyna”). Maç sonu reklamlarını kalıcı olarak kaldırır. Ödemeyi tamamen Apple (App Store) veya Google (Google Play) kendi koşulları ve gizlilik politikaları çerçevesinde işler. Adınızı, e-posta adresinizi veya ödeme bilgilerinizi almayız. Mağaza oyuna yalnızca satın almaya sahip olup olmadığınızı bildirir; oyun bunu cihazınızda saklar. Yeni bir iPhone veya iPad'de Ayarlar → “Satın alımları geri yükle” ile geri yükleyebilirsiniz; Android'de kendiliğinden geri yüklenir.",
        ]),
        ("6. Yapmadıklarımız", [
            "Kullanıcı hesabı oluşturmayız, veri satmayız, kendi analizimizi yapmayız; konumunuza, kişilerinize, fotoğraflarınıza, kameranıza veya mikrofonunuza erişmeyiz. Oyun, internet erişimi dışında yalnızca uygulama mağazasının satın alma hizmetini ve iPhone/iPad'de reklamlar için Apple'ın izleme penceresini kullanır. Oyunun kendisi çevrimdışı çalışır; internet yalnızca reklamlar ve satın alma için kullanılır.",
        ]),
        ("7. Hukuki dayanaklar (GDPR)", [
            ["AEA, Birleşik Krallık ve İsviçre'de reklamlar: izniniz (GDPR md. 6(1)(a), TDDDG § 25(1)).",
             "Diğer yerlerde: ücretsiz oyunu reklamla finanse etmedeki meşru menfaatimiz (GDPR md. 6(1)(f)).",
             "Satın alma: sözleşmenin ifası (GDPR md. 6(1)(b)).",
             "E-postalarınızı yanıtlamak: GDPR md. 6(1)(f)."],
        ]),
        ("8. Üçüncü ülkelere aktarım", [
            "Google verileri Avrupa Ekonomik Alanı dışında (ABD dahil) AB Standart Sözleşme Maddeleri veya AB-ABD Veri Gizliliği Çerçevesi temelinde işleyebilir.",
        ]),
        ("9. Haklarınız", [
            "Erişim, düzeltme, silme, işlemeyi kısıtlama, veri taşınabilirliği ve itiraz haklarına, ayrıca izninizi gelecekte geçerli olmak üzere istediğiniz zaman geri çekme hakkına sahipsiniz (Ayarlar → “Gizlilik seçenekleri”). Bir veri koruma denetim makamına da şikâyette bulunabilirsiniz. Bize {EMAIL} adresinden yazın. Kişisel verileri kendi sunucularımızda saklamadığımız için bunların çoğu oyunu silerek ve Google'ın ayarlarından halledilir.",
        ]),
        ("10. Yaş", [
            "Nailgoal 13 yaş ve üzeri genel kitleye yönelik bir oyundur. 13 yaşın altındaki çocuklara yönelik değildir.",
        ]),
        ("11. Değişiklikler", [
            "Bu politikayı, örneğin oyun değiştiğinde, güncelleyebiliriz. Güncel tarih en üstte yazar.",
        ]),
    ],
    support_title="Destek – Nailgoal",
    support=[
        ("İletişim", ["Soru, sorun ya da fikir mi var? Bize yazın: {EMAIL}"]),
        ("Sık sorulan sorular", [
            ["Nasıl oynanır: tahtanın herhangi bir yerinden geri çekerek parayı sapan gibi nişan alın ve bırakın. Ana menüdeki “?” düğmesi kuralları anlatır.",
             "Reklamsız Oyna: Ayarlar → “Reklamsız Oyna”. Yeni bir iPhone/iPad'de ya da yeniden yükledikten sonra Ayarlar → “Satın alımları geri yükle”. Android'de satın alma kendiliğinden geri yüklenir.",
             "Reklam gizliliği: Ayarlar → “Gizlilik seçenekleri” (izin gereken yerlerde görünür).",
             "Oyun dondu ya da çöktü: lütfen cihaz modelinizi ve ne yaptığınızı yazın."],
        ]),
    ],
    legal_title="Künye",
    legal=[
        ("§ 5 DDG uyarınca bilgiler", ["{NAME}", "{ADDRESS}"]),
        ("İletişim", ["E-posta: {EMAIL}"]),
    ],
)

# ---------------------------------------------------------------- Français
LANGS["fr"] = dict(
    name="Français", dir="ltr",
    nav=dict(home="Accueil", privacy="Confidentialité", support="Assistance", legal="Mentions légales"),
    updated_label="Dernière mise à jour",
    privacy_title="Politique de confidentialité – Nailgoal",
    privacy=[
        ("1. Responsable", [
            "L'éditeur du jeu « Nailgoal » et responsable du traitement des données personnelles est : {NAME}, {ADDRESS}. E-mail : {EMAIL}",
        ]),
        ("2. En bref", [
            "Nailgoal ne nécessite ni compte ni inscription, et nous ne demandons jamais ton nom, ton adresse e-mail ou ton numéro de téléphone. Tes réglages restent sur ton appareil. Le jeu utilise un seul service externe : Google AdMob, pour les publicités affichées après certains matchs. Dans l'Espace économique européen, au Royaume-Uni et en Suisse, les publicités personnalisées ne sont utilisées qu'avec ton consentement. Si tu achètes « Jouer sans pub », le paiement est géré par Apple ou Google. Le jeu n'a ni statistiques ni rapports de plantage propres.",
        ]),
        ("3. Données sur ton appareil", [
            "Tes réglages (langue, volume, terrain, type de jeu, buts pour gagner), un compteur des matchs joués depuis la dernière publicité et le fait d'avoir acheté « Jouer sans pub » sont enregistrés uniquement dans le stockage local du jeu sur ton appareil. Nous ne les recevons pas. Si tu supprimes le jeu, ces données sont supprimées aussi.",
        ]),
        ("4. Publicités (Google AdMob)", [
            "Après certains matchs, le jeu affiche une publicité en plein écran. Il n'y a ni bannières ni publicités pendant le jeu. Pour cela, le SDK Google Mobile Ads (Google Ireland Limited / Google LLC) peut traiter des données comme ton adresse IP, des identifiants de l'appareil (par exemple l'identifiant publicitaire), des informations sur l'appareil et l'application et ton interaction avec la publicité, afin de diffuser et mesurer les publicités et de prévenir la fraude.",
            "Dans l'Espace économique européen, au Royaume-Uni et en Suisse, nous demandons d'abord ton consentement (formulaire de consentement de Google). Tu peux consulter ou modifier ton choix à tout moment dans le jeu sous Paramètres → « Options de confidentialité ». La personnalisation des publicités dépend de ton choix et des réglages de ton appareil. Tu peux aussi réinitialiser ou supprimer ton identifiant publicitaire dans les réglages de ton téléphone.",
            "Sur iPhone et iPad, le jeu peut aussi afficher la demande d'Apple « Autoriser le suivi » (App Tracking Transparency). Si tu choisis « Demander à l'app de ne pas me suivre », ton identifiant publicitaire (IDFA) n'est pas utilisé pour les publicités. Tu peux le modifier à tout moment dans les réglages de l'appareil sous Confidentialité et sécurité → Suivi.",
            "En savoir plus : règles de confidentialité de Google ({G1}) et « Comment Google utilise les informations des sites ou applications qui utilisent ses services » ({G2}).",
        ]),
        ("5. Achats (Jouer sans pub)", [
            "Tu peux acheter « Jouer sans pub » une seule fois dans le jeu (Paramètres → « Jouer sans pub »). Cela supprime définitivement les publicités après les matchs. Le paiement est entièrement géré par Apple (App Store) ou Google (Google Play) selon leurs propres conditions et règles de confidentialité. Nous ne recevons ni ton nom, ni ton adresse e-mail, ni tes données de paiement. La boutique indique seulement au jeu si tu possèdes l'achat ; le jeu l'enregistre sur ton appareil. Sur un nouvel iPhone ou iPad, tu peux le récupérer sous Paramètres → « Restaurer les achats » ; sur Android, c'est automatique.",
        ]),
        ("6. Ce que nous ne faisons pas", [
            "Nous ne créons pas de comptes, ne vendons pas de données, ne faisons pas nos propres statistiques et n'accédons ni à ta position, ni à tes contacts, photos, appareil photo ou micro. En plus de l'accès à Internet, le jeu utilise seulement le service d'achat de la boutique et, sur iPhone et iPad, la demande de suivi d'Apple pour les publicités. Le jeu lui-même fonctionne hors ligne ; Internet ne sert qu'aux publicités et aux achats.",
        ]),
        ("7. Bases légales (RGPD)", [
            ["Publicités dans l'EEE, au Royaume-Uni et en Suisse : ton consentement (art. 6, par. 1, point a) RGPD, § 25, al. 1 TDDDG).",
             "Ailleurs : notre intérêt légitime à financer le jeu gratuit par la publicité (art. 6, par. 1, point f) RGPD).",
             "Achats : exécution du contrat (art. 6, par. 1, point b) RGPD).",
             "Réponse à tes e-mails : art. 6, par. 1, point f) RGPD."],
        ]),
        ("8. Transferts vers des pays tiers", [
            "Google peut traiter des données en dehors de l'Espace économique européen (y compris aux États-Unis) sur la base des clauses contractuelles types de l'UE ou du cadre de protection des données UE-États-Unis.",
        ]),
        ("9. Tes droits", [
            "Tu as le droit d'accès, de rectification, d'effacement, de limitation du traitement, de portabilité et d'opposition, ainsi que le droit de retirer ton consentement à tout moment pour l'avenir (Paramètres → « Options de confidentialité »). Tu peux aussi déposer une plainte auprès d'une autorité de protection des données. Écris-nous à {EMAIL}. Comme nous ne stockons aucune donnée personnelle sur nos propres serveurs, la plupart de ces droits s'exercent en supprimant le jeu et via les réglages de Google.",
        ]),
        ("10. Âge", [
            "Nailgoal est un jeu pour un public général de 13 ans et plus. Il ne s'adresse pas aux enfants de moins de 13 ans.",
        ]),
        ("11. Modifications", [
            "Nous pouvons mettre à jour cette politique, par exemple lorsque le jeu change. La date actuelle figure en haut.",
        ]),
    ],
    support_title="Assistance – Nailgoal",
    support=[
        ("Contact", ["Des questions, des problèmes ou des idées ? Écris-nous : {EMAIL}"]),
        ("Questions fréquentes", [
            ["Comment jouer : tire en arrière n'importe où sur le plateau pour viser avec la pièce comme avec un lance-pierre, puis relâche. Le bouton « ? » du menu principal explique les règles.",
             "Jouer sans pub : Paramètres → « Jouer sans pub ». Sur un nouvel iPhone ou iPad ou après une réinstallation : Paramètres → « Restaurer les achats ». Sur Android, l'achat est restauré automatiquement.",
             "Confidentialité des publicités : Paramètres → « Options de confidentialité » (affiché là où le consentement est requis).",
             "Le jeu s'est figé ou a planté : écris-nous en indiquant le modèle de ton appareil et ce que tu faisais."],
        ]),
    ],
    legal_title="Mentions légales",
    legal=[
        ("Informations selon le § 5 DDG", ["{NAME}", "{ADDRESS}"]),
        ("Contact", ["E-mail : {EMAIL}"]),
    ],
)

# ---------------------------------------------------------------- Italiano
LANGS["it"] = dict(
    name="Italiano", dir="ltr",
    nav=dict(home="Home", privacy="Privacy", support="Assistenza", legal="Note legali"),
    updated_label="Ultimo aggiornamento",
    privacy_title="Informativa sulla privacy – Nailgoal",
    privacy=[
        ("1. Titolare", [
            "L'editore del gioco “Nailgoal” e titolare del trattamento dei dati personali è: {NAME}, {ADDRESS}. E-mail: {EMAIL}",
        ]),
        ("2. In breve", [
            "Nailgoal non richiede alcun account né registrazione e non chiediamo mai il tuo nome, indirizzo e-mail o numero di telefono. Le tue impostazioni restano sul tuo dispositivo. Il gioco usa un solo servizio esterno: Google AdMob, per gli annunci mostrati dopo alcune partite. Nello Spazio economico europeo, nel Regno Unito e in Svizzera gli annunci personalizzati vengono usati solo con il tuo consenso. Se acquisti “Gioca senza pubblicità”, il pagamento è gestito da Apple o Google. Il gioco non ha statistiche né report sugli arresti anomali propri.",
        ]),
        ("3. Dati sul tuo dispositivo", [
            "Le tue impostazioni (lingua, volume, campo, tipo di gioco, gol per vincere), un contatore delle partite giocate dall'ultimo annuncio e l'eventuale acquisto di “Gioca senza pubblicità” sono salvati solo nella memoria locale del gioco sul tuo dispositivo. Noi non li riceviamo. Se elimini il gioco, vengono eliminati anche questi dati.",
        ]),
        ("4. Annunci (Google AdMob)", [
            "Dopo alcune partite il gioco mostra un annuncio a schermo intero. Non ci sono banner né annunci durante il gioco. A tal fine, l'SDK Google Mobile Ads (Google Ireland Limited / Google LLC) può trattare dati come il tuo indirizzo IP, identificatori del dispositivo (ad esempio l'ID pubblicità), informazioni sul dispositivo e sull'app e la tua interazione con l'annuncio, per pubblicare e misurare gli annunci e prevenire le frodi.",
            "Nello Spazio economico europeo, nel Regno Unito e in Svizzera chiediamo prima il tuo consenso (modulo di consenso di Google). Puoi rivedere o modificare la tua scelta in qualsiasi momento nel gioco in Impostazioni → “Opzioni privacy”. La personalizzazione degli annunci dipende dalla tua scelta e dalle impostazioni del dispositivo. Puoi anche reimpostare o eliminare l'ID pubblicità nelle impostazioni del telefono.",
            "Su iPhone e iPad il gioco può mostrare anche la richiesta di Apple “Consenti il tracciamento” (App Tracking Transparency). Se scegli “Chiedi all'app di non tracciare”, il tuo identificatore pubblicitario (IDFA) non viene usato per gli annunci. Puoi cambiarlo in qualsiasi momento nelle impostazioni del dispositivo in Privacy e sicurezza → Tracciamento.",
            "Per saperne di più: informativa sulla privacy di Google ({G1}) e “Come Google utilizza le informazioni dei siti o delle app che utilizzano i suoi servizi” ({G2}).",
        ]),
        ("5. Acquisti (Gioca senza pubblicità)", [
            "Puoi acquistare “Gioca senza pubblicità” una sola volta nel gioco (Impostazioni → “Gioca senza pubblicità”). Rimuove per sempre gli annunci dopo le partite. Il pagamento è gestito interamente da Apple (App Store) o Google (Google Play) secondo i loro termini e le loro informative sulla privacy. Non riceviamo il tuo nome, indirizzo e-mail o dati di pagamento. Lo store comunica al gioco solo se possiedi l'acquisto; il gioco lo salva sul tuo dispositivo. Su un nuovo iPhone o iPad puoi ripristinarlo in Impostazioni → “Ripristina acquisti”; su Android avviene automaticamente.",
        ]),
        ("6. Cosa non facciamo", [
            "Non creiamo account, non vendiamo dati, non raccogliamo statistiche proprie e non accediamo alla tua posizione, ai contatti, alle foto, alla fotocamera o al microfono. Oltre all'accesso a Internet, il gioco usa solo il servizio di acquisto dello store e, su iPhone e iPad, la richiesta di tracciamento di Apple per gli annunci. Il gioco funziona offline; Internet serve solo per annunci e acquisti.",
        ]),
        ("7. Basi giuridiche (GDPR)", [
            ["Annunci nel SEE, nel Regno Unito e in Svizzera: il tuo consenso (art. 6, par. 1, lett. a GDPR, § 25, c. 1 TDDDG).",
             "Altrove: il nostro legittimo interesse a finanziare il gioco gratuito con la pubblicità (art. 6, par. 1, lett. f GDPR).",
             "Acquisti: esecuzione del contratto (art. 6, par. 1, lett. b GDPR).",
             "Risposta alle tue e-mail: art. 6, par. 1, lett. f GDPR."],
        ]),
        ("8. Trasferimenti verso paesi terzi", [
            "Google può trattare dati al di fuori dello Spazio economico europeo (anche negli Stati Uniti) sulla base delle clausole contrattuali tipo dell'UE o del quadro UE-USA per la protezione dei dati.",
        ]),
        ("9. I tuoi diritti", [
            "Hai diritto di accesso, rettifica, cancellazione, limitazione del trattamento, portabilità e opposizione, nonché il diritto di revocare il consenso in qualsiasi momento con effetto per il futuro (Impostazioni → “Opzioni privacy”). Puoi anche presentare reclamo a un'autorità di controllo per la protezione dei dati. Scrivici a {EMAIL}. Poiché non conserviamo dati personali su server nostri, la maggior parte di questi diritti si esercita eliminando il gioco e tramite le impostazioni di Google.",
        ]),
        ("10. Età", [
            "Nailgoal è un gioco per un pubblico generale dai 13 anni in su. Non è rivolto a bambini sotto i 13 anni.",
        ]),
        ("11. Modifiche", [
            "Possiamo aggiornare questa informativa, ad esempio quando il gioco cambia. La data attuale è indicata in alto.",
        ]),
    ],
    support_title="Assistenza – Nailgoal",
    support=[
        ("Contatto", ["Domande, problemi o idee? Scrivici: {EMAIL}"]),
        ("Domande frequenti", [
            ["Come si gioca: trascina all'indietro in un punto qualsiasi del tavolo per mirare con la moneta come con una fionda, poi rilascia. Il pulsante “?” nel menu principale spiega le regole.",
             "Gioca senza pubblicità: Impostazioni → “Gioca senza pubblicità”. Su un nuovo iPhone o iPad o dopo una reinstallazione: Impostazioni → “Ripristina acquisti”. Su Android l'acquisto viene ripristinato automaticamente.",
             "Privacy degli annunci: Impostazioni → “Opzioni privacy” (visibile dove è richiesto il consenso).",
             "Il gioco si è bloccato o chiuso: scrivici indicando il modello del dispositivo e cosa stavi facendo."],
        ]),
    ],
    legal_title="Note legali",
    legal=[
        ("Informazioni ai sensi del § 5 DDG", ["{NAME}", "{ADDRESS}"]),
        ("Contatto", ["E-mail: {EMAIL}"]),
    ],
)

# ---------------------------------------------------------------- Bahasa Indonesia
LANGS["id"] = dict(
    name="Bahasa Indonesia", dir="ltr",
    nav=dict(home="Beranda", privacy="Privasi", support="Bantuan", legal="Informasi hukum"),
    updated_label="Terakhir diperbarui",
    privacy_title="Kebijakan Privasi – Nailgoal",
    privacy=[
        ("1. Pihak yang bertanggung jawab", [
            "Penerbit game “Nailgoal” dan pengendali data pribadi adalah: {NAME}, {ADDRESS}. Email: {EMAIL}",
        ]),
        ("2. Singkatnya", [
            "Nailgoal tidak memerlukan akun atau pendaftaran, dan kami tidak pernah meminta nama, alamat email, atau nomor telepon Anda. Pengaturan Anda tetap di perangkat Anda. Game ini hanya menggunakan satu layanan luar: Google AdMob, untuk iklan yang ditampilkan setelah beberapa pertandingan. Di Wilayah Ekonomi Eropa, Inggris, dan Swiss, iklan yang dipersonalisasi hanya digunakan dengan persetujuan Anda. Jika Anda membeli “Main Tanpa Iklan”, pembayaran diproses oleh Apple atau Google. Game ini tidak memiliki analitik atau laporan error sendiri.",
        ]),
        ("3. Data di perangkat Anda", [
            "Pengaturan Anda (bahasa, volume, lapangan, jenis permainan, target gol), penghitung pertandingan sejak iklan terakhir, dan apakah Anda membeli “Main Tanpa Iklan” hanya disimpan di penyimpanan lokal game di perangkat Anda. Kami tidak menerimanya. Jika Anda menghapus game, data ini juga ikut terhapus.",
        ]),
        ("4. Iklan (Google AdMob)", [
            "Setelah beberapa pertandingan, game menampilkan iklan layar penuh. Tidak ada banner dan tidak ada iklan saat bermain. Untuk itu, Google Mobile Ads SDK (Google Ireland Limited / Google LLC) dapat memproses data seperti alamat IP Anda, pengenal perangkat (misalnya ID iklan), informasi perangkat dan aplikasi, serta interaksi Anda dengan iklan, untuk menayangkan dan mengukur iklan serta mencegah penipuan.",
            "Di Wilayah Ekonomi Eropa, Inggris, dan Swiss, kami meminta persetujuan Anda terlebih dahulu (formulir persetujuan Google). Anda dapat melihat atau mengubah pilihan Anda kapan saja di game melalui Pengaturan → “Opsi privasi”. Apakah iklan dipersonalisasi bergantung pada pilihan dan pengaturan perangkat Anda. Anda juga dapat mengatur ulang atau menghapus ID iklan di pengaturan ponsel Anda.",
            "Di iPhone dan iPad, game juga dapat menampilkan permintaan Apple “Izinkan pelacakan” (App Tracking Transparency). Jika Anda memilih “Minta App untuk Tidak Melacak”, pengenal iklan Anda (IDFA) tidak digunakan untuk iklan. Anda dapat mengubahnya kapan saja di pengaturan perangkat pada Privasi & Keamanan → Pelacakan.",
            "Selengkapnya: kebijakan privasi Google ({G1}) dan “Cara Google menggunakan informasi dari situs atau aplikasi yang menggunakan layanan kami” ({G2}).",
        ]),
        ("5. Pembelian (Main Tanpa Iklan)", [
            "Anda dapat membeli “Main Tanpa Iklan” satu kali di game (Pengaturan → “Main Tanpa Iklan”). Ini menghapus iklan setelah pertandingan untuk selamanya. Pembayaran sepenuhnya diproses oleh Apple (App Store) atau Google (Google Play) sesuai ketentuan dan kebijakan privasi mereka. Kami tidak menerima nama, alamat email, atau detail pembayaran Anda. Toko hanya memberi tahu game apakah Anda memiliki pembelian tersebut, dan game menyimpannya di perangkat Anda. Di iPhone atau iPad baru, Anda dapat memulihkannya melalui Pengaturan → “Pulihkan Pembelian”; di Android pemulihan terjadi otomatis.",
        ]),
        ("6. Yang tidak kami lakukan", [
            "Kami tidak membuat akun pengguna, tidak menjual data, tidak menjalankan analitik sendiri, dan tidak mengakses lokasi, kontak, foto, kamera, atau mikrofon Anda. Selain akses internet, game hanya menggunakan layanan pembelian toko aplikasi dan, di iPhone dan iPad, permintaan pelacakan Apple untuk iklan. Game ini sendiri berjalan offline; internet hanya digunakan untuk iklan dan pembelian.",
        ]),
        ("7. Dasar hukum (GDPR)", [
            ["Iklan di EEA, Inggris, dan Swiss: persetujuan Anda (Pasal 6(1)(a) GDPR, § 25(1) TDDDG).",
             "Di tempat lain: kepentingan sah kami untuk membiayai game gratis dengan iklan (Pasal 6(1)(f) GDPR).",
             "Pembelian: pelaksanaan kontrak (Pasal 6(1)(b) GDPR).",
             "Menjawab email Anda: Pasal 6(1)(f) GDPR."],
        ]),
        ("8. Transfer ke negara ketiga", [
            "Google dapat memproses data di luar Wilayah Ekonomi Eropa (termasuk Amerika Serikat) berdasarkan Klausul Kontrak Standar UE atau Kerangka Privasi Data UE-AS.",
        ]),
        ("9. Hak Anda", [
            "Anda memiliki hak akses, perbaikan, penghapusan, pembatasan pemrosesan, portabilitas data, dan keberatan, serta hak untuk menarik persetujuan kapan saja untuk ke depannya (Pengaturan → “Opsi privasi”). Anda juga dapat mengajukan keluhan ke otoritas pengawas perlindungan data. Tulis kepada kami di {EMAIL}. Karena kami tidak menyimpan data pribadi di server kami sendiri, sebagian besar hal ini diselesaikan dengan menghapus game dan melalui pengaturan Google.",
        ]),
        ("10. Usia", [
            "Nailgoal adalah game untuk khalayak umum berusia 13 tahun ke atas. Game ini tidak ditujukan untuk anak di bawah 13 tahun.",
        ]),
        ("11. Perubahan", [
            "Kami dapat memperbarui kebijakan ini, misalnya saat game berubah. Tanggal terbaru tertera di bagian atas.",
        ]),
    ],
    support_title="Bantuan – Nailgoal",
    support=[
        ("Kontak", ["Ada pertanyaan, masalah, atau ide? Tulis kepada kami: {EMAIL}"]),
        ("Pertanyaan umum", [
            ["Cara bermain: tarik ke belakang dari mana saja di papan untuk membidik koin seperti ketapel, lalu lepaskan. Tombol “?” di menu utama menjelaskan aturannya.",
             "Main Tanpa Iklan: Pengaturan → “Main Tanpa Iklan”. Di iPhone atau iPad baru atau setelah instal ulang: Pengaturan → “Pulihkan Pembelian”. Di Android pembelian dipulihkan otomatis.",
             "Privasi iklan: Pengaturan → “Opsi privasi” (muncul di wilayah yang memerlukan persetujuan).",
             "Game macet atau tertutup sendiri: tulis kepada kami dengan model perangkat Anda dan apa yang sedang Anda lakukan."],
        ]),
    ],
    legal_title="Informasi hukum",
    legal=[
        ("Informasi sesuai § 5 DDG", ["{NAME}", "{ADDRESS}"]),
        ("Kontak", ["Email: {EMAIL}"]),
    ],
)
# ---------------------------------------------------------------- Русский
LANGS["ru"] = dict(
    name="Русский", dir="ltr",
    nav=dict(home="Главная", privacy="Конфиденциальность", support="Поддержка", legal="Выходные данные"),
    updated_label="Последнее обновление",
    privacy_title="Политика конфиденциальности – Nailgoal",
    privacy=[
        ("1. Ответственное лицо", [
            "Издатель игры «Nailgoal» и оператор персональных данных: {NAME}, {ADDRESS}. Эл. почта: {EMAIL}",
        ]),
        ("2. Коротко", [
            "Nailgoal не требует учётной записи и регистрации, и мы никогда не спрашиваем ваше имя, адрес эл. почты или номер телефона. Ваши настройки остаются на вашем устройстве. Игра использует только один внешний сервис: Google AdMob — для рекламы, которая показывается после некоторых матчей. В Европейской экономической зоне, Великобритании и Швейцарии персонализированная реклама используется только с вашего согласия. Если вы покупаете «Играть без рекламы», оплату обрабатывает Apple или Google. У игры нет собственной аналитики и отчётов о сбоях.",
        ]),
        ("3. Данные на вашем устройстве", [
            "Ваши настройки (язык, громкость, покрытие, тип игры, голов до победы), счётчик матчей с последней рекламы и информация о покупке «Играть без рекламы» хранятся только в локальном хранилище игры на вашем устройстве. Мы их не получаем. Если вы удалите игру, эти данные тоже удалятся.",
        ]),
        ("4. Реклама (Google AdMob)", [
            "После некоторых матчей игра показывает полноэкранную рекламу. Баннеров и рекламы во время игры нет. Для этого Google Mobile Ads SDK (Google Ireland Limited / Google LLC) может обрабатывать такие данные, как ваш IP-адрес, идентификаторы устройства (например, рекламный идентификатор), сведения об устройстве и приложении и ваше взаимодействие с рекламой — чтобы показывать и измерять рекламу и предотвращать мошенничество.",
            "В Европейской экономической зоне, Великобритании и Швейцарии мы сначала запрашиваем ваше согласие (форма согласия Google). Вы можете в любой момент просмотреть или изменить свой выбор в игре: Настройки → «Настройки конфиденциальности». Будет ли реклама персонализированной, зависит от вашего выбора и настроек устройства. Рекламный идентификатор также можно сбросить или удалить в настройках телефона.",
            "На iPhone и iPad игра может также показать запрос Apple «Разрешить отслеживание» (App Tracking Transparency). Если вы выберете «Попросить приложение не отслеживать», ваш рекламный идентификатор (IDFA) не используется для рекламы. Это можно изменить в любой момент в настройках устройства: Конфиденциальность и безопасность → Отслеживание.",
            "Подробнее: политика конфиденциальности Google ({G1}) и «Как Google использует информацию с сайтов и из приложений, которые используют сервисы Google» ({G2}).",
        ]),
        ("5. Покупки («Играть без рекламы»)", [
            "«Играть без рекламы» можно купить в игре один раз (Настройки → «Играть без рекламы»). Покупка навсегда убирает рекламу после матчей. Оплату полностью обрабатывает Apple (App Store) или Google (Google Play) по своим условиям и политикам конфиденциальности. Мы не получаем ваше имя, адрес эл. почты или платёжные данные. Магазин сообщает игре только, есть ли у вас покупка; игра сохраняет это на устройстве. На новом iPhone или iPad покупку можно восстановить: Настройки → «Восстановить покупки»; на Android она восстанавливается автоматически.",
        ]),
        ("6. Чего мы не делаем", [
            "Мы не создаём учётные записи, не продаём данные, не ведём собственную аналитику и не получаем доступ к вашему местоположению, контактам, фото, камере или микрофону. Помимо доступа в интернет, игра использует только сервис покупок магазина приложений и на iPhone и iPad — запрос Apple на отслеживание для рекламы. Сама игра работает офлайн; интернет нужен только для рекламы и покупок.",
        ]),
        ("7. Правовые основания (GDPR)", [
            ["Реклама в ЕЭЗ, Великобритании и Швейцарии: ваше согласие (ст. 6(1)(a) GDPR, § 25(1) TDDDG).",
             "В других странах: наш законный интерес в финансировании бесплатной игры за счёт рекламы (ст. 6(1)(f) GDPR).",
             "Покупки: исполнение договора (ст. 6(1)(b) GDPR).",
             "Ответы на ваши письма: ст. 6(1)(f) GDPR."],
        ]),
        ("8. Передача в третьи страны", [
            "Google может обрабатывать данные за пределами Европейской экономической зоны (в том числе в США) на основании стандартных договорных положений ЕС или Рамочного соглашения о защите данных ЕС–США.",
        ]),
        ("9. Ваши права", [
            "Вы имеете право на доступ, исправление, удаление, ограничение обработки, переносимость данных и возражение, а также право в любой момент отозвать согласие на будущее (Настройки → «Настройки конфиденциальности»). Вы также можете подать жалобу в надзорный орган по защите данных. Пишите нам: {EMAIL}. Поскольку мы не храним персональные данные на собственных серверах, большинство вопросов решается удалением игры и через настройки Google.",
        ]),
        ("10. Возраст", [
            "Nailgoal — игра для широкой аудитории от 13 лет. Она не предназначена для детей младше 13 лет.",
        ]),
        ("11. Изменения", [
            "Мы можем обновлять эту политику, например при изменении игры. Актуальная дата указана вверху.",
        ]),
    ],
    support_title="Поддержка – Nailgoal",
    support=[
        ("Контакты", ["Вопросы, проблемы или идеи? Напишите нам: {EMAIL}"]),
        ("Частые вопросы", [
            ["Как играть: потяните назад в любом месте доски, чтобы прицелиться монетой, как из рогатки, и отпустите. Кнопка «?» в главном меню объясняет правила.",
             "Играть без рекламы: Настройки → «Играть без рекламы». На новом iPhone или iPad или после переустановки: Настройки → «Восстановить покупки». На Android покупка восстанавливается автоматически.",
             "Конфиденциальность рекламы: Настройки → «Настройки конфиденциальности» (показывается там, где требуется согласие).",
             "Игра зависла или вылетела: напишите нам модель устройства и что вы делали."],
        ]),
    ],
    legal_title="Выходные данные",
    legal=[
        ("Сведения согласно § 5 DDG", ["{NAME}", "{ADDRESS}"]),
        ("Контакты", ["Эл. почта: {EMAIL}"]),
    ],
)

# ---------------------------------------------------------------- 日本語
LANGS["ja"] = dict(
    name="日本語", dir="ltr",
    nav=dict(home="ホーム", privacy="プライバシー", support="サポート", legal="運営者情報"),
    updated_label="最終更新日",
    privacy_title="プライバシーポリシー – Nailgoal",
    privacy=[
        ("1. 責任者", [
            "ゲーム「Nailgoal」の提供者および個人データの管理者：{NAME}、{ADDRESS}。メール：{EMAIL}",
        ]),
        ("2. 概要", [
            "Nailgoal はアカウントも登録も不要で、お名前・メールアドレス・電話番号をお聞きすることはありません。設定はお使いの端末に保存されます。ゲームが利用する外部サービスは 1 つだけです：一部の試合の後に表示される広告のための Google AdMob。欧州経済領域、英国、スイスでは、パーソナライズ広告はお客様の同意がある場合にのみ使用されます。「広告なしでプレイ」を購入する場合、支払いは Apple または Google が処理します。ゲーム独自のアクセス解析やクラッシュレポートはありません。",
        ]),
        ("3. 端末内のデータ", [
            "設定（言語、音量、フィールド、ゲームの種類、勝利ゴール数）、前回の広告以降の試合数カウンター、「広告なしでプレイ」の購入有無は、端末内のゲームのローカルストレージにのみ保存されます。私たちがこれらを受け取ることはありません。ゲームを削除すると、これらのデータも削除されます。",
        ]),
        ("4. 広告（Google AdMob）", [
            "一部の試合の後に、全画面広告が表示されます。バナー広告やプレイ中の広告はありません。このため、Google Mobile Ads SDK（Google Ireland Limited / Google LLC）は、広告の配信・効果測定・不正防止のために、IP アドレス、端末識別子（広告 ID など）、端末やアプリの情報、広告への操作などのデータを処理することがあります。",
            "欧州経済領域、英国、スイスでは、まずお客様の同意を求めます（Google の同意フォーム）。選択内容はゲーム内の 設定 →「プライバシー設定」でいつでも確認・変更できます。広告がパーソナライズされるかどうかは、お客様の選択と端末の設定によります。広告 ID は端末の設定からリセットまたは削除することもできます。",
            "iPhone と iPad では、Apple の「トラッキングを許可」の確認（App Tracking Transparency）が表示されることがあります。「Appにトラッキングしないように要求」を選ぶと、広告識別子（IDFA）は広告に使用されません。これは端末の設定の プライバシーとセキュリティ → トラッキング でいつでも変更できます。",
            "詳しくは：Google のプライバシーポリシー（{G1}）および「Google のサービスを使用するサイトやアプリから収集した情報の Google による使用」（{G2}）。",
        ]),
        ("5. 購入（広告なしでプレイ）", [
            "「広告なしでプレイ」はゲーム内で 1 回だけ購入できます（設定 →「広告なしでプレイ」）。試合後の広告がずっと表示されなくなります。支払いは Apple（App Store）または Google（Google Play）が、それぞれの規約とプライバシーポリシーに基づいてすべて処理します。私たちがお名前、メールアドレス、支払い情報を受け取ることはありません。ストアはゲームに購入済みかどうかだけを伝え、ゲームはそれを端末に保存します。新しい iPhone や iPad では 設定 →「購入を復元」で復元できます。Android では自動的に復元されます。",
        ]),
        ("6. 私たちが行わないこと", [
            "アカウントの作成、データの販売、独自のアクセス解析は行わず、位置情報、連絡先、写真、カメラ、マイクにもアクセスしません。インターネット接続のほかに、ゲームが使用するのはアプリストアの購入サービスと、iPhone・iPad での広告用の Apple のトラッキング確認だけです。ゲーム自体はオフラインで動作し、インターネットは広告と購入にのみ使用されます。",
        ]),
        ("7. 法的根拠（GDPR）", [
            ["EEA、英国、スイスでの広告：お客様の同意（GDPR 第 6 条 1 項 a、TDDDG 第 25 条 1 項）。",
             "その他の地域：無料ゲームを広告で運営するという当方の正当な利益（GDPR 第 6 条 1 項 f）。",
             "購入：契約の履行（GDPR 第 6 条 1 項 b）。",
             "メールへの返信：GDPR 第 6 条 1 項 f。"],
        ]),
        ("8. 第三国への移転", [
            "Google は、EU 標準契約条項または EU-米国データプライバシーフレームワークに基づき、欧州経済領域外（米国を含む）でデータを処理することがあります。",
        ]),
        ("9. お客様の権利", [
            "お客様には、アクセス、訂正、消去、処理の制限、データポータビリティ、異議申し立ての権利があり、また将来に向けていつでも同意を撤回する権利があります（設定 →「プライバシー設定」）。データ保護監督機関に苦情を申し立てることもできます。お問い合わせは {EMAIL} まで。当方のサーバーに個人データを保存していないため、ほとんどの場合はゲームの削除と Google の設定で対応できます。",
        ]),
        ("10. 年齢", [
            "Nailgoal は 13 歳以上の一般向けのゲームです。13 歳未満のお子様を対象としていません。",
        ]),
        ("11. 変更", [
            "ゲームの変更時などに、このポリシーを更新することがあります。最新の日付は上部に記載されています。",
        ]),
    ],
    support_title="サポート – Nailgoal",
    support=[
        ("お問い合わせ", ["ご質問、問題、アイデアはこちらへ：{EMAIL}"]),
        ("よくある質問", [
            ["遊び方：ボード上のどこからでも後ろに引いて、パチンコのようにコインの狙いを定めて離します。メインメニューの「?」ボタンでルールを確認できます。",
             "広告なしでプレイ：設定 →「広告なしでプレイ」。新しい iPhone・iPad や再インストール後は 設定 →「購入を復元」。Android では購入が自動的に復元されます。",
             "広告のプライバシー：設定 →「プライバシー設定」（同意が必要な地域で表示されます）。",
             "ゲームが止まった・落ちた：端末の機種と、そのとき何をしていたかをお知らせください。"],
        ]),
    ],
    legal_title="運営者情報",
    legal=[
        ("§ 5 DDG に基づく表示", ["{NAME}", "{ADDRESS}"]),
        ("お問い合わせ", ["メール：{EMAIL}"]),
    ],
)

# ---------------------------------------------------------------- 한국어
LANGS["ko"] = dict(
    name="한국어", dir="ltr",
    nav=dict(home="홈", privacy="개인정보", support="지원", legal="법적 고지"),
    updated_label="최종 업데이트",
    privacy_title="개인정보 처리방침 – Nailgoal",
    privacy=[
        ("1. 책임자", [
            "게임 「Nailgoal」의 제공자이자 개인정보 처리 책임자: {NAME}, {ADDRESS}. 이메일: {EMAIL}",
        ]),
        ("2. 요약", [
            "Nailgoal은 계정이나 가입이 필요 없으며, 이름, 이메일 주소, 전화번호를 묻지 않습니다. 설정은 기기에만 저장됩니다. 게임은 외부 서비스를 하나만 사용합니다: 일부 경기 후 표시되는 광고를 위한 Google AdMob. 유럽경제지역, 영국, 스위스에서는 맞춤형 광고가 사용자의 동의가 있을 때만 사용됩니다. 「광고 없이 플레이」를 구매하면 결제는 Apple 또는 Google이 처리합니다. 게임 자체의 분석이나 오류 보고 기능은 없습니다.",
        ]),
        ("3. 기기에 저장되는 데이터", [
            "설정(언어, 음량, 경기장, 게임 종류, 목표 골), 마지막 광고 이후 경기 수, 「광고 없이 플레이」 구매 여부는 기기의 게임 로컬 저장소에만 저장됩니다. 저희는 이 정보를 받지 않습니다. 게임을 삭제하면 이 데이터도 함께 삭제됩니다.",
        ]),
        ("4. 광고 (Google AdMob)", [
            "일부 경기 후 전체 화면 광고가 표시됩니다. 배너 광고나 플레이 중 광고는 없습니다. 이를 위해 Google Mobile Ads SDK(Google Ireland Limited / Google LLC)는 광고 게재·측정 및 부정 행위 방지를 위해 IP 주소, 기기 식별자(예: 광고 ID), 기기 및 앱 정보, 광고와의 상호작용 등의 데이터를 처리할 수 있습니다.",
            "유럽경제지역, 영국, 스위스에서는 먼저 동의를 요청합니다(Google 동의 양식). 선택 사항은 게임의 설정 → 「개인정보 옵션」에서 언제든지 확인하거나 변경할 수 있습니다. 맞춤형 광고 여부는 사용자의 선택과 기기 설정에 따라 달라집니다. 광고 ID는 휴대전화 설정에서 재설정하거나 삭제할 수도 있습니다.",
            "iPhone과 iPad에서는 Apple의 「추적 허용」 요청(App Tracking Transparency)이 표시될 수 있습니다. 「앱에 추적 금지 요청」을 선택하면 광고 식별자(IDFA)가 광고에 사용되지 않습니다. 이는 기기 설정의 개인정보 보호 및 보안 → 추적에서 언제든지 변경할 수 있습니다.",
            "자세히: Google 개인정보처리방침({G1}) 및 「Google 서비스를 사용하는 사이트 또는 앱의 정보를 Google이 사용하는 방법」({G2}).",
        ]),
        ("5. 구매 (광고 없이 플레이)", [
            "「광고 없이 플레이」는 게임에서 한 번만 구매할 수 있습니다(설정 → 「광고 없이 플레이」). 경기 후 광고가 영구적으로 제거됩니다. 결제는 전적으로 Apple(App Store) 또는 Google(Google Play)이 자체 약관과 개인정보처리방침에 따라 처리합니다. 저희는 이름, 이메일 주소, 결제 정보를 받지 않습니다. 스토어는 구매 보유 여부만 게임에 알려 주고, 게임은 이를 기기에 저장합니다. 새 iPhone이나 iPad에서는 설정 → 「구매 복원」으로 복원할 수 있으며, Android에서는 자동으로 복원됩니다.",
        ]),
        ("6. 하지 않는 일", [
            "저희는 계정을 만들거나 데이터를 판매하지 않으며, 자체 분석을 하지 않고, 위치, 연락처, 사진, 카메라, 마이크에 접근하지 않습니다. 인터넷 접속 외에 게임은 앱 스토어의 구매 서비스와 iPhone·iPad에서 광고를 위한 Apple의 추적 요청만 사용합니다. 게임 자체는 오프라인으로 작동하며, 인터넷은 광고와 구매에만 사용됩니다.",
        ]),
        ("7. 법적 근거 (GDPR)", [
            ["EEA, 영국, 스위스의 광고: 사용자의 동의(GDPR 제6조 제1항 a호, TDDDG 제25조 제1항).",
             "그 외 지역: 무료 게임을 광고로 운영하려는 정당한 이익(GDPR 제6조 제1항 f호).",
             "구매: 계약 이행(GDPR 제6조 제1항 b호).",
             "이메일 답변: GDPR 제6조 제1항 f호."],
        ]),
        ("8. 제3국 이전", [
            "Google은 EU 표준계약조항 또는 EU-미국 데이터 프라이버시 프레임워크에 따라 유럽경제지역 밖(미국 포함)에서 데이터를 처리할 수 있습니다.",
        ]),
        ("9. 사용자의 권리", [
            "사용자는 열람, 정정, 삭제, 처리 제한, 데이터 이동, 반대의 권리와 언제든지 장래를 향해 동의를 철회할 권리가 있습니다(설정 → 「개인정보 옵션」). 데이터 보호 감독 기관에 불만을 제기할 수도 있습니다. {EMAIL}로 연락해 주세요. 저희 서버에는 개인정보를 저장하지 않으므로, 대부분은 게임 삭제와 Google 설정으로 해결됩니다.",
        ]),
        ("10. 연령", [
            "Nailgoal은 13세 이상 일반 이용자를 위한 게임입니다. 13세 미만 어린이를 대상으로 하지 않습니다.",
        ]),
        ("11. 변경", [
            "게임이 바뀌는 경우 등에 이 방침을 업데이트할 수 있습니다. 최신 날짜는 상단에 표시됩니다.",
        ]),
    ],
    support_title="지원 – Nailgoal",
    support=[
        ("연락처", ["질문, 문제 또는 아이디어가 있으신가요? 이메일: {EMAIL}"]),
        ("자주 묻는 질문", [
            ["플레이 방법: 보드 어디에서든 뒤로 당겨 새총처럼 코인을 조준한 뒤 놓으세요. 메인 메뉴의 「?」 버튼에서 규칙을 볼 수 있습니다.",
             "광고 없이 플레이: 설정 → 「광고 없이 플레이」. 새 iPhone·iPad 또는 재설치 후에는 설정 → 「구매 복원」. Android에서는 구매가 자동으로 복원됩니다.",
             "광고 개인정보: 설정 → 「개인정보 옵션」(동의가 필요한 지역에서 표시).",
             "게임이 멈추거나 종료됨: 기기 모델과 그때 하던 일을 알려 주세요."],
        ]),
    ],
    legal_title="법적 고지",
    legal=[
        ("§ 5 DDG에 따른 정보", ["{NAME}", "{ADDRESS}"]),
        ("연락처", ["이메일: {EMAIL}"]),
    ],
)

# ---------------------------------------------------------------- العربية
LANGS["ar"] = dict(
    name="العربية", dir="rtl",
    nav=dict(home="الرئيسية", privacy="الخصوصية", support="الدعم", legal="بيانات الناشر"),
    updated_label="آخر تحديث",
    privacy_title="سياسة الخصوصية – Nailgoal",
    privacy=[
        ("1. المسؤول", [
            "ناشر لعبة «Nailgoal» والمسؤول عن البيانات الشخصية هو: {NAME}، {ADDRESS}. البريد الإلكتروني: {EMAIL}",
        ]),
        ("2. باختصار", [
            "لا تحتاج Nailgoal إلى حساب أو تسجيل، ولا نطلب أبدًا اسمك أو بريدك الإلكتروني أو رقم هاتفك. تبقى إعداداتك على جهازك. تستخدم اللعبة خدمة خارجية واحدة فقط: Google AdMob للإعلانات التي تظهر بعد بعض المباريات. في المنطقة الاقتصادية الأوروبية والمملكة المتحدة وسويسرا لا تُستخدم الإعلانات المخصصة إلا بموافقتك. إذا اشتريت «العب بدون إعلانات» فإن Apple أو Google تتولى عملية الدفع. لا تحتوي اللعبة على تحليلات أو تقارير أعطال خاصة بها.",
        ]),
        ("3. البيانات على جهازك", [
            "تُحفظ إعداداتك (اللغة، مستوى الصوت، الأرضية، نوع اللعب، أهداف الفوز)، وعدّاد المباريات منذ آخر إعلان، ومعلومة شرائك «العب بدون إعلانات» في التخزين المحلي للعبة على جهازك فقط. نحن لا نتلقى هذه البيانات. إذا حذفت اللعبة تُحذف هذه البيانات أيضًا.",
        ]),
        ("4. الإعلانات (Google AdMob)", [
            "بعد بعض المباريات تعرض اللعبة إعلانًا بملء الشاشة. لا توجد لافتات إعلانية ولا إعلانات أثناء اللعب. ولهذا الغرض قد تعالج حزمة Google Mobile Ads SDK (Google Ireland Limited / Google LLC) بيانات مثل عنوان IP ومعرّفات الجهاز (مثل المعرّف الإعلاني) ومعلومات الجهاز والتطبيق وتفاعلك مع الإعلان، وذلك لعرض الإعلانات وقياسها ومنع الاحتيال.",
            "في المنطقة الاقتصادية الأوروبية والمملكة المتحدة وسويسرا نطلب موافقتك أولًا (نموذج موافقة Google). يمكنك مراجعة اختيارك أو تغييره في أي وقت داخل اللعبة من الإعدادات ← «خيارات الخصوصية». يعتمد تخصيص الإعلانات على اختيارك وإعدادات جهازك. ويمكنك أيضًا إعادة تعيين المعرّف الإعلاني أو حذفه من إعدادات هاتفك.",
            "على iPhone وiPad قد تعرض اللعبة أيضًا طلب Apple «السماح بالتتبع» (App Tracking Transparency). إذا اخترت «طلب عدم التتبع من التطبيق» فلن يُستخدم معرّفك الإعلاني (IDFA) للإعلانات. يمكنك تغيير ذلك في أي وقت من إعدادات الجهاز: الخصوصية والأمن ← التتبع.",
            "للمزيد: سياسة خصوصية Google ({G1}) و«كيف تستخدم Google المعلومات من المواقع أو التطبيقات التي تستخدم خدماتها» ({G2}).",
        ]),
        ("5. المشتريات (العب بدون إعلانات)", [
            "يمكنك شراء «العب بدون إعلانات» مرة واحدة داخل اللعبة (الإعدادات ← «العب بدون إعلانات»). يزيل ذلك الإعلانات بعد المباريات نهائيًا. تتولى Apple (App Store) أو Google (Google Play) عملية الدفع بالكامل وفق شروطهما وسياسات الخصوصية الخاصة بهما. لا نتلقى اسمك أو بريدك الإلكتروني أو بيانات الدفع. يُبلغ المتجر اللعبة فقط ما إذا كنت تملك عملية الشراء، وتحفظ اللعبة ذلك على جهازك. على iPhone أو iPad جديد يمكنك استعادتها من الإعدادات ← «استعادة المشتريات»؛ وعلى Android تتم الاستعادة تلقائيًا.",
        ]),
        ("6. ما لا نفعله", [
            "لا ننشئ حسابات مستخدمين، ولا نبيع البيانات، ولا نجري تحليلات خاصة بنا، ولا نصل إلى موقعك أو جهات اتصالك أو صورك أو الكاميرا أو الميكروفون. إلى جانب الاتصال بالإنترنت، تستخدم اللعبة فقط خدمة الشراء في متجر التطبيقات، وعلى iPhone وiPad طلب Apple للتتبع من أجل الإعلانات. تعمل اللعبة نفسها دون اتصال، ويُستخدم الإنترنت فقط للإعلانات والمشتريات.",
        ]),
        ("7. الأسس القانونية (اللائحة العامة لحماية البيانات GDPR)", [
            ["الإعلانات في المنطقة الاقتصادية الأوروبية والمملكة المتحدة وسويسرا: موافقتك (المادة 6(1)(أ) من GDPR، والمادة 25(1) من TDDDG).",
             "في أماكن أخرى: مصلحتنا المشروعة في تمويل اللعبة المجانية بالإعلانات (المادة 6(1)(و) من GDPR).",
             "المشتريات: تنفيذ العقد (المادة 6(1)(ب) من GDPR).",
             "الرد على رسائلك: المادة 6(1)(و) من GDPR."],
        ]),
        ("8. النقل إلى دول ثالثة", [
            "قد تعالج Google البيانات خارج المنطقة الاقتصادية الأوروبية (بما في ذلك الولايات المتحدة) استنادًا إلى البنود التعاقدية القياسية للاتحاد الأوروبي أو إطار خصوصية البيانات بين الاتحاد الأوروبي والولايات المتحدة.",
        ]),
        ("9. حقوقك", [
            "لك الحق في الوصول والتصحيح والمحو وتقييد المعالجة ونقل البيانات والاعتراض، والحق في سحب موافقتك في أي وقت بأثر مستقبلي (الإعدادات ← «خيارات الخصوصية»). ويمكنك أيضًا تقديم شكوى إلى سلطة رقابية لحماية البيانات. راسلنا على {EMAIL}. ولأننا لا نخزّن أي بيانات شخصية على خوادمنا، تُحل معظم هذه الأمور بحذف اللعبة ومن خلال إعدادات Google.",
        ]),
        ("10. العمر", [
            "Nailgoal لعبة لجمهور عام بعمر 13 عامًا فأكثر، وهي غير موجّهة للأطفال دون 13 عامًا.",
        ]),
        ("11. التغييرات", [
            "قد نحدّث هذه السياسة، مثلًا عند تغيّر اللعبة. يظهر التاريخ الحالي في الأعلى.",
        ]),
    ],
    support_title="الدعم – Nailgoal",
    support=[
        ("التواصل", ["لديك سؤال أو مشكلة أو فكرة؟ راسلنا: {EMAIL}"]),
        ("الأسئلة الشائعة", [
            ["طريقة اللعب: اسحب للخلف من أي مكان على اللوحة لتصويب العملة كالمقلاع، ثم اترك. يشرح زر «؟» في القائمة الرئيسية القواعد.",
             "العب بدون إعلانات: الإعدادات ← «العب بدون إعلانات». على iPhone أو iPad جديد أو بعد إعادة التثبيت: الإعدادات ← «استعادة المشتريات». على Android تُستعاد عملية الشراء تلقائيًا.",
             "خصوصية الإعلانات: الإعدادات ← «خيارات الخصوصية» (تظهر حيث تكون الموافقة مطلوبة).",
             "توقفت اللعبة أو أُغلقت فجأة: راسلنا بطراز جهازك وما كنت تفعله."],
        ]),
    ],
    legal_title="بيانات الناشر",
    legal=[
        ("معلومات وفقًا للمادة 5 من DDG", ["{NAME}", "{ADDRESS}"]),
        ("التواصل", ["البريد الإلكتروني: {EMAIL}"]),
    ],
)
