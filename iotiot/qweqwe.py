import RPi.GPIO as GPIO
import time

LED1_PIN = 23
LED2_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)


def led_on(led_pin):
    GPIO.output(led_pin, GPIO.HIGH)


def led_off(led_pin):
    GPIO.output(led_pin, GPIO.LOW)


def blink(led_pin, interval):
    led_on(led_pin)
    time.sleep(interval)
    led_off(led_pin)
    time.sleep(interval)


try:
    while True:
        command = input("Enter command (+, -, *, /): ")

        if command == '+':
            led_on(LED1_PIN)
            led_off(LED2_PIN)

        elif command == '-':
            led_off(LED1_PIN)
            led_on(LED2_PIN)

        elif command == '*':
            for _ in range(10):  # 10번 깜빡이기
                blink(LED1_PIN, 0.5)

        elif command == '/':
            for _ in range(10):  # 10번 깜빡이기
                blink(LED2_PIN, 0.5)

        else:
            print("Invalid command. Please enter +, -, *, or /.")

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    GPIO.cleanup()
