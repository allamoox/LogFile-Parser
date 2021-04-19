#Mahmoud Allam  allam@1091see.com
#Last version for the project submission, os library/module is imported to check  if the logFile exist or not, Also it uses argv[0] to print the script name inside the \
#Usage variable.
# I know this should be the best LogFile Parser ever!!!!# :p :>

import sys
import os
 
Usage=("Please write the script name followed by the logfile location and the required action. Available actions are  (statistics, error and notice)\n....\
Example:- ", sys.argv[0], "/home/cLaS1c/PathToMyLogFile/test.log statistics....")
 
# The below block I have made it in if elif statment to practice it
#However, I can use doesn't equal operator ---> if len(sys.argv) != 3 
if len(sys.argv) <3:
    print(Usage)
    sys.exit()
elif len(sys.argv) > 3 :
    print(Usage)
    sys.exit()
elif os.path.isfile(sys.argv[1]):
 
    if str(sys.argv[2]) == ("error"):
        with open(sys.argv[1], "r") as file:
            for line in file:
               if 'error]' in line:                    
                print(line[1:25], line[35:]) 
 
    elif str(sys.argv[2]) == ("notice") :
        with open(sys.argv[1], "r") as file:
            for line in file:
               if 'ce]' in line:                    
                print(line[1:25], line[36:], end=' ') 
 
    elif str(sys.argv[2]) == ("statistics") :
        with open(sys.argv[1] , 'r') as file:
            counter = 0
            for i in file:
                if 'or]' in i:
                   counter += 1
        print("The Logfile contains \n", counter , "Errors")
 
        with open('test.log' , 'r') as file:
            counter = 0
            for i in file:
                if 'ce]' in i:
                   counter += 1
        print("",counter, "Notices")
    else:
        print(Usage)
else:
    print("Check your LogFile Path!! Your file doesn't Exist")
