class Translation(object):
    START_TEXT = """Salom @YtDown_UzBot ga hush kelibsiz!

<b>Iltimos, menga yuklamoqchi bo'lgan faylingiz yoki videouingizni ssilkasini yuboring

Men Youtubedan videolarni telegramga yuklab beraman📥 istalgan formatda</b>

boshqa narsalar /help menyusida..

Support : @Anonym_Uzbek"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>😅This is Free Service. No Upgrade Plans 😜</b>\nPlease Subscribe to my channel if you me useful. <a href='https://t.me/iDevelopersUz'>Dasturchilar kanali</a>  Yordam uchun /help"
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "<b>trying to download📥 </b>"
    UPLOAD_START = "<b>trying to upload📥</b>"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Please Subscribe to my channel if you  me useful. Dasturchilar kanali: https://t.me/iDevelopersUz"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "{} Soniya ichida yuklab olindi. \ nFoydali bo'lsangiz, kanalimga obuna bo'ling. <a href='https://t.me/iDevelopersUz'>Dasturchilar kanali</a> \n
{} Soniya ichida yuklandi‌‌."
    NOT_AUTH_USER_TEXT = "Iltimos /upgrade bosing.."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Aniqlangan fayl hajmi: {}. Bepul foydalanuvchilar faqat yuklashlari mumkin: {} \niltimos /upgrade ni bosing. \nAgar bu xato deb o'ylasangiz, iltimos bog'laning‌‌ <a href='https://telegram.me/Anonym_Uzbek>@Anonym_Uzbek</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Shaxsiy video /file eskizi saqlandi. Ushbu rasm video /file da ishlatiladi‌‌"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Foydalanuvchi rasmlari muvaffaqiyatli o'chirildi.‌‌."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media muvofaqqiyatli tozalandi."
    SAVED_RECVD_DOC_FILE = "Hujjat muvofaqiyatli yuklandi😊."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Haqiqiy ThumbNail topilmadi‌‌."
    NO_VOID_FORMAT_FOUND = "{}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """
Joriy reja tafsilotlari
TO'LIQ BEPUL
Telegram identifikatori: <code> {} </code>
Reja nomi: Bepul foydalanuvchi
Aloqa: @Anonym_Uzbek‌‌"""
    HELP_USER = """Salom bu @YtDown_UzBot ..
    
1. URL manzilini yuboring (link | Kengaytmali yangi nom).
2. Shaxsiy eskizni yuboring (ixtiyoriy).
3. Tugmani tanlang.‌‌
   <b>SVideo</b> - Videoni skrinshotlari bilan olish
   <b>DFile</b>  - Faylni skrinshotlari bilan olish
   <b>Video</b>  - Videoni skrinshotsiz olish
   <b>DFile</b>  - Faylni scrinshotsiz olish

 ♨Batafsil ma'lumot -
👉<a href="https://t.me/YtdownUz">uchun Shu yerga bosing</a>

Joriy reja tafsilotlarini bilish uchun menga /me niyuboring‌‌

Support : @Anonym_Uzbek"""
    REPLY_TO_DOC_GET_LINK = "Yuqori tezlikda to'g'ridan-to'g'ri yuklab olish havolasini olish uchun Telegram media-ga javob bering‌‌"
    REPLY_TO_DOC_FOR_C2V = "O'zgartirish uchun Telegram media-ga javob bering‌‌"
    REPLY_TO_DOC_FOR_SCSS = "Skrinshotlarni olish uchun Telegram media-ga javob bering"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Xususiy eskiz qo'llab-quvvatlashi bilan Telegram media-ga javob berish /rename o'zgartirish"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n© @Anonym_Uzbek"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Qirqish uchun: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "Avval biron bir vositaga mening localga yuklab olish uchun uni yuklang /downloadmedia. \ nHozirda yuklab olingan mediani bilish uchun /storageinfo yuboring"
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video davomiyligi: {} \ nUshbu mediani saqlash joyimdan o'chirish uchun yuboring."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Saqlangan media allaqachon mavjud. Mavjud media tafsilotlarini bilish uchun iltimos, /storageinfo ni yuboring‌‌."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Ichki oqimlarni olish uchun Telegram media-ga (MKV) javob bering‌‌"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Shaxsiy rasmlarni yaratish uchun media albomga javob bering /generatecustomthumbnail‌‌ "
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Albomda faqat ikkita fotosurat bo'lishi kerak. Iltimos, media albomni qayta yuboring va yana urinib ko'ring yoki albomga faqat ikkita rasmni yuboring‌‌."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL formati noto‘g‘ri. URL manzilingiz http: // yoki https: // bilan boshlanganiga ishonch hosil qiling. Format havolasi | yordamida siz shaxsiy fayl nomini qo'yishingiz mumkin file_name.extension"
    ABUSIVE_USERS = "Ushbu botni ishlatishingizga ruxsat yo'q. Agar bu xato deb o'ylasangiz, ushbu cheklovni olib tashlash uchun /me ni bosing tekshiring.‌‌."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "iltimos meni kanalimg azo buling. <a href='https://t.me/iDevelopersUz'>Dasturchilar kanali</a>"
    EXTRACT_ZIP_INTRO_ONE = "Avval zip faylni yuboring, so'ngra faylga reply qilib /unzip buyrug'ini yuboring‌‌."
    EXTRACT_ZIP_INTRO_THREE = " Qabul qilingan faylni tahlil qilish. ⚠️ Bu biroz vaqt talab qilishi mumkin. Iltimos, sabr qiling. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Kechirasiz. Siqilgan faylni qayta ishlash paytida xatolar yuz berdi. Iltimos, hamma narsani yana ikki marta tekshiring va agar muammo takrorlanmasa, bu haqda xabar bering<a href='https://telegram.me/Anonym_Uzbek>@Anonym_Uzbek</a>"
    EXTRACT_ZIP_STEP_TWO = """
Quyidagi variantlardan yuklash uchun file_name tanlang.
Faylni olganingizdan so'ng, uni kichik rasmlarni qo'llab-quvvatlash bilan qayta nomlash
 uchun /rename buyruqdan foydalanishingiz mumkin‌‌."""
    CANCEL_STR = "Jarayon to'xtatildi"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Ishlov berib bo‘lmadi.
Bepul foydalanuvchilar 30 daqiqada atigi bitta so'rov.
/upgrade qiling yoki 1800 soniyadan keyin urinib ko'ring."""
    SLOW_URL_DECED = "URL juda sekin ko'rinadi. Siz mening uyimni aylantirganingiz uchun, men ushbu faylni yuklab olishga xayolim yo'q. Shu bilan birga, nega bunday qilmayapsiz: ==> https://shrtz.me/PtsVnf6 va menga tezkor URL manzilini oling, shunda men Telegram-ga yuklay olaman, boshqa foydalanuvchilar uchun sekinlashmasdan.‌‌."
