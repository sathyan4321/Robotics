# This is fully education purposed project.
# It is not intended for commercial use.
# Author : Sathya Narayanan.R
# Date of Creation : 05-10-2024
# Date of Last Modification : 05-10-2024
# Country : India
# Language : Python
# IDE : Thonny
# Github : https://github.com/sathyan4321



#### Moving Car ####

from machine import Pin, PWM
from time import sleep, time

# Define pins for motor driver (L298N)
# Motor A (left)
IN1 = Pin(0, Pin.OUT)
IN2 = Pin(1, Pin.OUT)

# Motor B (right)
IN3 = Pin(2, Pin.OUT)
IN4 = Pin(3, Pin.OUT)

# Define pins for Ultrasonic Sensor (HC-SR04)
TRIG = Pin(4, Pin.OUT)
ECHO = Pin(5, Pin.IN)

# Function to measure distance using the ultrasonic sensor
def measure_distance():
    # Send a 10µs pulse to TRIG
    TRIG.low()
    sleep(0.02)
    TRIG.high()
    sleep(0.00001)
    TRIG.low()
    
    # Measure the duration of the pulse on ECHO
    while ECHO.value() == 0:
        pulse_start = time()
    
    while ECHO.value() == 1:
        pulse_end = time()
    
    pulse_duration = pulse_end - pulse_start
    
    # Convert pulse duration to distance (in cm)
    distance = pulse_duration * 17150  # Speed of sound (343m/s), adjusted for cm and duration
    
    return distance

# Function to move the car forward
def move_forward():
    IN1.high()
    IN2.low()
    IN3.high()
    IN4.low()

# Function to move the car backward
def move_backward():
    IN1.low()
    IN2.high()
    IN3.low()
    IN4.high()

# Function to turn the car left
def turn_left():
    IN1.low()
    IN2.high()
    IN3.high()
    IN4.low()

# Function to turn the car right
def turn_right():
    IN1.high()
    IN2.low()
    IN3.low()
    IN4.high()

# Function to stop the car
def stop():
    IN1.low()
    IN2.low()
    IN3.low()
    IN4.low()

# Main loop
try:
    while True:
        distance = measure_distance()
        print("Distance:", distance, "cm")
        
        if distance > 20:  # If the distance to the obstacle is greater than 20cm
            move_forward()  # Keep moving forward
        else:
            stop()          # Stop when an obstacle is too close
            sleep(1)
            move_backward() # Move backward for a short time
            sleep(1)
            stop()
            sleep(1)
            
            # Randomly choose to turn left or right
            turn_left()     # Turn left or right to avoid obstacle
            sleep(1)
            stop()
            sleep(1)
            
except KeyboardInterrupt:
    stop()
