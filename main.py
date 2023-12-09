import os
import ballot_reader
import logging

# logger = logging.Logger("main app")
logger = logging.getLogger("main app")
logging.basicConfig(level = logging.INFO)

ballot_reader = ballot_reader.Ballot_Reader

by_election_ballot_folder = r"C:\Users\Houmqn\Desktop\sample-ballots-by-election"
ridvan_ballot_folder_with_old_formats = r"C:\Users\Houmqn\Desktop\sample-ballots-ridvan"
ridvan_ballot_folder_without_old_formats = r"C:\Users\Houmqn\Desktop\sample-ballots-ridvan-without-old-formats"

ballot_folder = ridvan_ballot_folder_without_old_formats
expected_number_of_votes = 9

# List all files in the directory
files = os.listdir(ballot_folder)

number_of_ballots = len(files)
all_votes = []

for file in files:
    # Create the full file path
    file_path = os.path.join(ballot_folder, file)
    
    # Check if it is a file (not a subdirectory)
    if os.path.isfile(file_path):

        logger.info(f"FILE: {file}")
        logger.info(f"FILE PATH: {file_path}")

        cleaned_data, ballot_workbook = ballot_reader.read_in_ballot(file_path)
        sorted_votes = ballot_reader.sort_votes(ballot_workbook, cleaned_data, expected_number_of_votes, file_path, ballot_folder)
        
        if sorted_votes:
            all_votes.append(sorted_votes[0])
        
counted_votes = ballot_reader.count_votes(all_votes)

logger.info(f"Number of ballots: {number_of_ballots}")