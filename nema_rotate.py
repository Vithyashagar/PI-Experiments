from time import sleep
import RPi.GPIO as GPIO

DIR = 20 #Direction GPIO pin
STEP = 21 #Step GPIO pin
CW = 1 #Clokwise rotation 
CCW = 0 #Counter clokwise rotation
SPR = 48 #Steps per revolution (360/7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.output(DIR, CW)
step_count = SPR
delay = .0208

def rotate(step_count = step_count):
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

rotate()
sleep(0.5)

GPIO.output(DIR, CCW)
rotate()

# Micro stepping
resolution = {"Full": (0,0,0),
              "Half": (1,0,0),
              "1/4":(0,1,0),
              "1/8":(1,1,0),
              "1/16":(0,0,1),
              "1/32":(1,0,1)}

