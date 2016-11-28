# Resources
# Generating string Permutation
# https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
# Better Algorith Idea - Count and Compare
# http://ice-web.cc.gatech.edu/ce21/1/static/audio/static/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html

# Author Jules Voltaire - javoltaire
# Project 1 - AnagramDetector
# Project Description: implement and compare algorithms for determining if two strings are anagrams
import datetime, re, sys

BRUTE_FORCE = "bf"
BETTER = "btr"
TOTAL_NUM_LETTERS = 26

# Depending on the result this method will return a string 
# Indicating wether the two strings are anagrams or not
def getAnagramResultMessage(str1, str2, res):
    if(res):
        return "\"" + str1 + "\" and \"" + str2 + "\" ARE Anagrams"
    else:
        return "\"" + str1 + "\" and \"" + str2 + "\" ARE NOT Anagrams"
    
# This method returns a string indicating the time different between two datetime instances
def getTimeDiffMessage(before, after):
    timeLength = after - before
    return "Computation Time: " + str(timeLength)  

# Takes a string and strips all the spaces and non letter characters and replaces uppercase letters with lower case ones
# If the string is empty then an empty string is returned
def formatString(sInput):
    if(len(sInput) == 0):
        return "";
    else:
        regex = re.compile('[^a-zA-Z]')
        return regex.sub('', sInput).lower()

# Returns a generator over which we can iterate to get all permutations of a given string
def stringPerms(strInput):
     if len(strInput) <=1:
        yield strInput
     else:
        for permutation in stringPerms(strInput[1:]):
            for i in range(len(strInput)):
                yield permutation[:i] + strInput[0:1] + permutation[i:]

# Returns true if the two given strings are anagrams using the brute force approach
# Note. if the two string have different lenghts then false is immidiately returned
def bruteForce(str1, str2):
    if(len(str1) != len(str2)):
        return False
    else:
        for i in stringPerms(str2):
            if(str1 == i):
                return True
    return False

# Logs the time efficiency of the brute force algorithm and prints it out and then prints
# out whether the two strings are anagrams or not     
def effAnaBF(s1,s2):
    before = datetime.datetime.now()
    res = bruteForce(s1, s2)
    after = datetime.datetime.now()
    
    print(getAnagramResultMessage(s1, s2, res))
    print(getTimeDiffMessage(before, after) + " using brute force")
    
# Returns true if the two given strings are anagrams using a count and compare approach
# Note. if the two string have different lenghts then false is immidiately returned
def countAndCompare(str1, str2):
    isAnagram = True           # Boolean that indicates whether the two strings are anagrams
    if(len(str1) != len(str2)):
        isAnagram = False;
    else:
        cnt1 = [0]*TOTAL_NUM_LETTERS            # Array that will keep track of the number of each letter for in str1
        cnt2 = [0]*TOTAL_NUM_LETTERS            # Array that will keep track of the number of each letter for in str2
        
        # Loop over str1 and figure out how many of the 26 letters are present
        for i in range(len(str1)):
            # ord returns an number for a specific character, we will use that
            # to determine the index of the str1 character in the cnt1 array
            # see. https://docs.python.org/2/library/functions.html#ord for full documentation
            index = ord(str1[i]) - ord('a')     # Sustract the number for 'a' to get a 0 based index number
            cnt1[index] += 1                    # Increment the count for that letter
        
        # Loop over str2 and figure out how many of the 26 letters are present
        for i in range(len(str2)):
            # ord returns an number for a specific character, we will use that
            # to determine the index of the str2 character in the cnt2 array
            index = ord(str2[i]) - ord('a')     # Sustract the number for 'a' to get a 0 based index number
            cnt2[index] += 1                    # Increment the count for that letter
            
        # Now we need to compare the two counts and see if they are the same
        for j in range(TOTAL_NUM_LETTERS):
            if(cnt1[j] != cnt2[j]):
                isAnagram = False
                break
                
    return isAnagram
    
# Logs the time efficiency of the count and compare algorithm and prints it out and then prints
# out whether the two strings are anagrams or not  
def effAnaBtr(s1,s2):
    before = datetime.datetime.now()
    res = countAndCompare(s1, s2)
    after = datetime.datetime.now()
        
    print(getAnagramResultMessage(s1, s2, res))
    print(getTimeDiffMessage(before, after) + " using count and compare")
            
# This is the main method
def main():
    print("Welcome to AnagramDetector!!")
    # Getting input from the user.
    # Request the first string and make sure it is valid. Keep asking for it until valid
    s1 = input("Enter the first string: ")
    while(len(s1) == 0):
        print("String cannot be empty.")
        s1 = input("Enter the first string: ")
    formattedS1 = formatString(s1)
    print("String 1: " + formattedS1)

    # Request the second string and make sure it is valid. Keep asking for it until valid
    s2 = input("Enter the second string: ")
    while(len(s2) == 0):
        print("String cannot be empty.")
        s2 = input("Enter the second string: ")
    formattedS2 = formatString(s2)
    print("String 2: " + formattedS2)

    # Ask for the algorithm method to use. Keep asking if not br or btr
    method = input("Choose an algorithm method: \"bf\" for brute force or \"btr\" for a better algorithm: ")
    while(method != BRUTE_FORCE and method != BETTER):
        print("The method has to be \"bf\" for brute force or \"btr\" for a better algorithm.")
        method = input("Choose an algorithm method: ")

    # Call the right algorithm based on the one, the user picked
    if(method == BRUTE_FORCE):
        effAnaBF(formattedS1, formattedS2)
    else:
        effAnaBtr(formattedS1,formattedS2)

# Configuring to run main as the main method
if  __name__ =='__main__':
    main()