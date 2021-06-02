#---IMPORTS---
import pandas as pd
import numpy as np

#---ACTIONS---

# VIEW TABLE
def printD(a):
    print(a)

# DELETE ROW WITH NAN
def deleteNan(a):
    a.dropna(inplace=True)
    printD(a)

# DELETE DUPLICATES, KEEP FIRST
def duplicatef(a):
    a.drop_duplicates(subset=['Name'], keep='first')
    printD(a)

# DELETE DUPLICATES, KEEP SECOND
def duplicates(a):
    a.drop_duplicates(subset=['Name'], keep='second')
    printD(a)

# EXPORT
def exportd(a):
    datat.to_csv("New Data1.csv")

#---MENU---

def menu():
        print("Main Choice: Data CLEAN")
        print("Choose 1 - show the table")
        print("Choose 2 - delete  duplicate,keep the first")
        print("Choose 3 - delete duplicate,keep the second")
        print("Choose 4 - delete  NaN")
        print("Choose 5 - export new csv")
        print("Choose 6 - EXIT")
menu()

#---MAIN---  
datat=pd.read_csv("DataC.csv")
choice = input ("Please make a choice: ")
while choice!=6:
    
    if choice == "1":
        printD(datat) 
    elif choice == "2":
        duplicatef(datat)
    elif choice == "3":
        duplicates(datat)
    elif choice == "4":
        deleteNan(datat)
    elif choice == "5":
        exportd(datat)
    elif choice == "6":
        exit()
    else:
        print("I don't understand the choice")
    
    menu()
    choice = input ("Please make a choice: ")

    


