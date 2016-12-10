# Author Jules Voltaire - javoltaire
# Project 1 - SeriesWinnerFinder
# Project Description: Find the probability of a team winning a series based on the probability of winning one game
import datetime, sys
# Some constants
RECURSIVE_METHOD = 0
DYNAMIC_METHOD = 1

# prints all the values in a 2d array/matrix
def printMatrix(matrix):
    for element in enumerate(matrix):
        print(' '.join(str(element)))
        
# For testing purposes
def generateTest():
    p = 0.4
    print("_______________________________________________")
    for i in range(16):
        print("Number of Teams: " + str(i))
        print("Recursive...")
        beforeR = datetime.datetime.now()
        resultR = recursiveMethod(i, i, p)
        afterR = datetime.datetime.now()
        print(formatResult(resultR))
        print(getTimeDiffMessage(beforeR, afterR))
        print("----------------------------")
        print("Dynamic...")
        beforeD = datetime.datetime.now()
        resultD = dynamicMethod(i, i, p)
        afterD = datetime.datetime.now()
        print(formatResult(resultD))
        print(getTimeDiffMessage(beforeD, afterD))
        print("=================================================")

# This method returns a string indicating the time different between two datetime instances
def getTimeDiffMessage(before, after):
    timeLength = after - before
    return "Computation Time: " + str(timeLength)  
        
# returns a string that for letting the user know what the number returned is.
def formatResult(probResult):
    return "The probability of RedSox winning is: " + str(probResult)

# Calculates the probability of winning using dynamic programming
def dynamicMethod(i, j, p):
    matrixHeight = i + 1    # +1 to account for 0 games
    matrixWidth = j + 1     # +1 to account for 0 games
    # Create the matrix and set all values to 0
    matrix = [[0.00 for x in range(matrixWidth)] for y in range(matrixHeight)]
    
    # Since all the values are 0 we just need set the probability for first row
    for i in range(1, len(matrix[0])):
        matrix[0][i] = 1.00
    
    # Calculate the rest
    q = 1 - p       # Find the probability of the other team
    
    # Start from matrix[1][1] (0 index based) and the value of the current cell
    # should be the p * cell above + q * cell to the left
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            matrix[i][j] = p*matrix[i-1][j] + q*matrix[i][j-1]
    
    # Find bottom right most cell indexes
    lastRow = len(matrix)-1
    lastColumn = len(matrix[lastRow]) - 1
    # printMatrix(matrix)
    # Return the value of that bottom right most cell indexes
    return matrix[lastRow][lastColumn]
        
# Calculates the probability of winning using a recursive method
def recursiveMethod(i, j, p):
    if(i <= 0 and j <= 0):
        return 0
    elif(i <= 0 and j > 0):
        return 1
    elif(i > 0 and j <= 0):
        return 0
    else:
        q = 1 - p       # Calculate the probability of the other team
        return p*recursiveMethod(i-1, j, p) + q*recursiveMethod(i, j-1, p)

def main():
    print("This program will help you determine whether you should bet on a RedSox or Yankees.")
    # Getting input from the user
    n = None    # Holds the number of games to win
    p = None    # Holds the probability of winning each game
    m = None    # Tells which method to use to solve the probability
    # Request the number of teams
    # if the input is invalid then the program will keep asking until a
    # valid one is parsed
    while(1):
        try:
            n = int(input("Enter the number of games necessary to win the series: "))
            break
        except ValueError:
            print("This value must be an integer.")
            
    # Request the probability
    # if the input is invalid then the program will keep asking until a
    # valid one is parsed
    while(1):
        try:
            p = float(input("Enter the probability of RedSox winning a game: "))
            if(p > 1.0):
                print("The probability must be less than or equal to 1.")
                continue
            break
        except ValueError:
            print("This value must be a number.")
    
    # Request the method of calculation
    # if the input is invalid then the program will keep asking until a
    # valid one is parsed
    while(1):
        try:
            m = int(input("Choose the method of calculation: 0 for recursive and 1 for dynamic: "))
            if(m != RECURSIVE_METHOD and m != DYNAMIC_METHOD):
                print("This value must be " + str(RECURSIVE_METHOD) + " or " + str(DYNAMIC_METHOD))
                continue
            break
        except ValueError:
            print("This value must be a number.")
            
    # some more variables
    result = None
    before = None
    after = None
            
    # Call the right function based on the chosen method
    if(m == RECURSIVE_METHOD):
        before = datetime.datetime.now()
        result = recursiveMethod(n, n, p)
        after = datetime.datetime.now()
    else:
        before = datetime.datetime.now()
        result = dynamicMethod(n, n, p)
        after = datetime.datetime.now()
        
    print(formatResult(result))
    print(getTimeDiffMessage(before, after))
    
    # generateTest()
        
            


# Configuring to run main as the main method
if  __name__ =='__main__':
    main()
    
    
    
    
    

        