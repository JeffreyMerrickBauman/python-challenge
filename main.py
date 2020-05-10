#PyPoll, main.py


#importing os and csv modules
import os
import csv

#update for Poll
csvpath = os.path.join('Resources', 'election_datas.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0

    for row in csvreader:
        #print(row)
        if row[2] == "Khan":
            Khan += Khan
        elif row[2] == "Correy":
            Correy += Correy
        elif row[2] == "Li":
            Li += Li
        elif row[2] == "O'Tooley":
            OTooley += OTooley
        
print(f"Khan: {Khan}")
print(f"Correy: {Correy}")
print(f"Li: {Li}")
print(f"O'Tooley: {OTooley}")

#Find Winner
#If statement series or way to use Max?

