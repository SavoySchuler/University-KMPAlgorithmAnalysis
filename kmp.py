import sys
from kmpUnitTests import *

def KMP(T, P):  #T for text, P for pattern

    #initialize local variables

    matches = 0                     #count number of matches found
    n = len(T)                      #length of text
    m = len(P)                      #length of pattern
    PMT = PrefixFunc(P)             #partial matches table    
    q = 0                           #number of characters matched

    #display prefix table for user

    print ("\nPrefix table: ")
    for i in range(len(PMT)):
        print (PMT[i])  

    #verify pattern and text lengths to user

    print ("\nLength Pattern: " + str(m))
    print ("Length Text: " + str(n)+"\n")   
 
    #begin searching string for matches    
    for i in range(n):                      #scan text from left to right
        while q > 0 and P[q] != T[i]:       #while next char does not match
            q = PMT[q]                      #use table to "jump" # char matches
        if P[q] == T[i]:                    #when next character does match
            q = q + 1                       #increment # of char matches by 1
        if q == m:                          #if all characters in pattern found
            matches = matches + 1  #update number of matches
            #output location of match and number of char shifts needed to find
            print ("Pattern starts at the " + str(i+3-m) \
                + " position. Shift = " + str(i + 1 - m) )  
            q = PMT[q-1]                    #look for next match
    
    #conclude search
    #finish function with conditional output

    if matches == 0:             #if no matches found, inform user
        print ("\nNo match!\n")     
    else:                           #if matches were found, print total number
        print ("\nTotal number of matches found: " + str(matches) + "\n")
    return matches 



def PrefixFunc(P):  #P for pattrn

    #initialize local variables

    m = len(P)    #store length of patterm
    PMT = []            #table for prefix = suffix lengths in pattern 
                        #used for partial match "jumps" in full string search
    k = 0               #number of characters in pattern matched

    #initialize values of partial matches table

    for i in range(m):      #for length of the pattern...
        PMT.append(i+1)     #set each index to its 1-indexed location
    PMT[0] = 0              #set index of first character in pattern to zero

    #create table for prefix = suffix partial match jumps

    for q in range(m-1):                #for 1-index number of chars in pattern
        while k > 0 and P[k] != P[q+1]: #while char and index char do not match
            k = PMT[k]                  #use table to "jump" # of char matches
        if P[k] == P[q+1]:              #when indexed char does match
            k = k + 1                   #increment number of char matches by 1
        PMT[q+1] = k                    #update table with # of matched chars
                                        
    #this table will reflect the number of characters the search can skip ahead
        # when a partial mismatch occurs
    
    #return the table of partial matches to be used in search

    return PMT      



# this pattern allows us to mimic a main function
if __name__ == '__main__':
    if len(sys.argv) == 3:      #if full command line parameters entered
        Text = sys.argv[1]      #set text
        Pattern = sys.argv[2]   #set pattern
        KMP (Text, Pattern)     #call KMP search
    
    elif len(sys.argv) == 2:    #if flag set, check if for test, default to help
        if sys.argv[1] == 'test' or sys.argv[1] == '-t':    #if flag for testing
            tests()             #call function to run prewritten unit tests
        else:                   #any other, default to help for usage
            print("\nUsages:")  #list usage call types
            print("Run:  python3 kmp.py <text> <pattern>")
            print("Test: python3 kmp.py {-t} or {test} >> testResults.txt")
            print("Help: python3 kmp.py {-h} or {help}\n")
    else:                       #if no parameters passed, enter user input mode
        Text = input("\nPlease enter text to be searched: \n\n")
        Pattern = input("\nPlease enter pattern to search for: \n\n") 
        KMP (Text, Pattern)     #call KMP on user input
