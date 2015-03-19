#Import les differentes biblioteques
import requests
import time
import picamera

#Boucle infinie, pour que le programme ne se termine jamais
while True:
	#Permet d'ouvrir une image en ecriture et en lecture
	with picamera.PiCamera() as camera, open("my_image.jpg", "wb+") as my_image:
		#Permet de capturer une photo
		camera.capture(my_image)
	#Permet d'envoyer via une requete post l'image- open(@ du serveur/ mode de lecture doit ouvert: permet d'ouvrir le fichier en  lecture et en ecritue  en binaire, buffering)
	requests.post("http://149.91.83.88:3000/photos", files={'file': ("file.jpg", open("my_image.jpg", "rb"), "image/jpeg")})
	time.sleep(2)

