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

print(getCensusData([10001, 10002]))