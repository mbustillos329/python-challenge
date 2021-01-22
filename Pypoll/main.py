import os
import csv
csvpath = os.path.join("PyPoll", "Resources","election_data.csv")

voterid = []
county = []
candidate = []
khan = 0
correy = 0
li = 0 
otooley = 0
percentage = []

with open(csvpath,"r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        voterid.append(row[0])

        if row[2] == "Khan":
            khan = khan + 1
        if row[2] == "Correy":
            correy = correy + 1
        if row[2] == "Li":
            li = li + 1
        if row[2] == "O'Tooley":
            otooley = otooley + 1

    
    #The total number of votes cast
    totvotes = len(voterid)

    #percentages
    pkhan = str(round(100*(khan/totvotes),3)) + "%"
    pcorrey = str(round(100*(correy/totvotes),3)) + "%"
    pli= str(round(100*(li/totvotes),3)) + "%"
    potooley = str(round(100*(otooley/totvotes),3)) + "%"

# printed output
print("Election Results", file=open("pypoll.txt", "a"))
print("--------------------", file=open("pypoll.txt", "a"))
print("Total Votes: " + str(totvotes), file=open("pypoll.txt", "a"))
print("--------------------", file=open("pypoll.txt", "a"))
print("Khan: " + pkhan + " "+ str(khan), file=open("pypoll.txt", "a"))
print("Correy: " + pcorrey + " "+ str(correy), file=open("pypoll.txt", "a"))
print("Li: " + pli + " "+ str(li), file=open("pypoll.txt", "a"))
print("O'Tooley: " + potooley + " "+ str(otooley), file=open("pypoll.txt", "a"))
print("--------------------", file=open("pypoll.txt", "a"))
print("Winner: Khan", file=open("pypoll.txt", "a"))
print('--------------------', file=open("pypoll.txt", "a"))

