import os
import csv

# Importing csv file, must be in PyPoll folder.
electionPath = os.path.join(".", "Resources", "election_data.csv")

def analyze_election():
    # Opening csv file
    with open(electionPath, "r") as electionFile:
        voteTotal = 0
        candidates = []
        voteDict = {}

        # Creating reader object and storing headers
        csvreader = csv.reader(electionFile, delimiter=",")
        headers = next(csvreader)
        for row in csvreader:
            name = row[2]
            voteTotal += 1

            # Appending each unique candidate to a list
            if name not in candidates:
                candidates.append(name)

            # Adding votes for each candidate to a dict
            if name in voteDict.keys():
                voteDict[name][0] += 1
            else:
                voteDict[name] = [1]

        winner = ""
        winnerTotal = 0

        # Iterating through vote dict to find candidate with highest vote total (winner).
        for name in candidates:
            voteDict[name].append(round((voteDict[name][0]/voteTotal)*100, 3))
            if voteDict[name][0] > winnerTotal:
                winner = name
                winnerTotal = voteDict[name][0]

        # Printing report to terminal
        print("\nElection Results\n")
        print("----------------------------\n")
        print(f"Total Votes: {voteTotal}\n")
        print("----------------------------\n")

        for name in candidates:
            print(f"{name}: {voteDict[name][1]}% ({voteDict[name][0]})\n")
        print("----------------------------\n")
        print(f"Winner: {winner}\n")
        print("----------------------------\n")

        # Writing report to "./analysis/analysis.txt"
        outputPath = os.path.join(".", "analysis", "analysis.txt")
        outputFile = open(outputPath, "w")
        outputFile.write("Election Results\n")
        outputFile.write("\n----------------------------\n")
        outputFile.write(f"\nTotal Votes: {voteTotal}\n")
        outputFile.write("\n----------------------------\n")

        for name in candidates:
            outputFile.write(f"\n{name}: {voteDict[name][1]}% ({voteDict[name][0]})\n")
        outputFile.write("\n----------------------------\n")
        outputFile.write(f"\nWinner: {winner}\n")
        outputFile.write("\n----------------------------\n")


analyze_election()
