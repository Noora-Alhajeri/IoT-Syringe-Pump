from bottle import route, run, template, request, post, get
import threading, time, random
from threading import Timer
import schedule
import time
from os import system
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog

# from datetime import datetime
# import RPi.GPIO as GPIO
# from RpiMotorLib import RpiMotorLib
# import time
# Defining Pins
# direction = 22
# step = 23
# EN_pin = 24
# mymotorproject = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
# GPIO.setup(EN_pin, GPIO.OUT)
# GPIO.output(EN_pin, GPIO.OUT)
# GPIO.setmode(GPIO.BCM)


syringe = 0
dose = 0
dose_repeat = 0
dose_hours = 0


def Time1SecondsUp():
    global syringe
    global dose
    global dose_repeat
    global dose_hours
    print("1 second have passed")


def Time10SecondsUp():
    global syringe
    global dose
    global dose_repeat
    global dose_hours
    print("10 seconds have passed")


def Time60SecondsUp():
    global syringe
    global dose
    global dose_repeat
    global dose_hours
    print("60 seconds have passed")


def motorproject(n):
    # GPIO.setmode(GPIO.BCM)

    # GPIO.setup(EN_pin, GPIO.OUT)
    # GPIO.output(EN_pin, GPIO.OUT)

    # mymotorproject = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
    for i in range(n):
        # mymotorproject.motor_go(False, "Full", 200, 0.0005, False, 0.05)
        print("mymotorproject.motor_go(False, 200, 0.0005, False, 0.05)")
        time.sleep(1)

    time.sleep(10)
    print("10 seconds have passed")
    for j in range(n):
        # mymotorproject.motor_go(True, "Full", 200, 0.0005, False, 0.05)
        print("mymotorproject.motor_go(True, 200, 0.0005, False, 0.05)")
        time.sleep(1)


def motorproject1():
    # GPIO.setmode(GPIO.BCM)

    # GPIO.setup(EN_pin, GPIO.OUT)
    # GPIO.output(EN_pin, GPIO.OUT)

    # mymotorproject = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")

    for i in range(2):
        # mymotorproject.motor_go(False, "Full", 200, 0.0005, False, 0.05)
        print("mymotorproject.motor_go(False, 200, 0.0005, False, 0.05)")
        time.sleep(1)

    time.sleep(10)
    print("10 seconds have passed")
    for j in range(2):
        # mymotorproject.motor_go(True, "Full", 200, 0.0005, False, 0.05)
        print("mymotorproject.motor_go(True, 200, 0.0005, False, 0.05)")
        time.sleep(1)


def motorproject2():
    # GPIO.setmode(GPIO.BCM)

    # GPIO.setup(EN_pin, GPIO.OUT)
    # GPIO.output(EN_pin, GPIO.OUT)

    # mymotorproject = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
    for i in range(4):
        # mymotorproject.motor_go(False, "Full", 200, 0.0005, False, 0.05)
        print("mymotorproject.motor_go(False, 200, 0.0005, False, 0.05)")
        time.sleep(1)

    time.sleep(10)
    print("10 seconds have passed")
    for j in range(4):
        # mymotorproject.motor_go(True, "Full", 200, 0.0005, False, 0.05)
        print("mymotorproject.motor_go(True, 200, 0.0005, False, 0.05)")
        time.sleep(1)


def motorproject3():
    # GPIO.setmode(GPIO.BCM)

    # GPIO.setup(EN_pin, GPIO.OUT)
    # GPIO.output(EN_pin, GPIO.OUT)

    # mymotorproject = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
    for i in range(6):
        # mymotorproject.motor_go(False, "Full", 200, 0.0005, False, 0.05)
        print("mymotorproject.motor_go(False, 200, 0.0005, False, 0.05)")
        time.sleep(1)

    time.sleep(10)
    print("10 seconds have passed")
    for j in range(6):
        # mymotorproject.motor_go(True, "Full", 200, 0.0005, False, 0.05)
        print("mymotorproject.motor_go(True, 200, 0.0005, False, 0.05)")
        time.sleep(1)


def motorproject5():
    # GPIO.setmode(GPIO.BCM)

    # GPIO.setup(EN_pin, GPIO.OUT)
    # GPIO.output(EN_pin, GPIO.OUT)

    # mymotorproject = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
    for i in range(10):
        # mymotorproject.motor_go(False, "Full", 200, 0.0005, False, 0.05)
        print("mymotorproject.motor_go(False, 200, 0.0005, False, 0.05)")
        time.sleep(1)

    time.sleep(10)
    print("10 seconds have passed")
    for j in range(10):
        # mymotorproject.motor_go(True, "Full", 200, 0.0005, False, 0.05)
        print("mymotorproject.motor_go(True, 200, 0.0005, False, 0.05)")
        time.sleep(1)


def oneminute():
    time.sleep(60)


def twohours():
    time.sleep(7200)


def onehour():
    time.sleep(3600)


def fourhours():
    time.sleep(14400)


def eighthours():
    time.sleep(28800)


# def huda():
#    print("huda")

# for i in range(2):
#    huda()
#    Tk().after(10000, Time10SecondsUp())


@route('/Cancel')
def cancel():
    return template('Cancel.html')


@route('/')
def index():
    global syringe
    syringe = request.get("search")
    return template('Main.html', syringe=syringe)


@route('/Display', method='post')
def handle_data():
    global syringe
    global dose
    global dose_repeat
    global dose_hours
    syringe = request.forms.get('syringeValue')
    dose = request.forms.get('doseValue')
    dose_repeat = request.forms.get('doseRepeat')
    dose_hours = request.forms.get('doseHours')
    doseRemain = (int(syringe)) - (int(dose) * int(dose_repeat))
    remainingVolume = int(syringe) - int(dose)
    dosesAdministered = int(dose)*int(dose_repeat)

    # return template("Display.html", remainingVolume=remainingVolume, dose=dose)
    # remainingVolume = int(syringe) - int(dose)
    # This was under
    # global syringe
    # global dose
    # your code here

    # Dose 5 ml repeat 2 times
    if int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 10 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            oneminute()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)
    elif int(syringe) == 10 and int(dose) == 5:
        motorproject5()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))


    # Dose 5 ml repeat 3 times

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 5 ml repeat 4 times
    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 5 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)
    elif int(syringe) == 10 and int(dose) == 5:
        motorproject5()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))


    # Dose 1 ml, 10 ml syringe repeat 2 times

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)
    elif int(syringe) == 10 and int(dose) == 1:
        motorproject1()
        return template("Display.html", doseRemain=int(syringe)-int(dose), dosesAdministered=int(dose))


    # Dose 1 ml repeat 3 times

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 1 ml repeat 4 times
    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 1 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 2 ml, 10 ml syringe

    # Dose 2 ml, 10 ml syringe repeat 2 times

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)


    # Dose 2 ml repeat 3 times

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)


    # Dose 2 ml repeat 4 times

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 2 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)
    elif int(syringe) == 10 and int(dose) == 2:
        motorproject2()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))

    # Dose 3 ml, 10 ml syringe

    # Dose 3 ml, 10 ml syringe repeat 2 times

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 3 ml repeat 3 times

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 3 ml repeat 4 times

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 8 and int(dose_repeat) == 4:

        for i in range(4):
            motorproject3()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3:
        motorproject3()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))


    # Syringe 5 ml

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5:
        motorproject5()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))

    # Dose 5 ml repeat 3 times
    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 5 ml repeat 4 times
    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5:
        motorproject5()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))

    # Dose 1 ml, 5 ml syringe repeat 2 times
    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 1:
        motorproject1()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))

    # Dose 1 ml repeat 3 times
    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 1 ml repeat 4 times

    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 1 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 2 ml, 5 ml syringe
    # Dose 2 ml, 5 ml syringe repeat 2 times

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 2 ml repeat 3 times
    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 2 ml repeat 4 times

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 2 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 2:
        motorproject2()
        return template("Display.html",  doseRemain=int(syringe) - int(dose),dosesAdministered=int(dose))

    # Dose 3 ml, 5 ml syringe
    # Dose 3 ml, 5 ml syringe repeat 2 times

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 3 ml repeat 3 times

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 10 and int(dose) == 3 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 3 ml repeat 4 times

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 3 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 3:
        motorproject3()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))

    # Syringe 20 ml

    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject5()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 5:
        motorproject5()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))

    # Dose 5 ml repeat 3 times
    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject5()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)


    # Dose 5 ml repeat 4 times

    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 5 and int(dose) == 5 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 5 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject5()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 5:
        motorproject5()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))

    # Dose 1 ml, 20 ml syringe repeat 2 times
    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject1()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 1:
        motorproject1()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))

    # Dose 1 ml repeat 3 times

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject1()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 1 ml repeat 4 times

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 1 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject1()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 2 ml, 20 ml syringe

    # Dose 2 ml, 20 ml syringe repeat 2 times

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject2()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 2 ml repeat 3 times

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject2()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 2 ml repeat 4 times

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 2 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject2()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 2:
        motorproject2()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))


    # Dose 3 ml, 20 ml syringe
    # Dose 3 ml, 20 ml syringe repeat 2 times

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 1 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 2 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 4 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 8 and int(dose_repeat) == 2:
        for i in range(2):
            motorproject3()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 3 ml repeat 3 times

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 1 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 2 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 4 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            fourhours()
            continue

        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 8 and int(dose_repeat) == 3:
        for i in range(3):
            motorproject3()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    # Dose 3 ml repeat 4 times
    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 1 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            onehour()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 2 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            twohours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 4 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            fourhours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 3 and int(dose_hours) == 8 and int(dose_repeat) == 4:
        for i in range(4):
            motorproject3()
            eighthours()
            continue
        return template("Display.html", doseRemain=doseRemain, dosesAdministered=dosesAdministered)

    elif int(syringe) == 20 and int(dose) == 3:
        motorproject3()
        return template("Display.html", doseRemain=int(syringe) - int(dose), dosesAdministered=int(dose))

    else:
        print("This Value is not available")
        return template("Display.html", doseRemain="Value not available", dosesAdministered="Error!")


threading.Thread(target=run, kwargs=dict(host='localhost', port=8080)).start()

# GPIO.cleanup()


# @route('/Start')
# def start():
# print("Start() called")
# syringe = request.forms.get('SyringeValues')
# print(syringe)
# return template('Start.html')
# Code deleted from the display html
# <input name="Calculate" type="button" value="Calculate" onclick="calculateSyringe()"/>
# <input name="Calculate" type="button" value="Calculate" />
