from picamera import PiCamera
from time import sleep
from gpiozero import Button,LED
import datetime
button = Button(5)
camera = PiCamera()
led_red = LED(12)

#camera.start_preview()

frame = 1
filePath = "/home/pi/Desktop/timestamped_pics/"
while True:
    try:
        button.wait_for_press()
        # Grab the current time
        currentTime = datetime.datetime.now()
        # Create file name for our picture
        picTime = currentTime.strftime("%Y.%m.%d-%H%M%S")
        picName = picTime + '.jpg'
        completeFilePath = filePath + picName
        camera.start_preview()
        led_red.on()
        sleep(2)
        led_red.off()
        sleep(0.1)
        led_red.on()
        sleep(0.1)
        led_red.off()
        camera.annotate_text = picTime
        camera.capture(completeFilePath)
        camera.stop_preview()
        frame += 1
    except KeyboardInterrupt:
        break
# camera.stop_preview()