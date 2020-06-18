Sentiment Recognition through facial expression using openCV and Scikit Learn

Script developed during the Machine Learning course, imparted by Datalab Community and
Centraal Academy from January to May 2020 in Guadalajara Jalisco Mexico

Script to predict basic human emotions: Neutral, Happy, Sad, Surprise, Anger

The Mathematical model was made using the next Datasets

FacesDB:
(2008) - VISGRAF - http://app.visgraf.impa.br/database/faces/

CK+48
(2000) - Kanade, T., Cohn, J. F., & Tian, -
http://www.jeffcohn.net/wp-content/uploads/2020/04/CK-AgreementForm.pdf

The next files are included:

haarcascade_frontalface_default.xml
modelo_Reco_Facial_LogReg.sav
modelo_Reco_Facial_LogReg_Over.sav
Reco_Camara.py
Reco_Camara_Imagen.py
Reco_Camara_Video.py

If you already have knowledge on how to create virtual environments and install packages from the
terminal you can open the "Reco_Camara.py" file y just confirm the needed libraries for the correct
execution of this script, otherwise the recommended steps are listed:

01.- Download and extract (in the desktop *optional) the file Sentiment_Recognition.zip
02.- Download and install python 3.xx with the file you can find in "https://www.python.org/downloads/"
03.- Download and install miniconda with the file you can find in "https://docs.conda.io/en/latest/miniconda.html"
		VERY IMPORTANT during the installation enable environment variables
			in the step three or four of the installation the wizard will ask if you want to enable such variables
			it is needed to activate them
04.- Once the installations are done open a terminal
		Windows: search for the cmd
		Lynuc ctrl + alt + t
		Mac OS Finder->Aplicaciones->Utilidades->Terminal
05.- Create a virtual environment with command
	conda create --name myEnv
06.- Activate the virtual environment with command
	conda activate myEnv (after this the legend (myEnv) must be shown at the beginnig of the command line)
07.- Install openCV with comand
	Windows / Linux
		conda install -c conda-forge opencv
	MAC OS
		pip3 install opencv-python
08.- Install scikit con el comando
	Windows / Linux
		conda install scikit-learn=0.22.1
	MAC OS
		pip3 install scikit-learn
09.- Change the directory to the folder where the file Sentiment_Recognition.zip was decompresed
	Example:
		cd c:\Desktop\Sentiment_Recognition\
		cd c:\Downloads\Sentiment_Recognition\
10.- Execute the facial recognition using the command
	Windows / Linux
		python Reco_Camara.py
	MAC OS
		python3 Reco_Camara.py
11.- To terminate the execution simply press ESC

After the first time executing the file you just need to repeat the steps
4, 6, 9, 10 y 11

The file Reco_Camara_Imagen.py can be used to find faces and evaluate the emotion in static images
in image type files (jpg, bmp, png, etc) it is just needed to execute the file using the image file as
parameter, example:
		python Reco_Camara_Imagen.py Imagen.jpg

The file Reco_Camara_Video.py can be used to find faces and evaluate the emotion in video type files
(avi, mpg, etc) it is just needed to execute the file using the video file as parameter, example:
		python Reco_Camara_Video.py Video.avi