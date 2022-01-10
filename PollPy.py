#import packages
import csv
import os
#assign variable for file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#create filename variable
file_to_save = os.path.join("analysis","election_analysis.txt")
#create a variable to hold total votes and set it equal to 0
total_votes = 0
#create a list for candidates
candidate_options = []
#create a dictionary for votes for each candidate
candidate_votes = {}
#Create variables to track the winner and winning votes
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#open election results and read file
with open(file_to_load) as election_data:
    #To do: read and analyze data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #print the headers
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV file
    for row in file_reader:
        #Add up total votes
        total_votes = total_votes + 1
        #Print Candidate name for each row
        candidate_name = row[2]
        #If candidate is not already in list
        if candidate_name not in candidate_options:
            #add to list of candidates
            candidate_options.append(candidate_name)
            #begin tracking vote count
            candidate_votes[candidate_name] = 0
        #Add vote to that candidate's count
        candidate_votes[candidate_name] += 1
#Save the results to our text file
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)
    #Print the total number of votes
    #print(total_votes)
    #Print the candidate list
    #print(candidate_options)
    #print candidate vote dictionary
    #print(candidate_votes)
    #Determine precentage of votes each candidate won with a for loop
    for candidate_name in candidate_votes:
        #Retrieve vote count
        votes = candidate_votes[candidate_name]
        #Calculate percentrage of votes
        vote_percentage = float(votes)/float(total_votes) * 100
        #Save candidate results to a variable
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
         #Print each candidate, the vote count, and percentage to terminal
        print(candidate_results)
        #save to the text file
        txt_file.write(candidate_results)
        #determine winning vote count and candidate
        #determine if the votes are greater than the winning count
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            #If true make votes=winning votes and vote_percentrage=winning_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set winning_candidate equal to candidates name
            winning_candidate = candidate_name
   
    #Print winning candidate summary to terminal
    winning_candidate_summary = (
            f"-------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"--------------------\n")
    print(winning_candidate_summary)
    #Save winning candidate summary to text file
    txt_file.write(winning_candidate_summary)
        
#use open statement
#with open(file_to_save, "w") as txt_file:
    #Write something
    #txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")

#percentage of votes each candidate won
#winnder of election by popular vote
