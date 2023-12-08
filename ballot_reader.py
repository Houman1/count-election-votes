from pathlib import Path
import os
import openpyxl
import shutil
import logging

logger = logging.getLogger("ballot_reader")
logging.basicConfig(level = logging.INFO)
# logger = logging.Logger("ballot_reader")

class Ballot_Reader():

    def read_in_ballot(ballot):

        # Load the workbook
        workbook = openpyxl.load_workbook(ballot)
        logger.info("Loading in ballot")
        # Select the active worksheet
        worksheet = workbook.active

        return worksheet, workbook

    def read_columns(worksheet):
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


    def clean_up_data(all_columns):
        #remove empty values
        all_values = []
        for entry in all_columns:
            if len(entry) > 0:
                all_values.append(entry)

        # Print all columns as one list
        return all_values


    def sort_votes(workbook, all_values, expected_number_of_votes):

        #Count votes
        vote_list = [value for value in all_values if len(value) > 3]
        del vote_list[0]
        # print(f" VOTE LIST: {vote_list}")
        votes = []
        for vote in vote_list:
            if 'x' or 'X' in vote:
                votes.append(vote)

        number_of_votes = len(votes)
        logger.info(f"number of votes: {number_of_votes}")

        if not number_of_votes == expected_number_of_votes:
            logger.warn(f"number of votes: {number_of_votes}, doesn't match expected number of votes: {expected_number_of_votes}")

        # Close the workbook
        workbook.close()

        return votes
    
    def format_votes_list(votes):

        formatted_votes = []
        for vote in votes:
            formatted_votes.append(" ".join(vote[:-1]).lower())

        print(f"FORMATTED VOTES: {formatted_votes}")  
        return formatted_votes          

    def sort_counted_and_spoiled_ballots(votes, ballot, ballot_folder, expected_number_of_votes = 9 ):
        '''add checks for by-election vs regular, allow choice of how many people to expect to see if the vote is valid
        also create new directories one for counted and one for spoiled.'''
        #Check ballot is valid
        number_of_votes = len(votes)
        if number_of_votes == expected_number_of_votes:
            logger.info(f"vote is valid")
        #     dst_counted = os.path.join(ballot_folder, "counted-ballots")
        #     # use the shutil.move() function to move the file
        #     shutil.move(str(ballot), dst_counted)
        #     return votes
        else:
            logger.warn(f"invalid vote")
            logger.info(f"expected {expected_number_of_votes} votes, actually have: {number_of_votes}")
        #     dst_invalid = os.path.join(ballot_folder, "invalid-ballots")
        #     # dst = r'C:/Users/houma/PycharmProjects/CountElectionVotes/spoiled-ballots'

        #     # use the shutil.move() function to move the file
        #     shutil.move(str(ballot), dst_invalid)
        # return