import telebot
from pyexpat.errors import messages
from telebot import types
from telebot.apihelper import send_message

TOKEN = '7994175520:AAE3XjJJ0GSJtHZkllx02CsF9gkB2-ZQRkk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    catalog = types.KeyboardButton('Catalog')
    basket = types.KeyboardButton('Coș🛒')
    orders = types.KeyboardButton('Comenzi')
    feedback = types.KeyboardButton('Feedback')

    markup.add(catalog,basket,orders,feedback)

    send_message = "<b>Salut👋 </b>\nBine ai venit la magazinul nostru online"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == "Catalog":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        tshirt = types.KeyboardButton('Tricouri')
        jeans = types.KeyboardButton('Blugi')
        shoes = types.KeyboardButton('Incaltaminte')
        shirt = types.KeyboardButton('Camasi')
        suit = types.KeyboardButton('Costum')
        dress = types.KeyboardButton('Rochii')
        back = types.KeyboardButton('Inapoi')
        markup.add(tshirt,jeans,shoes,shirt,suit,dress,back)
        send_message="Minunat! Ce anume va intereseaza?"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    elif message.text == "Incaltaminte":
        markup = types.InlineKeyboardMarkup()
        unity = types.InlineKeyboardButton("Accesati", url="https://intertop.kz/brands/")
        markup.add(unity)
        send_message="Intreaga colectie o puteti vedea pe siteul nostru!"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    elif message.text =="Inapoi":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        catalog = types.KeyboardButton('Catalog')
        basket = types.KeyboardButton('Coș🛒')
        orders = types.KeyboardButton('Comenzi')
        feedback = types.KeyboardButton('Feedback')

        markup.add(catalog,basket,orders,feedback)

        send_message = "<b>Ce anume va intereseaza?</b>\n"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Nu huh: {e}")