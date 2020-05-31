# CoronaASA
All the raw data for the project can be found in the ASA Raw Data.pdf file. This file contains the raw data from our study in a document format. All of the data is stored in arrays and each entry corresponds with a word in 200CoronaWords.txt.

200CoronaWords.txt is a text file that contains the 200 keywords we tested in alphabetical order. This needs to be stored
locally on one's computer if they wish to run 200_Word_Tester_CoronaTime.ipynb.

200_Word_Tester_CoronaTime.ipynb is a program written in Jupyter Notebook. This program calculates and stores the MSE values 
for the 200 keywords in 200CoronaWords.txt

CoronaKeywordData.csv holds the MSE and other data for each keyword that we found in 200_Word_Tester_CoronaTime.ipynb.

CoronaSimData.m is a MATLAB file that analyzes the simulate data produced in RandomSim.py. The MATLAB program calculates the
minimum and maximum of the data, as well as the probability distribution. 

CoronaTime.ipynb is a program written in Jupyter Notebook that produces the keyword search trend map. The map details the
change in search trends for a certain keyword. In order to run the program, all the files in the folder "Map Files"
must be downloaded and stored locally on one's computer.

Expected.py is a Python program that calculates the expected MSE value for a theoretically random keyword with zero
association with the spread of COVID-19. The program calculates a nested sum and outputs a value of 416.5.

RandomSim.py is the Python program that simulated 1 million trials of the theoretically random keyword. It stores the 
1 million MSE values in a file named "ValRange". This data was used in CoronaSimData.m.




