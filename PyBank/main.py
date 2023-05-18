# importing modules
import csv
from pathlib import Path

# declaring file path
inputFile = Path("Resources", "budget_data.csv")

# creating variable lists
totalMonths = []
totalProfit = []
monthlyChangeInProfit = []

# opening csv file
with open(inputFile, "r") as budget:

    # declaring csv variable to store contents
    csvreader = csv.reader(budget, delimiter=",")

    # Parse the header
    header = next(csvreader)

    for row in csvreader:

        # Appending the total months and total profit
        totalMonths.append(row[0])
        totalProfit.append(int(row[1]))

    #  calculating monthly change in profits
    for i in range(len(totalProfit)-1):

        #  appending the difference to profit change per month
        monthlyChangeInProfit.append(totalProfit[i+1]-totalProfit[i])

# maximum and minimum values of profit change
maxIncrease = max(monthlyChangeInProfit)
maxDecrease = min(monthlyChangeInProfit)

# adding one to move on to next month
maxIncreaseByMonth = monthlyChangeInProfit.index(
    max(monthlyChangeInProfit)) + 1
maxDecreaseByMonth = monthlyChangeInProfit.index(
    min(monthlyChangeInProfit)) + 1


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(totalMonths)}")
print(f"Total: ${sum(totalProfit)}")
print(
    f"Average Change: {round(sum(monthlyChangeInProfit)/len(monthlyChangeInProfit),2)}")
print(
    f"Greatest Increase in Profits: {totalMonths[maxIncreaseByMonth]} (${(str(maxIncrease))})")
print(
    f"Greatest Decrease in Profits: {totalMonths[maxDecreaseByMonth]} (${(str(maxDecrease))})")

# Output file
outputFile = Path("analysis", "Financial_Analysis_Summary.txt")

with open(outputFile, "w") as file:

    # converting into write files
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(totalMonths)}\n")
    file.write(f"Total: ${sum(totalProfit)}\n")
    file.write(
        f"Average Change: {round(sum(monthlyChangeInProfit)/len(monthlyChangeInProfit),2)}\n")
    file.write(
        f"Greatest Increase in Profits: {totalMonths[maxIncreaseByMonth]} (${(str(maxIncrease))})\n")
    file.write(
        f"Greatest Decrease in Profits: {totalMonths[maxDecreaseByMonth]} (${(str(maxDecrease))})")
