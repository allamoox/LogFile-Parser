import sys

Usage=("Please write the script name followed by the logfile location and the required action. Available actions are  (statistics, error and notice)\n....\
Example:- actionloganalyzer.py /home/cLaS1c/PathToMyLogFile/test.log statistics....")

if len(sys.argv) <3:
    print(Usage)
    sys.exit()
elif len(sys.argv) > 3 :
    print(Usage)
    sys.exit()
else:

    if str(sys.argv[2]) == ("error"):
        with open('test.log', "r") as file:
            for line in file:
               if 'error]' in line:                    
                print(line[1:25], line[35:]) 

    elif str(sys.argv[2]) == ("notice") :
        with open('test.log', "r") as file:
            for line in file:
               if 'ce]' in line:                    
                print(line[1:25], line[36:], end=' ') 

    elif str(sys.argv[2]) == ("statistics") :
        with open('test.log' , 'r') as file:
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
