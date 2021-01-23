import sys
import csv
import re



def main():
    if len(sys.argv) != 3: #checks if the number of arguments is right, if it's wrong prints the right usage and return 0, exiting the program.
        print("Usage: python elixir.py shoplist.csv e-mails.csv")
        exit(0) #exit returning 0, program will not do his job.

    else:
        with open(sys.argv[1], newline='\n') as csvfile1:
            shopdict = csv.DictReader(csvfile1) #open the 1srt csv file on the argument as a dict and assign it to the variable shopdict.

            with open(sys.argv[2], newline='\n') as csvfile2:
                people = csv.reader(csvfile2) #open the 2nd csv file on the argument as a dict and assign it to the variable shopdict.

                shareit(shopdict, people) #call shareit function to share the bill from the shopdict (shoplist dict) among the people (list of people).

def shareit(shopdict, people):
    share = 0 #declare the variable share and assign the 0 value

    for row in shopdict:
        share = share + int(row['price'])*int(row['amount']) #each line of dictshare is incremented on share(int) by adding up each item's price multiplied by the amount.

    if share == 0:
        print("There is nothing to be shared!") #if the dictshare value is 0, it means that there is nothing to pay, consequently nothing to be shared.

    else:
        sharedict = {} #declare the dict sharedict
        counter = 0 #create the variable counter and assign the 0 value

        for row in people:
            for i in row:
                sharedict[i] = 0 #define a sharedict item for each person on people list as the key and assigning 0 as value.
                counter = counter + 1 #count the number of people on the list
        if counter==0:
            print("There is nobody to share!") #if counter == 0, it means nobody on people list, consequently nobody to pay.
        else:
            rest = share % counter #declare the rest(int) with value as share(int) module counter(int)
            share = int(share / counter)
            test = 0
            for i in range(counter): #uptade sharedict values to each person share
                if (counter - i <= rest): #including de rest the division, every cents counts
                    sharedict[row[i]] = share + 1
                    test = test + share + 1
                else:
                    sharedict[row[i]] = share
                    test = test + share
            if(test == share * counter + rest): #do a test to check the bill and each person share. If its ok, exit returning sharedict.
                exit (sharedict)

    exit(0) #if the program didnt exit yet, exit returning 0, it failed.



main()