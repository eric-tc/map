# Questo file crea i ground truth in formato txt partendo dal json
import json
import os



VIEW_NUMBER=5

files=os.listdir("/media/eric/dati/wildTrack/Wildtrack_dataset/annotations")



for filename in files:
    DR_PATH="/home/eric/Desktop/2020/mAP/WildTrack/data/"

    with open('/media/eric/dati/wildTrack/Wildtrack_dataset/annotations/{}'.format(filename)) as f:

        annotations=json.load(f)

        print(filename)
        #filename senza extensio
        filename_outext=os.path.splitext(filename)[0]

        print(filename_outext)
        outfile = open(os.path.join(DR_PATH, filename_outext + '.txt'), 'w+')

        


        for index,annotations in enumerate(annotations):
            #print(annotation)
            bbox=annotations["views"][5]
            #print(bbox["xmin"])

            outfile.write("{} {} {} {} {}\n".format("person",bbox["xmin"], bbox["ymin"], bbox["xmax"], bbox["ymax"]))
           
        
        
        outfile.close()
        #input("first")