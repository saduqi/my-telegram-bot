from unittest.mock import call

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8846364154:AAFXzPBoGx8cW-FDpGaNPFGtrd_xLPYieL8"
bot = telebot.TeleBot(TOKEN)

# عند إرسال /start تظهر الأزرار
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # إنشاء القائمة
    markup = InlineKeyboardMarkup()
    markup.row_width = 2 # عدد الأزرار في الصف الواحد

    # إنشاء الأزرار (الاسم الظاهر، والبيانات المرجعية callback_data)
    btn_files = InlineKeyboardButton("📂 كل الملخصات ", callback_data="files")
    btn_schedule = InlineKeyboardButton("📅 جدول الفصل الأول ", callback_data="schedule")
    btn_website = InlineKeyboardButton("🌐 الموقع الرسمي للجامعة ", url="https://www.amu-ye.com/")    

    # إضافة الأزرار للوحة
    markup.add(btn_files, btn_schedule, btn_website)

    bot.send_message(message.chat.id, "مرحبا! اختر من القائمة التالية :", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    if call.data == "files":
        # فتح ملف الـ PDF وإرساله
        with open("Programming in Python language @ArabLibrary.pdf", "rb") as pdf_file:
            bot.send_document(call.message.chat.id, pdf_file, caption="📚 اختر تخصصك")

    elif call.data == "schedule":
        with open("photo_٢٠٢٦-٠٩-٠٥_٢١-٥٨-٣١.jpg", "rb") as photo_file:
            bot.send_photo(call.message.chat.id, photo_file)
            
    bot.answer_callback_query(call.id)

# تشغيل البوت
bot.polling()