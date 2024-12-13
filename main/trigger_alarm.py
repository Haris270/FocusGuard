from gpiozero import Buzzer
from time import sleep


# Function to trigger the buzzer
def trigger_alarm():
    buzzer = Buzzer(18)  # Sets the GPIO pin 18 to the buzzer

    try:
        buzzer.on()  # turn on the buzzer
        sleep(0.5)
        buzzer.off()  # turn off the buzzer
        sleep(0.5)
    except Exception as e:
        print(f"Alerting System Halted. Error : {e}")


trigger_alarm()