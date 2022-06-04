import pandas as pd
import csv
dataset= pd.read_csv('apriori.csv',header=None)
with open('results.csv','a',encoding='UTF8',newline='') as f:
    writer=csv.writer(f)
    total_records=len(dataset)
    records=[]
    for i in range(0,total_records):
        records.append([str(dataset.values[i,k]) for k in range(20,40)])
    print(i)
   

    from apyori import apriori
    associationRules= apriori(records,min_support=0.0053,min_confidence=0.70,min_lift=3,min_length=2)
    associationResults=list(associationRules)
    #print(associationResults[0])
    #print("")
    #print(len(associationResults))
    results=[]


    for item in associationResults: #grocery_item lai item bana
        pair=item[0]   #grocery_item lai item bana
        items=[x for x in pair]



        # value0=str(items[0])
        # value1=str(items[1])
        # value2=str(grocery_item[1])[:7]
        # value3=str(grocery_item[2][0][2])[:7]
        # value4=str(grocery_item[2][0][3])[:7]




        # rows=(value0,value1,value2,value3,value4)
        # results.append(rows)

        # Label=['List1','List2','Support','Confidence','Lift']

        # store_deals=pd.DataFrame.from_records(results,columns=Label)
        # print(store_deals)
    



        print("Rule: " + items[0] + " -> " + items[1])  
    
        print("Support: " + str(item[1]))  
        print("Confidence: " + str(item[2][0][2]))  
        print("Lift: " + str(item[2][0][3])) 
        # print("You might also like:"+ str(items[1])) 
        print( items[1:]) 
        writer.writerow(items)
        print("=====================================") 
