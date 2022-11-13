from datetime import datetime as dt
from time import time


def div_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("log.txt", "a") as file:
        file.write("{}, division, {}".format(time, data))


def sum_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("log.txt", "a") as file:
        file.write("{}, sum, {}".format(time, data))


def sub_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("log.txt", "a") as file:
        file.write("{}, subtraction, {}".format(time, data))


def mult_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("log.txt", "a") as file:
        file.write("{}, multiplication, {}".format(time, data))
