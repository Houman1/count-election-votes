import os
import ballot_reader
import logging

# logger = logging.Logger("main app")
logger = logging.getLogger("main app")
logging.basicConfig(level = logging.INFO)

ballot_reader = ballot_reader.Ballot_Reader

ballot_folder = r"C:\Users\Houmqn\Desktop\counted_samples"


# List all files in the directory
files = os.listdir(ballot_folder)


for file in files:
    # Create the full file path
    file_path = os.path.join(ballot_folder, file)
    
    # Check if it is a file (not a subdirectory)
    if os.path.isfile(file_path):

        logger.info(file)
        logger.info(file_path)
        ballot_read, ballot_workbook = ballot_reader.read_in_ballot(file_path)
        column_data = ballot_reader.read_columns(ballot_read)
        cleaned_data = ballot_reader.clean_up_data(column_data)
        counted_votes = ballot_reader.count_votes(ballot_workbook, cleaned_data)
        ballot_reader.sort_counted_and_spoiled_ballots(counted_votes, ballot_read, ballot_folder, expected_number_of_votes = 1)