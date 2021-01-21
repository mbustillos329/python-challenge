#  
import os
import csv
csvpath = os.path.join("PyBank", "Resources","budget_data.csv")

# list for profits and losses
pl= []
plc = []

with open(csvpath,"r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
   
    # count for months
    count = 0
    # skip header
    header = next(csvreader)

    # loop
    for row in csvreader:
        # The total number of months included in the dataset
        count = count + 1
        # The net total amount of "Profit/Losses" over the entire period
        pl.append(int(row[1]))

        # Calculate the changes in "Profit/Losses" over the entire period, 
        # then find the average of those changes
        range1 = range(len(pl)-1)
        for x in range1:
            mpc = pl[x+1] - pl[x]
            plc.append(mpc)

    avg_ch = round(sum(plc)/count,2)
    # total months formula
    net_pl = sum(pl)

    # greatest increase in profits
    gincrease = max(plc)

    #greatest decrease in profits
    gdecrease = min(plc)

# printed results
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(count))
print("Total: $" + str(net_pl))
print("Average Change: $" + str(avg_ch))
print("Greatest  Increase in Profits: " + str(gincrease))
print("Greatest  Decrease in Profits: " + str(gdecrease))

# export text file 



    







