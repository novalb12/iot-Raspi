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
markup_servo = types.ReplyKeyboardMarkup()
markup_data = types.ReplyKeyboardMarkup()
arr_btn = ['-0.5','-0.4','-0.3','-0.2','-0.1','0','0.1','0.2','0.3','0.4','0.5']
arr_servo =['Servo1','Servo2','Servo3']
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
markup_servo.row(btn_ser1,btn_ser2,btn_ser3)
markup_data.row(btn_1,btn_2,btn_3,btn_4,btn_5)
markup_data.row(btn_6)
markup_data.row(btn_7,btn_8,btn_9,btn_10,btn_11)

@bot.message_handler(commands=arr_servo)
def message_handler(message):
    bot.send_message(message.chat.id, message.text)
@bot.message_handler(commands=arr_btn)
def message_handler(message):
    bot.send_message(message.chat.id, message.text)
@bot.message_handler(func=lambda message: True)
def message_handler(message):
    print(type(message.text))
    bot.send_message(message.chat.id, "Pilih Servo :",reply_markup=markup_servo)

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
