import telebot
from telebot import types
import model_div as m_div
import model_sub as m_sub
import model_sum as m_sum
import model_mult as m_mult

first_number = 0
second_number = 0
first_number_comp = 0
second_number_comp = 0
math_operation = ''

token = '5736586297:AAFYeKkaqyOe7FQAn2FbFP-bbZYYyoTXn1Y'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])

def first_fun(message):
    bot.send_message(message.chat.id, 'Выберите тип числа.')
    bot.register_next_step_handler(message,first)
    
def first(message):
    global first_number
    first_number = int(message.text)
    bot.send_message(message.chat.id, 'Введите второе число.')
    bot.register_next_step_handler(message,second)
    
def second(message):
    global second_number
    second_number = int(message.text)
    bot.send_message(message.chat.id, "Сумма")
    #m_sum(first_number,second_number,first_number_comp,second_number_comp,1)
bot.polling(non_stop=True)