# imports data management functions
import managedata
import scoresplit

# imports graphing libraries 
import matplotlib.pyplot as plt

# stores scores by income
data = managedata.filterData(managedata.getScoresByIncome())

# fills [x, y] lists with the information to be graphed
readingByIncome = scoresplit.incomeVsMathReading(data, "reading")
mathByIncome = scoresplit.incomeVsMathReading(data, "math")
scoreByIncome = scoresplit.incomeVsScore(data)

# plots reading scores
plt.scatter(readingByIncome[0], readingByIncome[1])
plt.xlabel("Median Household Income In School's ZIP Code")
plt.ylabel("Average SAT Reading Score")
plt.savefig('results/reading.png')
plt.close()

# plots math scores
plt.scatter(mathByIncome[0], mathByIncome[1])
plt.xlabel("Median Household Income In School's ZIP Code")
plt.ylabel("Average SAT Math Score")
plt.savefig('results/math.png')
plt.close()

# plots total scores
plt.scatter(scoreByIncome[0], scoreByIncome[1])
plt.xlabel("Median Household Income In School's ZIP Code")
plt.ylabel("Average SAT Score")
plt.savefig('results/score.png')
plt.close()