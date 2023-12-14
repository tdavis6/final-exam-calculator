desiredScore = float(input("What percent do you need in the class?\n"))
finalWeighting = float(input("How much weighting does the final have?\n"))
currentScore = float(input("What is your current grade in the class?\n"))

finalScore = (100*desiredScore - ((100-finalWeighting)*(currentScore)))/finalWeighting

finalScore = round(finalScore,2)

finalScore = str(finalScore)
desiredScore = str(desiredScore)

print("You need to achieve a " + finalScore + "% on the final to get a " + desiredScore + "% in the class.")
