import telebot
import os
from telebot import types
from keep_alive import keep_alive
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

# لێرە تۆکینی بۆتەکەت دابنێ
TOKEN = '8685827632:AAEVVqmbDHNps0YilijgQ8Qo87vB1MKce68'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎵 ڤیدیۆ بۆ MP3")
    btn2 = types.KeyboardButton("🖼️ تەنها گۆڕینی وێنە")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "سڵاو ڕێبەر گیان! یەکێک هەڵبژێرە:", reply_markup=markup)

# دەستپێکردنی سێرڤەری پاراستن
keep_alive()

# کارپێکردنی بۆت
bot.polling(none_stop=True)
