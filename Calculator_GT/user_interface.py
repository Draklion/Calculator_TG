import telebot
from telebot import types
import model_div as m_div
import model_sub as m_sub
import model_sum as m_sum
import model_mult as m_mult
import log

first_number = 0
second_number = 0
first_number_comp = 0
second_number_comp = 0
math_operation = ''
type_number = ''

token = '5736586297:AAFYeKkaqyOe7FQAn2FbFP-bbZYYyoTXn1Y'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])

def start_func(message):
    bot.send_message(message.chat.id, 'Укажите рациональное или комплексное число:\nРациональное число: R\nКомплексное число: C\n')
    bot.register_next_step_handler(message,type_number_fun)
    
def type_number_fun(message):
    global type_number
    type_number = message.text
    if type_number == "R":
        bot.send_message(message.chat.id, 'Укажите математическую операцию:\nСложение: +\nВычитание: -\nУмножение: *\nДеление: /\nОстаток от деления: %')
    elif type_number == "C":
        bot.send_message(message.chat.id, 'Укажите математическую операцию:\nСложение: +\nВычитание: -\nУмножение: *\nДеление: /')
    bot.register_next_step_handler(message,math_operation_fun)
   
def math_operation_fun(message):    
    global math_operation
    math_operation = message.text
    bot.send_message(message.chat.id, 'Введите первое число.')
    bot.register_next_step_handler(message,first)
    
def first(message):
    global first_number
    first_number = int(message.text)
    bot.send_message(message.chat.id, 'Введите второе число.')
    bot.register_next_step_handler(message,second)
    
def second(message):
    global second_number
    second_number = int(message.text)
    if type_number=="R":
        calculations(message)
    elif type_number=="C":
            bot.send_message(message.chat.id, 'Введите третье число.')
            bot.register_next_step_handler(message,comp_FN)       

def comp_FN(message):
    global first_number_comp
    first_number_comp = int(message.text)
    bot.send_message(message.chat.id, 'Введите четвертое число.')
    bot.register_next_step_handler(message,comp_SN)

def comp_SN(message):
    global second_number_comp
    second_number_comp = int(message.text)
    calculations(message)

def calculations(message):
    if math_operation == "+":
        bot.send_message(message.chat.id, m_sum.Sum(first_number,second_number,first_number_comp,second_number_comp,type_number))
        log.sum_logger(f"{first_number},{second_number},{first_number_comp},{second_number_comp},{type_number}\n")
    elif math_operation == "-":
        bot.send_message(message.chat.id, m_sub.Subtraction(first_number,second_number,first_number_comp,second_number_comp,type_number))
        log.sub_logger(f"{first_number},{second_number},{first_number_comp},{second_number_comp},{type_number}\n")
    elif math_operation == "*":
        bot.send_message(message.chat.id, m_mult.Multiplication(first_number,second_number,first_number_comp,second_number_comp,type_number))
        log.mult_logger(f"{first_number},{second_number},{first_number_comp},{second_number_comp},{type_number}\n")
    elif math_operation == "/":
        bot.send_message(message.chat.id, m_div.Division(first_number,second_number,type_number))
        log.div_logger(f"{first_number},{second_number},{first_number_comp},{second_number_comp},{type_number}\n")
    elif math_operation == "%":
        bot.send_message(message.chat.id, m_div.Division_remain(first_number,second_number,type_number))
        log.div_logger(f"{first_number},{second_number},{first_number_comp},{second_number_comp},{type_number}\n")
    bot.send_message(message.chat.id, 'Вы закончили работу?(Да/Нет)')
    bot.register_next_step_handler(message,end)
    
def end(message):
    if message.text == "Да":
        bot.send_message(message.chat.id, 'Спасибо за проведенное со мной время.')
    elif message.text == "Нет":         
        start_func(message)    
       
bot.polling(non_stop=True)