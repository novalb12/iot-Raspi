#from gpiozero import Servo
import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#servo1 = Servo(2)
#servo2 = Servo(3)
#servo3 = Servo(4)
pilih_servo= "sada"
pilih_btn=""
servo1= "ini kesatu"
servo2 = 3534
servo3 = "ini ketiga"
bot_token="734540315:AAGuZ0Qt9d6qzd0x3iA8ZVWcG1Vhw-Nb9xA"
bot=telebot.TeleBot(token=bot_token)
markup_servo = types.ReplyKeyboardMarkup()
markup_data = types.ReplyKeyboardMarkup()
arr_btn = ['-0.5','-0.4','-0.3','-0.2','-0.1','0.0','0.1','0.2','0.3','0.4','0.5']
arr_servo =['servo1','servo2','servo3']
btn_1 = types.KeyboardButton('/-0.5')
btn_2 = types.KeyboardButton('/-0.4')
btn_3 = types.KeyboardButton('/-0.3')
btn_4 = types.KeyboardButton('/-0.2')
btn_5 = types.KeyboardButton('/-0.1')
btn_6 = types.KeyboardButton('/0.0')
btn_7 = types.KeyboardButton('/0.1')
btn_8 = types.KeyboardButton('/0.2')
btn_9 = types.KeyboardButton('/0.3')
btn_10 = types.KeyboardButton('/0.4')
btn_11 = types.KeyboardButton('/0.5')
btn_ser1 = types.KeyboardButton('/servo1')
btn_ser2 = types.KeyboardButton('/servo2')
btn_ser3 = types.KeyboardButton('/servo3')
markup_servo.row(btn_ser1,btn_ser2,btn_ser3)
markup_data.row(btn_1,btn_2,btn_3,btn_4,btn_5)
markup_data.row(btn_6)
markup_data.row(btn_7,btn_8,btn_9,btn_10,btn_11)
print("bot udh mulai")
@bot.message_handler(commands=arr_btn)
def btn_handler(message):
	global pilih_btn
	pilih_btn = message.text[1:]
	send_servo(pilih_servo,pilih_btn)
	bot.send_message(message.chat.id, "Servo sudah bergerak")
	bot.send_message(message.chat.id, "ketik apa saja untuk mengulang")
@bot.message_handler(commands=arr_servo)
def servo_handler(message):
	temp=message.text[1:]
	global pilih_servo
	if temp == "servo1":
		print("nais1")
		pilih_servo=servo1
	elif temp == "servo2":
		print("nais2")
		pilih_servo=servo2
	elif temp == "servo3":
		print("nais3")
		pilih_servo=servo3
	bot.send_message(message.chat.id, ("Kamu memilih "+temp))
	bot.send_message(message.chat.id, "pilih posisi Servo",reply_markup=markup_data)
@bot.message_handler(func=lambda message: True)
def message_handler(message):
    print(type(message.text))
    bot.send_message(message.chat.id, "Pilih Servo :",reply_markup=markup_servo)

def send_servo(servo,pos):
	print("ini send servo")
	print(servo)
	print(pos)
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
