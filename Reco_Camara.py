#Librerias necesarias
'''
Python version > 3.XX
Anaconda installed with path variables activated (miniconda can be installed too)
For the correct execution of the script create a new environment
install openCV using:
    conda install -c conda-forge opencv
    pip3 install opencv-python
install scikit learn version 0.22.1 to prevent any waring or malfunction
scikit=0.22.1
numpy could be any version however the one used was
    numpy=1.18.1
'''
import cv2
import numpy as np
import pickle

#XML para reconocimiento de rostros
#XML for facial recognition
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Archivo del modelo de reconocimiento de emociones
#Sentiment recognition model

#filename = 'modelo_Reco_Facial_LogReg.sav'
filename = 'modelo_Reco_Facial_LogReg_Over.sav'

#Instancia del Modelo
#Model Instance
loaded_model = pickle.load(open(filename, 'rb'))
#Contador de Fotogramas
#Framse counter
count = 0
#Lista con la emoción respectiva a cada rostro en la imagen (Hasta 10)
#Loist with the respective emotion for each face(Up to 10)
emotions = [''] * 10
#Se activa la cámara con OpenCV
#Camera is oppened
cap = cv2.VideoCapture(0)

#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#out = cv2.VideoWriter('output.avi', fourcc, 15.0, (640,480))

while True:
    #Función read() retorna boolean e imagen como np.array()
    #read() function return boolean and image as np.array()
    ret, img = cap.read()
    #La imagen es convertida a escala de grises
    #Image converted into gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Se detectan las caras en la imagen
    #Face detection in the image
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    #Recorrido y enumeración de cada uno de los rostros en la imagen
    #tambien son retornadas las coordenadas de cada cara
    #Traverse and enumerate each face in the image
    #face coordenates are returned too
    for idx, (x,y,w,h) in enumerate(faces):
        #Se crea en la imagen un rectangulo delimitando el rostro que fue encontrado
        #A Rectangle is printed in the imagen marking the found face off
        cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
        #Se aisla el rostro en la imagen en escala de grises para trabajar con él
        #Face gets isolated and turned to gray scale
        roi_gray = gray[y:y+h,x:x+w]
        #Dimensiones que escalar el rostro a evaluar
        #Dimensions to scalate the face to evaluate
        dim = (48,48)
        #Redimensión y "aplanamiento" de la np.array() (matriz(48,48)->vector(2304))
        #Resize and flattening of the array from matriz(48,48)->vector(2304)
        res = cv2.resize(roi_gray,dim).flatten()
        #Tipo de fuente para mostrar la emoción en pantalla
        #Font to show in screen
        font = cv2.FONT_HERSHEY_SIMPLEX
        #Para aligerar la carga en el procesador se evalua la emoción cada 10 fotogramas
        #Emotion will be evaluated each 10 frames to lighten the procesing load up
        if count%10==0:
            #Con el vector de 2304 dimensiones se realiza la predicción con la instancia del modelo
            #With the vector of 2304 dimension the prediction is done with the model
            emotions[idx] = loaded_model.predict([res])[0]
        #Se imprime en la imagen original la emoción correspondiente para cada rostro
        #The predicted emotion is printed in the original image for each face
        cv2.putText(img,emotions[idx],(x, y+h),font, 1,(0, 255, 255),2,cv2.LINE_4)
    #Imagen resultante, incluyendo el rectangulo que delimita al rostro y la emoción predicha
    #Final image, including the rectangle markinf the face up and the predicted emotion
    cv2.imshow('Prediccion Tiempo Real',img)
    #Contador de fotogramas incrementa en 1
    #Frame counter plus 1
    count +=1
    #out.write(img)
    #Se registra la tecla ESC para finalizar el programa
    #Esc key get registered to end up the program
    k = cv2.waitKey(30 & 0xff)
    if k == 27:
        break
#Liberación de la camara y recursos usados
#Camera and resourses released
cap.release()
#out.release()
cv2.destroyAllWindows()

#Para guardar el video en discon simplemente descomentar las líneas 40,41,89,98
#To save video in disk simply uncomment lines 40,41,89,98
