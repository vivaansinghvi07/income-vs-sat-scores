def incomeVsMathReading(scoresByIncome, method):

    # gets which score to look at
    index = 0 if method == "reading" else 1

    # stores x and y values
    x, y = [], []

    # popualtes arrays
    for income, scores in scoresByIncome.items():
        x.append(int(income.replace(",", "")))
        y.append(int(scores[index]))

    return [x, y]

def incomeVsScore(scoresByIncome):

    # stores x and y values
    x, y = [], []

    # popualates arrays
    for income, scores in scoresByIncome.items():
        x.append(int(income.replace(",", "")))
        y.append(sum(scores))

    return [x, y]