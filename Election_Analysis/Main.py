import os
import csv
csvpath=os.path.join("Resources", "election_data.csv") 
with open(csvpath) as csvfile: #open file
    csvreader = csv.reader(csvfile, delimiter=',') 
    csvheader=next(csvreader)
    votes_cast=0
    most_votes=0
    candidates_dic={}
    candidates_list=[]
    analysis_txt=[]
    winner=[]
    for i in csvreader:
        votes_cast=votes_cast+1
        if i[2] not in candidates_dic: 
            candidates_dic[i[2]]=1
            candidates_list.append(i[2])
        else:
            candidates_dic[i[2]]+=1
        
    
    analysis_txt.append("Election Results")
    analysis_txt.append("--------------------------")
    analysis_txt.append(f"Total Votes Cast:{votes_cast}")
    analysis_txt.append("--------------------------")
    count=0
    for i in candidates_list:
            analysis_txt.append(f"{candidates_list[count]}: {round(candidates_dic[candidates_list[count]]/votes_cast*100,2)}%      ({candidates_dic[candidates_list[count]]})")
            if candidates_dic[candidates_list[count]]>most_votes:
                most_votes=candidates_dic[candidates_list[count]]
                winner=candidates_list[count]
            count+=1

    analysis_txt.append("--------------------------")
    analysis_txt.append(f"Winner: {winner}")


    # save the output file path
csvpath=os.path.join("Analysis", "Analysis.txt") 

# open the output file, create a header row, and then write the zipped object to the csv
with open(csvpath, "w") as text:
    
    for i in analysis_txt:
        text.write(i)
        text.write("\n")
        print(i)