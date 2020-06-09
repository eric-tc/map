import os
# questo script crea un file txt con tutte le path delle immagini nella cartella Folder
# Le path servono a Yolo per trovare le detection

FOLDER= "/media/eric/dati/wildTrack/Wildtrack_dataset/Image_subsets/C5/"

files= os.listdir(FOLDER)

f= open("imagePaths.txt","w+")

for single_file in files:

    f.write("{}\n".format(FOLDER + single_file))