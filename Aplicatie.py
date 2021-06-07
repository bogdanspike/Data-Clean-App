#---IMPORTS---
import pandas as pd
import numpy as np


class Actions:

#---ACTIONS---
    # VIEW TABLE
    def printD(dataframe):
        print(dataframe)
        print("Number of rows: {}.".format(int(dataframe.shape[0])))
        print("Number of columns: {}.".format(int(dataframe.shape[1])))

    # DELETE ROW WITH NAN
    def delete_nan(dataframe):
        dataframe.dropna(inplace=True)
        print(dataframe)

    # DELETE DUPLICATES, KEEP FIRST
    def duplicatef(dataframe):
        dataframe.drop_duplicates(subset=['Name'], keep='first')
        print(dataframe)

    # DELETE DUPLICATES, KEEP SECOND
    def duplicates(dataframe):
        dataframe.drop_duplicates(subset=['Name'], keep='last')
        print(dataframe)

    # DELETE SPECIFIED COLUMN
    def drop_col(dataframe,col_index: int):
        if col_index != 0 and col_index != 4:
            dataframe.drop(dataframe.columns[col_index], inplace=True, axis=1)
        else:
            print("Nu ai voie sa stergi coloanele respective('Name','Rank')")
        print(dataframe.columns)
    
     # DELETE SPECIFIED ROW
    def drop_row(dataframe,row_index: int):
        if row_index != 0:
            dataframe.drop(row_index, inplace=True)
            print(dataframe)
        else:
            print("Nu ai voie sa stergi randul respectiv")
        

    # CALCULATE AVERAGE ON COLUMN
    def average(dataframe,col_index: int):
        average_col=0
        req_col=dataframe.columns[col_index]
        average_obj=dataframe.mean(skipna=True, numeric_only=True)
        average_col=average_obj.get(req_col,'Coloana selectata nu are valoare numerica.')
        print(average_col)

    # CALCULATE MEDIAN ON COLUMN
    def median(dataframe,col_index: int):
        average_med=0
        req_col=dataframe.columns[col_index]
        average_obj_med=dataframe.median(skipna=True, numeric_only=True)
        average_med=average_obj_med.get(req_col,'Coloanei nu i se poate calcula mediana.')
        print(average_med)
    
    #Describe
    def describe(dataframe):
        print(dataframe.describe())

    

class Export:

    # EXPORT
    def exportcsv(dataframe):
        datat.to_csv("New Data-CSV.csv")

    def exportjson(dataframe):
        datat.to_json("New Data-JSON.json")

    def exportexcel(dataframe):
        datat.to_excel("New Data-Excel.xlsx")

#---MENU---

def menu():
        print("Main Choice: Data CLEAN")
        print("Choose 1 - show the table")
        print("Choose 2 - describe")
        print("Choose 3 - delete  duplicate,keep the first")
        print("Choose 4 - delete duplicate,keep the second")
        print("Choose 5 - delete  NaN")
        print("Choose 6 - delete column")
        print("Choose 7 - delete row")
        print("Choose 8 - calculate average on column")
        print("Choose 9 - calculate median on column")
        print("Choose 10 - export csv")
        print("Choose 11 - export json")
        print("Choose 12 - export excel")
        print("Choose 13 - EXIT")
menu()


#---MAIN---  
datat=pd.read_csv("DataC.csv")
choice = input ("Please make a choice: ")
while choice!=13:
    
    if choice == "1":
        Actions.printD(datat) 
    elif choice=="2":
        Actions.describe(datat)
    elif choice == "3":
        Actions.duplicatef(datat)
    elif choice == "4":
        Actions.duplicates(datat)
    elif choice == "5":
        Actions.delete_nan(datat)
    elif choice == "6":
        col_index=int(input("Alege indexul coloanei:"))
        Actions.drop_col(datat,col_index)
    elif choice == "7":
        row_index=int(input("Alege indexul randului:"))
        Actions.drop_row(datat,row_index)
    elif choice == "8":
        col_index=int(input("Alege indexul coloanei:"))
        Actions.average(datat,col_index)
    elif choice == "9":
        col_index=int(input("Alege indexul coloanei:"))
        Actions.median(datat,col_index)  
    elif choice == "10":
        Export.exportcsv(datat)
    elif choice == "11":
        Export.exportjson(datat)
    elif choice == "12":
        Export.exportexcel(datat)   
    elif choice == "13":
        exit()        
    else:
        print("I don't understand the choice")
    
    menu()
    choice = input ("Please make a choice: ")

    


