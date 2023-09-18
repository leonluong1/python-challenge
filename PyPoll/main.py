import os
import csv

electionPath = os.path.join(".", "Resources", "election_data.csv")

def analyze_election():
    with open(electionPath, "r") as electionFile:
        voteTotal = 0
        candidates = []
        voteDict = {}
        csvreader = csv.reader(electionFile, delimiter=",")
        headers = next(csvreader)
        for row in csvreader:
            voteTotal += 1

            name = row[2]
            if name not in candidates:
                candidates.append(name)

            if name in voteDict.keys():
                voteDict[name][0] += 1
            else:
                voteDict[name] = [1]

        winner = ""
        winnerTotal = 0
        for name in candidates:
            voteDict[name].append(round((voteDict[name][0]/voteTotal)*100, 3))
            if voteDict[name][0] > winnerTotal:
                winner = name
                winnerTotal = voteDict[name][0]

        print("\nElection Results\n")
        print("----------------------------\n")
        print(f"Total Votes: {voteTotal}\n")
        print("----------------------------\n")

        for name in candidates:
            print(f"{name}: {voteDict[name][1]}% ({voteDict[name][0]})\n")
        print("----------------------------\n")
        print(f"Winner: {winner}\n")
        print("----------------------------\n")

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
