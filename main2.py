

#PyPoll


# Modules
import os
import csv

count = 0


# function to get unique values 
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list


#listy = ["a","a","q","q","a","a"]
#stringy = "q"
#num = 0
#print("list:",listy)
#print("string:",stringy)
#print("num:",num)

def Count_in(list1,string1):
    y_index=0
    temp=0
    for y in list1:
        if y_index < len(list1):
            if list1[y_index]==string1:
                temp=temp+1
            y_index = y_index +1
    return temp


#num =Count_in(listy,stringy)
#print("num:",num)


candidate = []
short_can=[]


# Prompt user for video lookup
#video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if count > 0:
            candidate.append(row[2])
        count = count +1
        

short_can=unique(candidate)
temp = 0
x_index = 0
y_index = 0
votes = []


#for x in short_can:
 #   for y in candidate:
  #      if y_index < len(candidate):
   #         if candidate[y_index]==short_can[x_index]:
    #            temp=temp+1
     #       y_index = y_index +1
    #votes.append(temp)
    #print("x", x_index,"temp",temp)
    #print(votes)
    #temp=0
    #x_index=x_index+1

x_index=0
vote_count=[]

for x in short_can:
    ans=Count_in(candidate,short_can[x_index])
    x_index=x_index+1
    vote_count.append(ans)

x_index=0
vote_per =[]
for x in short_can:
    ans=vote_count[x_index]/count
    x_index=x_index+1
    vote_per.append(ans)

x_index=0
winner=short_can[0]
high_vote=vote_count[0]



for x in vote_count:
    if vote_count[x_index]>high_vote:
        high_vote=vote_count[x_index]
        winner=short_can[x_index]
    x_index=x_index+1
   




print("Total Votes:", count-1)

with
x_index=0
for x in short_can:
    print(short_can[x_index],"   ",vote_per[x_index],"%   ",vote_count[x_index])
    x_index=x_index+1





print("Winner:",winner)

output_file = os.path.join("output.csv")




