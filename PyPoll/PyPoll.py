import os
import csv
election_csv = os.path.join("Resources", "election_data.csv")

candidate_names = []
total_votes = []
vote_percentages = []

with open(election_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    candidates = {}

    for row in csvreader:
        candidate = row[2]

        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

    total_vote_count = sum(candidates.values())
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {total_vote_count}')
    print(f'-------------------------')

    for candidate, vote_count in candidates.items():
        vote_percentage = round(((vote_count / total_vote_count) * 100),3)
       
        candidate_names.append(candidate)
        total_votes.append(vote_count)
        vote_percentages.append(vote_percentage)

for i in range(len(candidate_names)):
    print(f'{candidate_names[i]}: {vote_percentages[i]}% ({total_votes[i]})')

winner = max(candidates, key=candidates.get)
print(f'-------------------------')
print(f"Winner: {winner}")
print(f'-------------------------')

output = (f'\n'
f'Election Results\n'
f'-------------------------\n'
f'Total Votes: {total_votes}\n'
f'-------------------------\n'
f'{candidate_names[0]}: {vote_percentages[0]}% ({total_votes[0]})\n'
f'{candidate_names[1]}: {vote_percentages[1]}% ({total_votes[1]})\n'
f'{candidate_names[2]}: {vote_percentages[2]}% ({total_votes[2]})\n'
f'-------------------------\n'
f'Winner: {winner}\n')

output_file = os.path.join("poll_final.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(output)

#Sited Peer Collaboration with Juliet Hamilton, Adam Gostinger and Ryan Himes