import csv

def dictHeader(code):
    return f"ZCTA5 {code}!!Households!!Estimate"

def getCensusData(zipCodes):

    # creates output
    output = {}

    # saves index
    index = -1

    # gets the index of the reader where the median income is
    with open("datasets/census-data.csv", "r") as f:

        # creates a reader
        reader = csv.DictReader(f)

        # the name of the field of the first element (the label) 
        label = reader.fieldnames[0]

        # converts reader into a list for indexing
        readerList = list(reader)

        for i in range(len(readerList)):
            if readerList[i][label] == "Median income (dollars)":
                index = i
    
    # returns an array of incomes corresponding to the zip codes entered
    with open("datasets/census-data.csv", "r") as f:
        
        # creates a reader in list form so it can be indexed over
        reader = list(csv.DictReader(f))

        # goes through every zip code given
        for code in zipCodes:

            # gets the income of the code
            output[code] = reader[index][dictHeader(code)]

    # returns a dictionary with zip code and corresponding household incomes
    return output


def getScoresAndCodes():

    # stores the school's DBN as a key and its SAT scores as a value
    scoresByDBN = {}

    with open ("datasets/2012-sat-results.csv", "r") as f:

        # creates reader
        reader = csv.DictReader(f)

        # stores the reading and math scores as a list pointed to by the DBN of the school
        for line in reader:
            scoresByDBN[line["DBN"]] = [line["SAT Critical Reading Avg. Score"], line["SAT Math Avg. Score"]]

    return scoresByDBN

def addressToZip(address):
    try:
        return int(address.split("\n")[-2].split(" ")[-1])
    except:
        pass

def getZipCodes():

    # stores the scores but this time according to zip code
    ZipByDBN = {}

    with open("datasets/school-locations.csv", "r") as f:

        # creates reader
        reader = csv.DictReader(f)

        # assigns a zip code by the DBN number
        for line in reader:
            ZipByDBN[line["ATS SYSTEM CODE"].strip()] = addressToZip(line["Location 1"])

    return ZipByDBN

def getScoresByIncome():
    # gets dicts
    scoresByDBN = getScoresAndCodes()
    DBNtoZip = getZipCodes()

    # creates dict of scores by the zip code
    scoresByZip = {}

    # fills the scores by zip code dictionary
    for dbn, scores in scoresByDBN.items():
        try:
            scoresByZip[DBNtoZip[dbn]] = scores
        except:
            continue

    # gets zip codes that need to be converted to incomes
    zips = []

    # fills zips list
    for zip in scoresByZip.keys():
        if not zip:
            continue
        zips.append(zip)

    # gets incomes by zip code
    incomeByZip = getCensusData(zips)

    # creates dict of scores by median income
    scoresByIncome = {}

    # fills scores by income
    for zip, scores in scoresByZip.items():
        try:
            scoresByIncome[incomeByZip[zip]] = scores
        except:
            continue

    return scoresByIncome

def filterData(scoresByIncome):

    # empty output dict
    output = {}

    # filters out ['s', 's'] lists
    for income, score in scoresByIncome.items():
        if score[0] == 's':
            continue
        output[income] = score

    return output