import os
import csv

# Importing csv file, must be in PyPoll folder.
bankPath = os.path.join(".", "Resources", "budget_data.csv")

def analyze_records():
    # Opening csv file
    with open(bankPath, "r") as bankFile:
        monthTotal = 0
        netProfit = 0
        totalChange = 0
        maxInc = 0
        maxIncDate = ""
        maxDec = 0
        maxDecDate = ""
        prevAmount = 0

        # Creating reader object and storing headers
        csvreader = csv.reader(bankFile, delimiter=",")
        headers = next(csvreader)
        
        for row in csvreader:
            value = int(row[1])
            monthTotal += 1

            # Adding all profits and losses together to find net profit
            netProfit += value

            # Finding the current profits/losses this month by finding the difference from previous month
            currChange = value - prevAmount

            # Adding all the monthly changes to find average later
            if monthTotal > 1:
                totalChange += currChange
            prevAmount = value

            # Finding the greatest monthly increase/decrease while iterating through data
            if currChange > maxInc:
                maxInc = currChange
                maxIncDate = row[0]
            if currChange < maxDec:
                maxDec = currChange
                maxDecDate = row[0]

        # Printing report to terminal
        print("\nFinancial Analysis\n")
        print("----------------------------\n")
        print(f"Total Months: {monthTotal}")
        print(f"Total: ${netProfit}")
        print(f"Average Change: ${round(totalChange/(monthTotal -1), 2)}")
        print(f"Greatest Increase in Profits: {maxIncDate} (${maxInc})")
        print(f"Greatest Decrease in Profits: {maxDecDate} (${maxDec})")

        # Writing report to "./analysis/analysis.txt"
        outputPath = os.path.join(".", "analysis", "analysis.txt")
        outputFile = open(outputPath, "w")
        outputFile.write("Financial Analysis\n\n")
        outputFile.write("----------------------------\n\n")
        outputFile.write(f"Total Months: {monthTotal}\n\n")
        outputFile.write(f"Total: ${netProfit}\n\n")
        outputFile.write(f"Average Change: ${round(totalChange/(monthTotal -1), 2)}\n\n")
        outputFile.write(f"Greatest Increase in Profits: {maxIncDate} (${maxInc})\n\n")
        outputFile.write(f"Greatest Decrease in Profits: {maxDecDate} (${maxDec})\n\n")

analyze_records()
