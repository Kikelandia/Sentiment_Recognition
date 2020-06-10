Reconocimiento de emociones a traves de la expresión facial utilizando open CV y scikit Learn

Script Realizado durante el curso de MAchine Learning impartido por Datalab Community y
Centraal Academy de Enero a Mayo del 2020 en Guadalajara Jalisco México

El Desarrollo del modelo matemático fue realizado utilizando las siguientes bases de datos

FacesDB:
(2008) - VISGRAF - http://app.visgraf.impa.br/database/faces/

CK+48
(2000) - Kanade, T., Cohn, J. F., & Tian, -
http://www.jeffcohn.net/wp-content/uploads/2020/04/CK-AgreementForm.pdf

se incluyen los siguientes archivos:

haarcascade_frontalface_default
modelo_Reco_Facial_LogReg
modelo_Reco_Facial_LogReg_Over
Reco_Camara
Reco_Camara_Imagen
Reco_Camara_Video

Si ya cuenta con los conocimientos necesarios para crear ambientes virtuales o instalar paquetes
desde la terminal de python puede abrir el archivo "Reco_Camara" y verificar las librerias necesarias
para la correcta ejecución del archivo, en caso contrario a continuación se enlistan los pasos
recomendados:

1.- Descargar y descomprimir (en el escritorio *opcional) el archivo Proyecto_Final_1.0.zip
2.- Descargar e instalar python con el archivo exe que puede ancontrar en "https://www.python.org/downloads/"
3.- Descargar e instalar miniconda con el archivo exe que puede ancontrar en "https://docs.conda.io/en/latest/miniconda.html"
		MUY IMPORTANTE abilitar variables de entorno durante la instalación
			en el paso 3 o 4 de la instalación de miniconda el programa preguntará si desea habilitar las variables
			de entorno (path variables) es necesario aceptar la activación de dichas variables
4.- Una vez instalados los archivos anteriores abrir una terminal
		en windows abrir el símbolo del sistema (tecla windows y buscar cmd)
		en Lynux ctrl + alt + t
		Mac OS Finder->Aplicaciones->Utilidades->Terminal
5.- Crear un ambiente virtual con el comando
	conda create --name myEnv
6.- Activar el ambiente virtual con el comando
	conda activate myEnv (despues de esto deberá aparecer la leyenda (myEnv) al principio de la línea de comandos)
7.- Instalar openCV con el comando
	conda install -c conda-forge opencv
8.- Instalar scikit con el comando
	conda install scikit-learn=0.22.1
9.- Cambiar el directorio hacia el lugar donde fue descomprimido el archivo Proyecto_Final_1.0.zip
	Ejemplo: cd c:\Desktop\
10.- Ejecutar el archivo de reconocimiento de emociones con el comando
	python Reco_Camara.py
11.- Para finalizar la ejecución es forzoso presionar la tecla esc


El archivo Reco_Camara_Imagen sirve para encontrar rostros y evaluar su emoción con imagenes fijas
en archivos de tipo imagen (jpg, bmp, png) solo es necesario ejecutar el archivo usando como parametro
la imagen que se desea evaluar, ejemplo:
		python Reco_Camara_Imagen.py Imagen.jpg

El archivo Reco_Camara_Video sirve para encontrar rostros y evaluar su emoción en archivos
de tipo video (avi, mpg, etc) solo es necesario ejecutar el archivo usando como parametro
el video que se desea evaluar, ejemplo:
		python Reco_Camara_Video.py Video.avi