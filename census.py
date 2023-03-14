import csv

def dictHeader(code):
    return f"ZCTA5 {code}!!Households!!Estimate"

def getCensusData(zipCodes):

    # creates output
    output = {}

    # saves index
    index = -1

    # gets the index of the reader where the median income is
    with open("census-data.csv", "r") as f:

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
    with open("census-data.csv", "r") as f:
        
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
    return int(address.split(" ")[-1])

def getZipCodes():

    # stores the scores but this time according to zip code
    ZipByDBN = {}

    with open("datasets/school-locations.csv", "r") as f:

        # creates reader
        reader = csv.DictReader(f)

        # assigns a zip code by the DBN number
        for line in reader:
            ZipByDBN[line["ATS SYSTEM CODE"]] = addressToZip(line["Location 1"])

    return ZipByDBN
