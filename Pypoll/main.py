# 
import os
import csv
csvpath = os.path.join("PyBank", "Resources","budget_data.csv")

# reading using csv module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # The total number of months included in the dataset
    def months(row):
        count = 0
        for row in csvreader:
            count += 1
        return count

        
        
