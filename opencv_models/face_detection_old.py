# https://towardsdatascience.com/https-medium-com-dilan-jay-face-detection-model-on-webcam-using-python-72b382699ee9
# https://github.com/DilanKalpa/FaceDetection

import cv2
import sys

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')

# Define a fonte de video para a webcam
video_capture = cv2.VideoCapture(0)

img_counter = 0

while True:
    # Leitura frame-a-frame
    ret, frame = video_capture.read()

    # A maioria das operações no OpenCV é feita em escala de cinza[1]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Capturar tecla pressionada
    k = cv2.waitKey(1)
    
    # Detectar rostos
    faces = faceCascade.detectMultiScale( # Função geral que detecta objetos
        gray, # Escala cinza
        scaleFactor=1.5, # Para rostos mais proximos a camera
        # janela movel para detectar objetos
        minNeighbors=50, # define quantos objetos são detectados perto do atual antes de declarar a face encontrada
        minSize=(30, 30), # o tamanho de cada janela
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Desenha os retangulos ao redor das faces
    # Retorna a localização e largura do retangulo (x, y) e a largura e altura do retângulo (w, h)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibir webcam
    cv2.imshow('FaceDetection', frame)

    # Teclas de controle:
    if k%256 == 27: #ESC Pressed
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "facedetect_webcam_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
