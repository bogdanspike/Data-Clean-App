#---IMPORTS---
import pandas as pd
import numpy as np


#---ACTIONS---


class actions:

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
        a.drop_duplicates(subset=['Name'], keep='last')
        printD(a)

# EXPORT
class exportd:
    def exportcsv(a):
        datat.to_csv("New Data-CSV.csv")

    def exportjson(a):
        datat.to_json("New Data-JSON.json")

    def exportexcel(a):
        datat.to_excel("New Data-Excel.xlsx")

#---MENU---

def menu():
        print("Main Choice: Data CLEAN")
        print("Choose 1 - show the table")
        print("Choose 2 - delete  duplicate,keep the first")
        print("Choose 3 - delete duplicate,keep the second")
        print("Choose 4 - delete  NaN")
        print("Choose 5 - export csv")
        print("Choose 6 - export json")
        print("Choose 7 - export excel")
        print("Choose 8 - EXIT")
menu()


#---MAIN---  
datat=pd.read_csv("DataC.csv")
choice = input ("Please make a choice: ")
while choice!=8:
    
    if choice == "1":
        actions.printD(datat) 
    elif choice == "2":
        actions.duplicatef(datat)
    elif choice == "3":
        actions.duplicates(datat)
    elif choice == "4":
        actions.deleteNan(datat)
    elif choice == "5":
        exportd.exportcsv(datat)
    elif choice == "6":
        exportd.exportjson(datat)
    elif choice == "7":
        exportd.exportexcel(datat)
    elif choice == "8":
        exit()
    else:
        print("I don't understand the choice")
    
    menu()
    choice = input ("Please make a choice: ")

    


