from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)


LED = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

@app.route("/")
def helloworld():
    return "Hello world"

@app.route("/led/<state>")
def led(state):
    if state == "on":
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
    return "LED "+state

@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEANUP"
    
if __name__ == "__main__":
    app.run(debug = True, port = 8080, host='0.0.0.0')