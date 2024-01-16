import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

election_data = os.path.join('.', 'Resources', 'election_data.csv')

count={}

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)

#creates a dictionary counting votes for each candidate
    for row in csvreader:
        count[row[2]] = count.get(row[2], 0) + 1

#adds all the values in the dictionary to calculate total votes
    TotalVotes = sum(count.values())

#finds the candidate with the most number of votes and saves the key
    winner = max(count, key=count.get)

    #prints out all results
    print("Election Results")
    print("--------------------------")
    print(f'Total Votes: {TotalVotes}')
    print("--------------------------")
    for key, value in count.items():
        print(f'{key}: {round((value/TotalVotes)* 100, 2)}% ({value})')
    print("-----------------------------")
    print(f'Winner: {winner}')
    print("-----------------------------------")

#create an output file
OutputFile = os.path.join('.', 'Resources', 'Analysis.txt')

with open(OutputFile, "w") as text:
    text.write("Election Results\n")
    text.write("----------------------\n")
    text.write(f'Total Votes: {TotalVotes}\n')
    text.write("--------------------------\n")
    for key, value in count.items():
               text.write(f'{key}:{round((value/TotalVotes)*100,2)}%({value})\n')
    text.write("------------------------------\n")
    text.write(f'Winner: {winner}\n')
    text.write("---------------------------------\n")
    