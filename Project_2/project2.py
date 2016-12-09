# Author Jules Voltaire - javoltaire
# Project 1 - SeriesWinnerFinder
# Project Description: Find the probability of a team winning a series based on probability
import sys
# Some constants
RECURSIVE_METHOD = 0
DYNAMIC_METHOD = 1

def printMatrix(matrix):
    for i, element in enumerate(matrix):
        print(' '.join(str(element)))

def dynamicMethod(i, j, p):
    matrixHeight = i + 1    # +1 to account for 0 games
    matrixWidth = j + 1     # +1 to account for 0 games
    matrix = [[0 for x in range(matrixWidth)] for y in range(matrixHeight)]
    
    printMatrix(matrix)
    return "Probability:" + str(p) + "\tTeams:" + str(j) + " using dynamic method "
        
def recursiveMethod(i, j, p):
    if(i <= 0 and j > 0):
        return 1
    elif(i > 0 and j <= 0):
        return 0
    else:
        q = 1 - p
        return p*recursiveMethod(i-1, j, p) + q*recursiveMethod(i, j-1, p)

def main():
    print("This program will help you determine whether you should bet on a RedSox or Yankees.")
    # Getting input from the user
    n = None    # Holds the number of games to win
    p = None    # Holds the probability of winning each game
    m = None    # Tells which method to use to solve the probability
    # Request the number of teams
    while(1):
        try:
            n = int(input("Enter the number of games necessary to win the series: "))
            break
        except ValueError:
            print("This value must be an integer.")
            
    # Request the probability
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
    while(1):
        try:
            m = int(input("Choose the method of calculation: 0 for recursive and 1 for dynamic: "))
            if(m != RECURSIVE_METHOD and m != DYNAMIC_METHOD):
                print("This value must be " + str(RECURSIVE_METHOD) + " or " + str(DYNAMIC_METHOD))
                continue
            break
        except ValueError:
            print("This value must be a number.")
            
    # Call the right function based on the chosen method
    if(m == RECURSIVE_METHOD):
        print(str(recursiveMethod(n, n, p)))
    else:
        print(dynamicMethod(n, n, p))
            


# Configuring to run main as the main method
if  __name__ =='__main__':
    main()
    
    
    
    
    

        