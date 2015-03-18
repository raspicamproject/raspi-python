import requests
import time
import picamera

while True:
	with picamera.PiCamera() as camera, open("my_image.jpg", "wb+") as my_image:
		camera.capture(my_image)

	requests.post("http://149.91.83.88:3000/photos", files={'file': ("file.jpg", open("my_image.jpg", "rb"), "image/jpeg")})
	time.sleep(2)

