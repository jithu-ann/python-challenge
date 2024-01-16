import os
import csv

PyBankcsv = os.path.join("Resources","budget_data.csv")

#storing the data

profit = []
Monthly_Changes = []
date=[]

 #variable initialisation

count=0
TotalProfit=0
total_change_profits =0
InitialProfit =0

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)


    for row in csvreader:    
  
      count = count + 1 

  
      date.append(row[0])
#append the profit
      profit.append(row[1])
      TotalProfit = TotalProfit + int(row[1])
      total_months=len(date)
      
      final_profit = int(row[1])
      monthly_change_profits = final_profit - InitialProfit
      Monthly_Changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      InitialProfit = final_profit

      #couldnt get the exact value of Average Change by using the below code as it shows some error. so make it as a comment
       
      #for x in range(1, len(profit)):
       # Monthly_Changes.append((int(profit[x])-int(profit[x-1])))
      #average_change_profit=sum(Monthly_Changes)/len(Monthly_Changes)
      #average_change_profits=round(average_change_profit,2)


      average_change_profits=(total_change_profits/count)

    #maximum and minimum profit and the dates
      GreatestIncrease_profit = max(Monthly_Changes)
      GreatestDecrease_profit = min(Monthly_Changes)

      date_increase =date[Monthly_Changes.index(GreatestIncrease_profit)]
      date_decrease = date[Monthly_Changes.index(GreatestDecrease_profit)]
      
         
    
    print("Financial Analysis")
    print("-------------------------------------------------")
    print("Total Months:" + str(count))
    print("Total Profits: " + "$" + str(TotalProfit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(date_increase) + " ($" + str(GreatestIncrease_profit) + ")")
    print("Greatest Decrease in Profits: " + str(date_decrease) + " ($" + str(GreatestDecrease_profit) + ")")
  
OutputFile=os.path.join('.','Analysis','Analysis.txt')
with open(OutputFile,"w") as text:
    text.write(" Financial Analysis"+ "\n")
    text.write("-----------------------------------------------------\n")
    text.write("Total Months:" + str(count)+"\n")
    text.write("Total Profits: " + "$" + str(TotalProfit)+"\n")
    text.write("Average Change: " + "$" + str(int(average_change_profits))+"\n")
    text.write("Greatest Increase in Profits: " + str(date_increase) + " ($" + str(GreatestIncrease_profit) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(date_decrease) + " ($" + str(GreatestDecrease_profit) + ")\n")