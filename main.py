import os
import ballot_reader
import converter
import logging


logger = logging.getLogger("main app")
logging.basicConfig(level = logging.INFO)

ballot_reader = ballot_reader.Ballot_Reader
format_converter = converter.Converter 

by_election_ballot_folder = r"C:\Users\Houmqn\Desktop\sample-ballots-by-election"
ridvan_ballot_folder_with_old_formats = r"C:\Users\Houmqn\Desktop\sample-ballots-ridvan"
ridvan_ballot_folder_without_old_formats = r"C:\Users\Houmqn\Desktop\sample-ballots-ridvan-without-old-formats"

old_format_file = r"C:\Users\Houmqn\Desktop\conversion_test"

ballot_folder = old_format_file
expected_number_of_votes = 9

# List all files in the directory
files = os.listdir(ballot_folder)

number_of_ballots = 0
number_of_incompatible_files = 0
all_votes = []

for file in files:

    # Create the full file path
    file_path = os.path.join(ballot_folder, file)

    # Check if it is a file (not a subdirectory)
    if os.path.isfile(file_path) and (file_path.endswith('.xlsx') or file_path.endswith('.xls')):
        
        number_of_ballots += 1

        is_file_compatible = file_path.endswith('.xlsx')

        if is_file_compatible:
            cleaned_data, ballot_workbook = ballot_reader.read_in_ballot(file_path)
            sorted_votes = ballot_reader.sort_votes(ballot_workbook, cleaned_data, expected_number_of_votes, file_path, ballot_folder)
            
            if sorted_votes:
                all_votes.append(sorted_votes[0])
        else:
            number_of_incompatible_files += 1


logger.info(f"Number of ballots: {number_of_ballots}")
logger.warning(f"{number_of_incompatible_files} incompatible files not counted")

counted_votes = ballot_reader.count_votes(all_votes)
