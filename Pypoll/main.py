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

    pkhan = str(round(100*(khan/totvotes),3)) + "%"
    pcorrey = str(round(100*(correy/totvotes),3)) + "%"
    pli= str(round(100*(li/totvotes),3)) + "%"
    potooley = str(round(100*(otooley/totvotes),3)) + "%"


print("Election Results")
print("--------------------")
print("Total Votes: " + str(totvotes))
print("--------------------")
print("Khan: " + pkhan + " "+ str(khan))
print("Correy: " + pcorrey + " "+ str(correy))
print("Li: " + pli + " "+ str(li))
print("O'Tooley: " + potooley + " "+ str(otooley))
print("--------------------")
print("Winner: ")
print('--------------------')



        
