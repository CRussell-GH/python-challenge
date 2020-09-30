#PyBank

# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set vars to 0 or empty
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

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through to count months and create lists
    for row in csvreader:
        #print(month_count)
        if month_count >0: 
            if month_count == 1:
                last = 0
            change=float(row[1])-last
            changes_list.append(change)
            change_month.append(row[0])
            last = float(row[1])

            profit_loss_total =  profit_loss_total + int(row[1]) #+ profit_loss_total
            
        month_count = month_count +1

    #set vars to 0 or empty    
    list_for_ave = []
    diff = 0
    change_total=0

    #loop to total changes and find max and mins
    for i in range(len(changes_list)):
        if i == 0:
           last = 0
        if i > 0: 
            diff=changes_list[i]-last
            change_total=change_total+changes_list[i]
            list_for_ave.append(diff)
            last=changes_list[i]
        
        if int(changes_list[i]) > max_increase:
            max_increase = int(changes_list[i])
            max_index = i
           
        if int(changes_list[i]) < max_decrease:
            max_decrease = int(changes_list[i])
            min_index = i
            
    

#Discount header row
month_count = month_count - 1

#print results
print("Financial Analysis")
print("------------------")
print("Total Months:", month_count)
print("Total:", profit_loss_total)
print("Average Change:", change_total/(month_count-1))
print("Greatest Increase in Profts:", change_month[max_index], " ", max_increase)
print("Greatest Decrease in Profts:", change_month[min_index], " ", max_decrease)

# Set path for file
txtpath = os.path.join("Analysis", "budget_data.txt")

# Open the text file
with open(txtpath,"w") as txtfile:
    #write results to text file
    txtfile.write("Financial Analysis \n")
    txtfile.write("---------------- \n")

    txtfile.write("Total Months: ")
    txtfile.write(str(month_count))
    txtfile.write(" \n")

    txtfile.write("Total: ")
    txtfile.write(str(profit_loss_total))
    txtfile.write(" \n")

    txtfile.write("Average Change: ")
    txtfile.write(str(change_total/(month_count-1)))
    txtfile.write(" \n")

    txtfile.write("Greatest Increase in Profts: ")
    txtfile.write(str(change_month[max_index]))
    txtfile.write(" ")
    txtfile.write(str(max_increase))
    txtfile.write(" \n")

    txtfile.write("Greatest Decrease in Profts: ")
    txtfile.write(str(change_month[min_index]))
    txtfile.write(" ")
    txtfile.write(str(max_decrease))
    txtfile.write(" \n")
