# election_analysis
Analysis of election results for colorado districts
##Project Overview
The following tasks were given by a Colorado Board of Elections employee. These tasks were designed to complete the audit of a recent local congressional election

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the toatl number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data source: election_results.csv
- Software: Python 3.10.1, Visual Studio Code, 1.63.2

## Summary
The analysis of the eleciton show that:
- There were 369,711 votes cast in the elction
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
 - The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85213 total number of votes.
    - Diana DeGette received 73.8% of the vote and 272892 total number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11606 total number of votes.

## Challenge Overview

# Overview of Election Audit
The purpose of this analysis of the election audit is to calculate total votes, who received votes, and how many votes that person received. In addition, total votes by county were also calculated. This analysis allows us to see who won the election and by what percentage of the total vote.


# Election-Audit Results

- How many votes were cast in this congressional election?
  - 369,711 votes were cast in this congressional election.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Jefferson County recorded 38,855 votes, which was 10.5% of the total votes.
  - Arapahoe County recorded 306,05 votes, which was 82.8% of the total votes.
  - Denver County recorded 24,801 votes, which was 6.7% of the total vote.
- Which county had the largest number of votes?
  - County had the largest number of votes
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Casper Stockham received 23.0% of the vote and 85213 total number of votes.
  - Diana DeGette received 73.8% of the vote and 272892 total number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11606 total number of votes.
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Diana DeGette won the election with 272,892 total votes, which was 73.8% of the total vote.

## Challenge Summary
While this script was used to audit the results of a single Colorado district election, the script can be modified to analyze most other elections. Since the script finds the unique values of candidates who received votes, an election with several candidates can be analyzed using this script. Moreover, the county portion of the script can be modified for districts, states, or other census-designated areas. This script could be used to audit a mayoral election or a gubernatorial election. In addition, it could be modified to calculate results for propositions. This script may have trouble with write-in candidates if two different people write in the same candidate but with a differnt spelling or a different syntax.
![Fig1_challenge](https://user-images.githubusercontent.com/95397823/150704497-e115870e-db99-43eb-905d-bdb62e917e36.PNG)
Fig.1 shows how the candidate list and the county list in generated. This code allows for any number of candidates to receive votes in an election. A problem may arise if a write-in candidate is written differently by two different voters. (ie. using a nickname verus using the candidate's full name).
