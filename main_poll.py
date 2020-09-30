

#PyPoll


# Modules
import os
import csv




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


# function to count the times a string is in a list
def Count_in(list1,string1):
    y_index=0
    temp=0
    for y in list1:
        if y_index < len(list1):
            if list1[y_index]==string1:
                temp=temp+1
            y_index = y_index +1
    return temp


# Set vars to 0 or empty
count = 0
candidate = []
short_can=[]

temp = 0
x_index = 0
y_index = 0
votes = []
vote_per =[]
x_index=0
vote_count=[]
winner=""


# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through to count and to create list of candidates
    for row in csvreader:
        if count > 0:
            candidate.append(row[2])
        count = count +1
        
#call function to create a list of unique candidates
short_can=unique(candidate)

# loop to count the votes for each candidate
for x in short_can:
    ans=Count_in(candidate,short_can[x_index])
    x_index=x_index+1
    vote_count.append(ans)

#reset index for loop
x_index=0

# loop to create a list of percentages
for x in short_can:
    ans=vote_count[x_index]/count
    x_index=x_index+1
    vote_per.append(ans)

#reset index for loop
x_index=0
# set vars for winner calculation
print(short_can)

#set vars to calculate winner
winner=short_can[0]
high_vote=vote_count[0]

#loop to calculate the winner
for x in vote_count:
    if vote_count[x_index]>high_vote:
        high_vote=vote_count[x_index]
        winner=short_can[x_index]
    x_index=x_index+1
   
#print results
print("Election Results")
print("----------------")
print("Total Votes:", count-1)

#reset index for loop
x_index=0

#loop through to print out results
for x in short_can:
    print(short_can[x_index],"   ",vote_per[x_index],"%   ",vote_count[x_index])
    x_index=x_index+1

print("Winner:",winner)

# Set path for file
txtpath = os.path.join("Analysis", "election_data.txt")

# Open the text file
with open(txtpath,"w") as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("---------------- \n")

    #reset index for looping
    x_index=0
    #loop to write to text file
    for x in short_can:
        txtfile.write(short_can[x_index])
        txtfile.write("    ")
        txtfile.write(str(vote_per[x_index]))
        txtfile.write("%    ")
        txtfile.write(short_can[x_index])
        txtfile.write("    ")
        txtfile.write(str(vote_count[x_index]))
        txtfile.write(" \n")
        x_index=x_index+1
    
    txtfile.write("Winner: ")
    txtfile.write(winner)






