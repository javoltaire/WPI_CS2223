# Author Jules Voltaire - javoltaire
# Project 1 - SeriesWinnerFinder
# Project Description: Find the probability of a team winning a series based on probability
import sys

# Some constants
RECURSIVE_METHOD = 0
DYNAMIC_METHOD = 1

def dynamicMethod(n, p):
    return "Probability:" + str(p) + "\tTeams:" + str(n) + " using dynamic method "
        
def recursiveMethod(n, p):
    return "Probability:" + str(p) + "\tTeams:" + str(n) + " using recursive method "    

def main():
    print("This program will help you determine whether you should bet on a team.")
    # Getting input from the user
    n = None
    p = None
    m = None
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
            p = float(input("Enter the probability of winning a game: "))
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
        print(recursiveMethod(n, p))
    else:
        print(dynamicMethod(n, p))
            


# Configuring to run main as the main method
if  __name__ =='__main__':
    main()