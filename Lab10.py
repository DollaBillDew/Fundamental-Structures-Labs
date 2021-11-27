import csv
import json
import os

#opens the csv file
with open("SalesJan2009(1).csv","r") as f:
    reader=csv.reader(f)
    sales_data=[]
    #iterate through each line and puts value into the list in form of dictionary
    for row in reader:
        sales_data.append({'Transaction_date':row[0].strip('"'),'Product':row[1].strip('"'),'Price':row[2].strip('"')
                           ,'Payment_Type':row[3].strip('"'),'Name':row[4].strip('"'), 'City':row[5].strip('"'),'State':row[6].strip('"'),'Country':row[7].strip('"')})

#creates a json file and added data into it.
with open('transaction_data.json','w') as jsonf:
    json.dump(sales_data,jsonf, indent=4) 