import os
import csv
csvpath=os.path.join("Resources", "budget_data.csv") 

with open(csvpath) as csvfile: #open file
    csvreader = csv.reader(csvfile, delimiter=',') 
    csvheader=next(csvreader)
    net_profit_losses=0
    count=0
    tot_diff=0
    diff=0
    grt_inc=0
    grt_dec=0
    col1=[0]
    col2=[]
    col3=[]
       
    for i in csvreader:
        col1.append(int(i[1]))
        col2.append(int(i[1]))
        diff=col2[count] - col1[count]
        col3.append(diff)
        
        if diff>grt_inc:
            grt_inc=diff
            inc_date=i[0]
            
        if diff<grt_dec:
            grt_dec=diff
            dec_date=i[0]
            
        tot_diff=tot_diff+diff
        net_profit_losses=net_profit_losses+int(i[1])
        count=count+1
        
    tot_diff=tot_diff-int(col3[0])

tot_month= f'''
Financial Analysis
---------------------------------------------------
Total Months:{count}
Total:{net_profit_losses}
Average Change:{tot_diff/(count-1)}
Greatest Increase:{grt_inc} happened on {inc_date}
Greatest Decrease:{grt_dec} happened on {dec_date}'''


# save the output file path
csvpath=os.path.join("Analysis", "Analysis.txt") 

# open the output file, create a header row, and then write the zipped object to the csv
with open(csvpath, "w") as text:
    text.write(tot_month)
print(tot_month)