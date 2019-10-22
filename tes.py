from gpiozero import Servo
import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
servo1 = Servo(2)
servo2 = Servo(3)
servo3 = Servo(4)
bot_token="734540315:AAGuZ0Qt9d6qzd0x3iA8ZVWcG1Vhw-Nb9xA"
bot=telebot.TeleBot(token=bot_token)
markup = types.ReplyKeyboardMarkup()
btn_1 = types.KeyboardButton('-0.5')
btn_2 = types.KeyboardButton('-0.4')
btn_3 = types.KeyboardButton('-0.3')
btn_4 = types.KeyboardButton('-0.2')
btn_5 = types.KeyboardButton('-0.1')
btn_6 = types.KeyboardButton('0.0')
btn_7 = types.KeyboardButton('0.1')
btn_8 = types.KeyboardButton('0.2')
btn_9 = types.KeyboardButton('0.3')
btn_10 = types.KeyboardButton('0.4')
btn_11 = types.KeyboardButton('0.5')
btn_ser1 = types.KeyboardButton('Servo1')
btn_ser2 = types.KeyboardButton('Servo2')
btn_ser3 = types.KeyboardButton('Servo3')
btnOff = types.KeyboardButton('/lightoff')

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Servo1", callback_data="cb_servo1"),
               InlineKeyboardButton("Servo2", callback_data="cb_servo2"),
               InlineKeyboardButton("Servo3", callback_data="cb_servo3"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_servo1":
        print(call)
        bot.send_message(call.message.message_id," suda")
def set_servo1(pesan):
    bot.send_message(pesan.chat.id," suda")
@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())
#@bot.message_handler(commands=['lighton'])
#def light_on(message):
#    led.on();
#    bot.reply_to(message,"Light ON")
#    bot.get_webhook_info()
#@bot.message_handler(commands=['lightoff'])
#def light_off(message):
#    led.off();
#    bot.reply_to(message,'Light Off')
#    bot.get_webhook_info()
#@bot.message_handler(commands=['help'])
#def send_help(message):
#    bot.send_message(message.chat.id,"The Command on this Bot",reply_markup=markup)
#    bot.get_webhook_info()
#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#    bot.reply_to(message,"This message is not supported,type /help for more info")
#    bot.get_webhook_info()
bot.polling(none_stop=True)
