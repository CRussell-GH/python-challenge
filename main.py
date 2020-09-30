

# Modules
import os
import csv
import re

# Prompt user for video lookup
#video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")


# ------------------------------------------
# Set count to 0
month_count = 0
profit_loss_total = 0
changes_list = []
profit_list = []
average_change = 0
max_increase = 0
max_decrease = 0
Inc_month = ""
Dec_month = ""
temp_str = ""
last = 0
change_month = []
max_index = 0
min_index = 9999999

def Ave(the_list):
    return sum(the_list) / len(the_list)




# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #a = csvreader{}[1]
    #print(a)


    # Loop through looking for the video
    for row in csvreader:
        #print(month_count)
        if month_count >0: 
            if month_count == 1:
                last = 0
            change=float(row[1])-last
            changes_list.append(change)
            change_month.append(row[0])
            last = float(row[1])


            
            #if int(row[1]) > max_increase:
             #   max_increase = int(row[1])
              #  print(row[1])

            #float("-5")
            #print(row[1])

            #profit_list[month_count]=row[1]

            # s = len(row[1])

            #s = re.sub(r'[^\x00-\x7F]+','-', s)

            #s = float(s)
            #print(row[1])

            profit_loss_total =  profit_loss_total + int(row[1]) #+ profit_loss_total
            #int(row[1])
            #temp_str = row[1].split(" ")
            #float(temp_str[0])
            #int("-2345343")
            #print(temp_str)
        month_count = month_count +1
        #profit_loss_total = profit_loss_total + row[int(1)]
    list_for_ave = []
    diff = 0
    #print(changes_list)
    change_total=0
    for i in range(len(changes_list)):
        #print(changes_list[i])
        
        if i == 0:
           last = 0
        if i > 0: 
            diff=changes_list[i]-last
            #print("diff",diff, "changes", changes_list[i],"old last", last)
            print(changes_list[i])
            change_total=change_total+changes_list[i]

            list_for_ave.append(diff)
            last=changes_list[i]
            #print("diff",diff, "new last", last)


        


        if int(changes_list[i]) > max_increase:
            max_increase = int(changes_list[i])
            max_index = i
           # print(changes_list[i])
        if int(changes_list[i]) < max_decrease:
            max_decrease = int(changes_list[i])
            min_index = i
            #print(changes_list[i])
        #list_for_ave[]

    

#Ave(changes_list)
#Subtract out the header row
print("Sum",sum(list_for_ave))
print("Len",len(list_for_ave))

print("CH",sum(changes_list))


month_count = month_count - 1
print(change_total)
print(month_count-1)
#print(list_for_ave)
print("Total Months:", month_count)
print("Total:", profit_loss_total)
print("Average Change:", change_total/(month_count-1))
print("Greatest Increase in Profts:", change_month[max_index], " ", max_increase)
print("Greatest Decrease in Profts:", change_month[min_index], " ", max_decrease)

#temp_list = [5,-15,15]
#print("Average List:", Ave(temp_list))

#print(change_month[max_index])

    # If the video is never found, alert the user
   # if found is False:
    #    print("Sorry about this, we don't seem to have what you are looking for!")
