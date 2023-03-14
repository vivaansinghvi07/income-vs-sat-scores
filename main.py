# imports data management functions
import managedata

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