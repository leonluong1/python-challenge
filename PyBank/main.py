import os
import csv

bankPath = os.path.join(".", "Resources", "budget_data.csv")

def analyze_records():
    with open(bankPath, "r") as bankFile:
        monthTotal = 0
        netProfit = 0
        totalChange = 0
        maxInc = 0
        maxIncDate = ""
        maxDec = 0
        maxDecDate = ""
        csvreader = csv.reader(bankFile, delimiter=",")
        headers = next(csvreader)
        prevAmount = 0
        for row in csvreader:
            value = int(row[1])
            monthTotal += 1
            netProfit += value
            currChange = value - prevAmount
            if monthTotal > 1:
                totalChange += currChange
            prevAmount = value

            if currChange > maxInc:
                maxInc = currChange
                maxIncDate = row[0]
            if currChange < maxDec:
                maxDec = currChange
                maxDecDate = row[0]

        print("\nFinancial Analysis\n")
        print("----------------------------\n")
        print(f"Total Months: {monthTotal}")
        print(f"Total: ${netProfit}")
        print(f"Average Change: ${round(totalChange/(monthTotal -1), 2)}")
        print(f"Greatest Increase in Profits: {maxIncDate} (${maxInc})")
        print(f"Greatest Decrease in Profits: {maxDecDate} (${maxDec})")

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
