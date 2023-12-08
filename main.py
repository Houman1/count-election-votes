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

ballot_folder = by_election_ballot_folder

# List all files in the directory
files = os.listdir(ballot_folder)

number_of_ballots = len(files)
expected_number_of_votes = 1
all_votes = []

for file in files:
    # Create the full file path
    file_path = os.path.join(ballot_folder, file)
    
    # Check if it is a file (not a subdirectory)
    if os.path.isfile(file_path):

        logger.info(f"FILE: {file}")
        logger.info(f"FILE PATH: {file_path}")
        ballot_read, ballot_workbook = ballot_reader.read_in_ballot(file_path)
        column_data = ballot_reader.read_columns(ballot_read)
        cleaned_data = ballot_reader.clean_up_data(column_data)
        sorted_votes = ballot_reader.sort_votes(ballot_workbook, cleaned_data, expected_number_of_votes)
        format_votes_list = ballot_reader.format_votes_list(sorted_votes)
        all_votes.append(format_votes_list)

    
print(f"ALL VOTES: {all_votes}")
print(f"Number of ballots: {number_of_ballots}")
# ballot_reader.sort_counted_and_spoiled_ballots(counted_votes, ballot_read, ballot_folder, expected_number_of_votes)
