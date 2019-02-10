import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# PIN セットアップ

S1  = 26
S2  = 19
S3  = 13
S4  = 6
S5  = 5
S6  = 21

S7  = 23
S8  = 18
S9  = 22
S10 = 27
S11 = 17
S12 = 4

GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)
GPIO.setup(S4, GPIO.OUT)
GPIO.setup(S5, GPIO.OUT)
GPIO.setup(S6, GPIO.OUT)
GPIO.setup(S7, GPIO.OUT)
GPIO.setup(S8, GPIO.OUT)
GPIO.setup(S9, GPIO.OUT)
GPIO.setup(S10, GPIO.OUT)
GPIO.setup(S11, GPIO.OUT)
GPIO.setup(S12, GPIO.OUT)

D1 = S12
D2 = S9
D3 = S8
D4 = S6

LA = S11
LB = S7
LC = S4
LD = S2
LE = S1
LF = S10
LG = S5
DP = S3

def reset():
    GPIO.output(D1, GPIO.HIGH)
    GPIO.output(D2, GPIO.HIGH)
    GPIO.output(D3, GPIO.HIGH)
    GPIO.output(D4, GPIO.HIGH)
    GPIO.output(LA, GPIO.LOW)
    GPIO.output(LB, GPIO.LOW)
    GPIO.output(LC, GPIO.LOW)
    GPIO.output(LD, GPIO.LOW)
    GPIO.output(LE, GPIO.LOW)
    GPIO.output(LF, GPIO.LOW)
    GPIO.output(LG, GPIO.LOW)
    GPIO.output(DP, GPIO.LOW)

def enableDigit(digit):
    if digit == 1:
        GPIO.output(D1, GPIO.LOW)
    elif digit == 2:
        GPIO.output(D2, GPIO.LOW)
    elif digit == 3:
        GPIO.output(D3, GPIO.LOW)
    elif digit == 4:
        GPIO.output(D4, GPIO.LOW)

def selectNumber(num):
    num = num % 10;
    if num == 0:
        GPIO.output(LA, GPIO.HIGH)
        GPIO.output(LB, GPIO.HIGH)
        GPIO.output(LC, GPIO.HIGH)
        GPIO.output(LD, GPIO.HIGH)
        GPIO.output(LE, GPIO.HIGH)
        GPIO.output(LF, GPIO.HIGH)
        GPIO.output(LG, GPIO.LOW)
    elif num == 1:
        GPIO.output(LA, GPIO.LOW)
        GPIO.output(LB, GPIO.HIGH)
        GPIO.output(LC, GPIO.HIGH)
        GPIO.output(LD, GPIO.LOW)
        GPIO.output(LE, GPIO.LOW)
        GPIO.output(LF, GPIO.LOW)
        GPIO.output(LG, GPIO.LOW)
    elif num == 2:
        GPIO.output(LA, GPIO.HIGH)
        GPIO.output(LB, GPIO.HIGH)
        GPIO.output(LC, GPIO.LOW)
        GPIO.output(LD, GPIO.HIGH)
        GPIO.output(LE, GPIO.HIGH)
        GPIO.output(LF, GPIO.LOW)
        GPIO.output(LG, GPIO.HIGH)
    elif num == 3:
        GPIO.output(LA, GPIO.HIGH)
        GPIO.output(LB, GPIO.HIGH)
        GPIO.output(LC, GPIO.HIGH)
        GPIO.output(LD, GPIO.HIGH)
        GPIO.output(LE, GPIO.LOW)
        GPIO.output(LF, GPIO.LOW)
        GPIO.output(LG, GPIO.HIGH)
    elif num == 4:
        GPIO.output(LA, GPIO.LOW)
        GPIO.output(LB, GPIO.HIGH)
        GPIO.output(LC, GPIO.HIGH)
        GPIO.output(LD, GPIO.LOW)
        GPIO.output(LE, GPIO.LOW)
        GPIO.output(LF, GPIO.HIGH)
        GPIO.output(LG, GPIO.HIGH)
    elif num == 5:
        GPIO.output(LA, GPIO.HIGH)
        GPIO.output(LB, GPIO.LOW)
        GPIO.output(LC, GPIO.HIGH)
        GPIO.output(LD, GPIO.HIGH)
        GPIO.output(LE, GPIO.LOW)
        GPIO.output(LF, GPIO.HIGH)
        GPIO.output(LG, GPIO.HIGH)
    elif num == 6:
        GPIO.output(LA, GPIO.LOW)
        GPIO.output(LB, GPIO.LOW)
        GPIO.output(LC, GPIO.HIGH)
        GPIO.output(LD, GPIO.HIGH)
        GPIO.output(LE, GPIO.HIGH)
        GPIO.output(LF, GPIO.HIGH)
        GPIO.output(LG, GPIO.HIGH)
    elif num == 7:
        GPIO.output(LA, GPIO.HIGH)
        GPIO.output(LB, GPIO.HIGH)
        GPIO.output(LC, GPIO.HIGH)
        GPIO.output(LD, GPIO.LOW)
        GPIO.output(LE, GPIO.LOW)
        GPIO.output(LF, GPIO.LOW)
        GPIO.output(LG, GPIO.LOW)
    elif num == 8:
        GPIO.output(LA, GPIO.HIGH)
        GPIO.output(LB, GPIO.HIGH)
        GPIO.output(LC, GPIO.HIGH)
        GPIO.output(LD, GPIO.HIGH)
        GPIO.output(LE, GPIO.HIGH)
        GPIO.output(LF, GPIO.HIGH)
        GPIO.output(LG, GPIO.HIGH)
    elif num == 9:
        GPIO.output(LA, GPIO.HIGH)
        GPIO.output(LB, GPIO.HIGH)
        GPIO.output(LC, GPIO.HIGH)
        GPIO.output(LD, GPIO.LOW)
        GPIO.output(LE, GPIO.LOW)
        GPIO.output(LF, GPIO.HIGH)
        GPIO.output(LG, GPIO.HIGH)

def selectDot():
    GPIO.output(DP, GPIO.HIGH)

def selectMinus():
    GPIO.output(LA, GPIO.LOW)
    GPIO.output(LB, GPIO.LOW)
    GPIO.output(LC, GPIO.LOW)
    GPIO.output(LD, GPIO.LOW)
    GPIO.output(LE, GPIO.LOW)
    GPIO.output(LF, GPIO.LOW)
    GPIO.output(LG, GPIO.HIGH)

INTERVAL = 0.001

def showInt(i):
    if i == 0:
        reset()
        enableDigit(4)
        selectNumber(0)
        time.sleep(INTERVAL * 4)
    elif i > 0:
        if i >= 1000:
            reset()
            enableDigit(1)
            selectNumber(i // 1000)
            time.sleep(INTERVAL)
        if i >= 100:
            reset()
            enableDigit(2)
            selectNumber(i // 100)
        time.sleep(INTERVAL)
        if i >= 10:
            reset()
            enableDigit(3)
            selectNumber(i // 10)
        time.sleep(INTERVAL)
        if i >= 1:
            reset()
            enableDigit(4)
            selectNumber(i)
        time.sleep(INTERVAL)
    elif i < 0:
        i = -i
        if i >= 100:
            reset()
            enableDigit(1)
            selectMinus()
            time.sleep(INTERVAL)
            reset()
            enableDigit(2)
            selectNumber(i // 100)
            time.sleep(INTERVAL)
            reset()
            enableDigit(3)
            selectNumber(i // 10)
            time.sleep(INTERVAL)
            reset()
            enableDigit(4)
            selectNumber(i)
            time.sleep(INTERVAL)
        elif i >= 10:
            reset()
            time.sleep(INTERVAL)
            reset()
            enableDigit(2)
            selectMinus()
            time.sleep(INTERVAL)
            reset()
            enableDigit(3)
            selectNumber(i // 10)
            time.sleep(INTERVAL)
            reset()
            enableDigit(4)
            selectNumber(i)
            time.sleep(INTERVAL)
        elif i >= 1:
            reset()
            time.sleep(INTERVAL * 2)
            reset()
            enableDigit(3)
            selectMinus()
            time.sleep(INTERVAL)
            reset()
            enableDigit(4)
            selectNumber(i)
            time.sleep(INTERVAL)

# main 処理
cnt = -999
WAIT_COUNT = 10

try:
    while True:
        for i in range(WAIT_COUNT):
            showInt(cnt)
        cnt += 1;
finally:
    GPIO.cleanup()

