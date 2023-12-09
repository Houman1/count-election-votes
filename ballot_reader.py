from pathlib import Path
import os
import openpyxl
import shutil
import logging
from collections import Counter

logger = logging.getLogger("ballot_reader")
logging.basicConfig(level = logging.INFO)
# logger = logging.Logger("ballot_reader")


class Ballot_Reader():


    def read_in_ballot(ballot):

        # Load the workbook
        workbook = openpyxl.load_workbook(ballot)
        logger.info("Reading in ballot")
        # Select the active worksheet
        worksheet = workbook.active

        read_columns = Ballot_Reader._read_columns(worksheet)
        clean_data = Ballot_Reader._remove_empty_values(read_columns)

        return clean_data, workbook



    def sort_votes(workbook, all_values, expected_number_of_votes, file_path, ballot_folder):

        #This checks for the entries that have an "x" in the 4th column, which are the votes.
        vote_list = [value for value in all_values if len(value) > 3]
        del vote_list[0]

        votes = []
        for vote in vote_list:
            if 'x' or 'X' in vote:
                votes.append(vote)

        number_of_votes = len(votes)

        logger.info(f"number of votes: {number_of_votes}")

        # Close the workbook
        workbook.close()

        if number_of_votes != expected_number_of_votes:
            logger.warn(f"number of votes: {number_of_votes}, doesn't match expected number of votes: {expected_number_of_votes}")
           
            #Sort spoiled votes
            Ballot_Reader._sort_spoiled_ballots(file_path, ballot_folder)

        else:
            #format the vote entries
            formatted_votes = Ballot_Reader._format_votes_list(votes)
            Ballot_Reader._sort_valid_ballot(file_path, ballot_folder)

            return formatted_votes

        return



    def count_votes(all_votes):

        vote_counts = Counter(all_votes)

        logger.info(f"Results: {vote_counts}")




    #Private methods
    def _read_columns(worksheet):
        # Get all columns into one list
        all_columns = []
        for row in worksheet.values:
            trimmed_row = []
            for value in row:
                if value is not None:
                    # logger.info(value)
                    trimmed_row.append(value)
            all_columns.append(trimmed_row)

        return all_columns


    def _remove_empty_values(all_columns):
        
        #remove empty values
        all_values = []
        for entry in all_columns:
            if len(entry) > 0:
                all_values.append(entry)

        return all_values


    def _format_votes_list(votes):
        '''Combine all the list entries into a single string and make them all lower case. '''

        formatted_votes = []
        for vote in votes:
            format_vote = " ".join(vote[:-1]).lower()
            formatted_votes.append(format_vote)

        logger.info(f"formatted votes: {formatted_votes}")  
        sorted(formatted_votes)
        
        return formatted_votes



    def _sort_spoiled_ballots(file_path, ballot_folder):
        '''move a spoiled ballot into a spoiled_ballots directory'''

        logger.warn(f"Spoiled ballot: {file_path}")

        spoiled_ballot_directory = os.path.join(ballot_folder, "spoiled_ballots")

        if not os.path.exists(spoiled_ballot_directory):
            os.makedirs(spoiled_ballot_directory)

        shutil.move(str(file_path), spoiled_ballot_directory)

        return
    

    def _sort_valid_ballot(file_path, ballot_folder):
        '''move a valid ballot into a counted_ballots directory'''

        counted_valid_ballot_directory = os.path.join(ballot_folder, "counted_valid_ballots")

        if not os.path.exists(counted_valid_ballot_directory):
            os.makedirs(counted_valid_ballot_directory)

        shutil.move(str(file_path), counted_valid_ballot_directory)

        return