# importing modules
import csv
from pathlib import Path

# declaring file path
inputFile = Path("Resources", "election_data.csv")


# declaring variables
rowCount = 0
candidateList = list()

# Opening csv file to store contents
with open(inputFile, newline="") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

  # total rows
    next(csvReader)
    data = list(csvReader)
    rowCount = len(data)

  # creating a list to count total candidates

    total = list()
    for i in range(0, rowCount):
        candidate = data[i][2]
        total.append(candidate)
        if candidate not in candidateList:
            candidateList.append(candidate)
    candidateCount = len(candidateList)

  # total number of votes and the percentage of votes
    votes = list()
    percentage = list()
    for j in range(0, candidateCount):
        name = candidateList[j]
        votes.append(total.count(name))
        votePercentage = votes[j]/rowCount
        percentage.append(votePercentage)

  # declaring the winner
    winner = votes.index(max(votes))

  # Printing the results
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {rowCount:,}")
    print("----------------------------")
    for k in range(0, candidateCount):
        print(f"{candidateList[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidateList[winner]}")
    print("----------------------------")


# Output file
outputFile = Path("analysis", "PyPoll.txt")
# Printing the results
with open(outputFile, "w") as file:

    # writing to file
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {rowCount:,}\n")
    file.write("----------------------------\n")
    for k in range(0, candidateCount):
        file.write(f"{candidateList[k]}: {percentage[k]:.3%} ({votes[k]:,})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {candidateList[winner]}\n")
    file.write("----------------------------")
