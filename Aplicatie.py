#---IMPORTS---
import pandas as pd
import numpy as np


class Actions:

#---ACTIONS---
    # VIEW TABLE
    def printD(a):
        print(a)

    # DELETE ROW WITH NAN
    def delete_nan(a):
        a.dropna(inplace=True)
        print(a)

    # DELETE DUPLICATES, KEEP FIRST
    def duplicatef(a):
        a.drop_duplicates(subset=['Name'], keep='first')
        print(a)

    # DELETE DUPLICATES, KEEP SECOND
    def duplicates(a):
        a.drop_duplicates(subset=['Name'], keep='last')
        print(a)

    # DELETE SPECIFIED COLUMN
    def drop_col(a,col_index: int):
        if col_index != 0 and col_index != 4:
            a.drop(a.columns[col_index], inplace=True, axis=1)
        else:
            print("Nu ai voie sa stergi coloanele respective('Name','Rank')")
        print(a.columns)

    # CALCULATE AVERAGE ON COLUMN
    def average(a,col_index: int):
        average_col=0
        req_col=a.columns[col_index]
        average_obj=a.mean(skipna=True, numeric_only=True)
        average_col=average_obj.get(req_col,'Coloana selectata nu are valoare numerica.')
        print(average_col)

    # CALCULATE MEDIAN ON COLUMN
    def median(a,col_index: int):
        average_med=0
        req_col=a.columns[col_index]
        average_obj_med=a.median(skipna=True, numeric_only=True)
        average_med=average_obj_med.get(req_col,'Coloanei nu i se poate calcula mediana.')
        print(average_med)

class Export:

    # EXPORT
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
        print("Choose 8 - delete column")
        print("Choose 9 - calculate average on column")
        print("Choose 10 - calculate median on column")
        print("Choose 11 - EXIT")
menu()


#---MAIN---  
datat=pd.read_csv("DataC.csv")
choice = input ("Please make a choice: ")
while choice!=11:
    
    if choice == "1":
        Actions.printD(datat) 
    elif choice == "2":
        Actions.duplicatef(datat)
    elif choice == "3":
        Actions.duplicates(datat)
    elif choice == "4":
        Actions.delete_nan(datat)
    elif choice == "5":
        Export.exportcsv(datat)
    elif choice == "6":
        Export.exportjson(datat)
    elif choice == "7":
        Export.exportexcel(datat)
    elif choice == "8":
        col_index=int(input("Alege indexul coloanei:"))
        Actions.drop_col(datat,col_index)
    elif choice == "9":
        col_index=int(input("Alege indexul coloanei:"))
        Actions.average(datat,col_index)
    elif choice == "10":
        col_index=int(input("Alege indexul coloanei:"))
        Actions.median(datat,col_index)    
    elif choice == "11":
        exit()        
    else:
        print("I don't understand the choice")
    
    menu()
    choice = input ("Please make a choice: ")

    


