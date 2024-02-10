#importar librerias
import cv2
import time
import numpy as np

#para guardar el output en un archivo output.avi
fourcc = cv2.videowrite_forcc(*'XXVID')
output_file = cv2.videowrite('output.avi', fourcc, 20.0, (640,480))

#iniciar la camara web
cap = cv2.videocapture(0)

#permitir a la camara web iniciar a cierto el codigo dormir o esperar por dos segundos
time.sleep(2)
bg = 0

#capturar el fondo por 60 cuadros
for i in range(60):
	ret, bg = cap.read()
#voltear el fondo
pg = np.flip(bg,axis=1)

#leer el cuadro capturado hasta que la camara este abierta
while(cap.isopened()):
	ret,img = cap.read()
	if not ret:
		break
	#voltear la imagen para que haya concordancia
	img = np.flip(img,axis=1)

	#convertir el color de bgr a hsv
	hsv=cv2.cvtcolor(img, cv2.COLOR_BGR2HSV)

	#general y la mascara para detectar el color rojo(los valores se pueden cambiar)
	lower_red=np.array([0,120,50])
	upper_ret = np_array([10,255,255])
	mask_1 = cv2.inrange(hsv,lower_ret,upper_ret)
cap.release()
out.release()
cv2.destroyAllWindows()
