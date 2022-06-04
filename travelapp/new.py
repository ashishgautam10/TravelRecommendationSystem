from asyncore import read
import pandas as pd
import os
import csv

def apriorialgo(search):
    search=search.strip().lower()
   
    print(search)
    # with open('results.csv')as f:
    #     reader=csv.reader(f)
    #     for row in reader:
           
    #         print(row)
                
    with open('results.csv')as f:
        reader=csv.reader(f)
        for row in reader:
            if len(row)<1:
                continue
            print(row)
            print(row[0].strip().lower())
            if row[0].strip().lower()==search:
                print(row)
                return row[1:]
                break
    # print(os.getcwd())
    # mypath=(os.path.join(os.getcwd(), "travelapp", "apriori.csv"))
    # # print(os.path.exists(mypath))

    # dataset= pd.read_csv(mypath,header=None)
    # # dataset= pd.read_csv('apriori.csv',header=None)


    # total_records=len(dataset)
    # records=[]
    # mylocation=dict()
    # for i in range(0,total_records):
    #     records.append([str(dataset.values[i,k]) for k in range(0,20)])

    # from apyori import apriori
    # associationRules= apriori(records,min_support=0.0053,min_confidence=0.70,min_lift=3,min_length=2)
    # associationResults=list(associationRules)
    # #print(associationResults[0])
    # #print("")
    # #print(len(associationResults))
    # results=[]

    # with open('results.csv','w',encoding='UTF8') as f:
    #     writer=csv.writer(f)
    #     for item in associationResults: #grocery_item lai item bana
    #         pair=item[0]   #grocery_item lai item bana
    #         items=[x for x in pair]



    #         # value0=str(items[0])
    #         # value1=str(items[1])
    #         # value2=str(grocery_item[1])[:7]
    #         # value3=str(grocery_item[2][0][2])[:7]
    #         # value4=str(grocery_item[2][0][3])[:7]




    #         # rows=(value0,value1,value2,value3,value4)
    #         # results.append(rows)

    #         # Label=['List1','List2','Support','Confidence','Lift']

    #         # store_deals=pd.DataFrame.from_records(results,columns=Label)
    #         # print(store_deals)
        



    #         print("Rule: " + items[0] + " -> " + items[1])
        
    #         mylocation[items[0]]=items[1]
    #         print("Support: " + str(item[1]))  
    #         print("Confidence: " + str(item[2][0][2]))  
    #         print("Lift: " + str(item[2][0][3])) 
    #         print("You might also like:"+ str(items[1:])) 
    #         if(items[0]==search):
    #             print(items[0])
    #             print(search)
    #             return (items[1:]) 
    #         print("=====================================")
    #         print(items)
    #         writer.writerow(items)
    # #     print(mylocation[search]) 
    # # apriorialgo(' Daman')