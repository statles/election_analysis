#import packages
import csv
import os
#assign variable for file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#create filename variable
file_to_save = os.path.join("analysis","election_analysis.txt")
#open election results and read file
with open(file_to_load) as election_data:
    #To do: read and analyze data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #print the headers
    headers = next(file_reader)
    print(headers)
#use open statement
with open(file_to_save, "w") as txt_file:
    #Write something
    txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")
#Total number of votes cast
#complete list of candidates who recieved votes
#percentage of votes each candidate won
#total number of votes each candidate won
#winnder of election by popular vote
