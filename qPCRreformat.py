#A program to reformat the qPCR output back into a plate layout rather than just one long column. 
#Hopefully should make analysis much faster!
#Save your data elsewhere, the output file will be overwritten each time you run the program (unless you change the filename).

#Made by Andy Tuckey, Oct 2022
#NO Hugh I will NOT be adding PyPlot, DO NOT ask!!

#Change the input file here:
inputfile = "Desktop/20221018 kuf1 dlk2 qPCR 3.txt"

import csv

with open(inputfile, newline='\n') as f: #Opens the input file
    reader = csv.reader(f, delimiter = "\t") 
    outputfile = open("Desktop/Plate Layout.csv", "w") #Creates output file.
    counter = 0
    for a in list(reader): #'a' represents a row of the qPCR file. a[2] is the coordinate of the data point, a[4] is the Cp value we actually want.
        if((len(a)>3) and (counter > 1)): #Avoids crashing with the header lines.
            if(counter == 2): #Gotta define the initial row (i.e. A, B, C, etc.). Should be flexible with whatever layout you've got.
                currentLetter = a[2][0]
                outputfile.write(currentLetter+',')
                
            if(a[2][0] != currentLetter): #A new row is started if 'B' is reached for the first time.
                outputfile.write('\n'+a[2][0]+',')
                currentLetter = a[2][0]
                
            outputfile.write(a[4]+',')
            
        counter += 1
        
f.close()
outputfile.close()
