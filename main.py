
import csv

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
