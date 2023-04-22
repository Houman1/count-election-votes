import openpyxl
import shutil

#path to ballts (xlsx files)
path_to_ballots = r"C:/Users/houma/PycharmProjects/CountElectionVotes/Sample Votes/"
# file = "345t64.xlsx"
file = "33333.xlsx"
ballot = path_to_ballots + file


def read_in_ballot(ballot_file):

    # Load the workbook
    workbook = openpyxl.load_workbook(ballot)

    # Select the active worksheet
    worksheet = workbook.active

    # Get all columns into one list
    all_columns = []
    for row in worksheet.values:
        trimmed_row = []
        for value in row:
            if value is not None:
                print(value)
                trimmed_row.append(value)
        all_columns.append(trimmed_row)


    #remove empty values
    all_values = []
    for entry in all_columns:
        if len(entry) > 0:
            all_values.append(entry)

    # Print all columns as one list
    print(all_columns)
    print(all_values)

    #Select votes
    vote_list = [value for value in all_values if len(value) > 3]

    votes_only = []
    for i in vote_list:
        if 'x' in i:
            votes_only.append(i)

    for vote in votes_only:
        print(vote)

    # Close the workbook
    workbook.close()

    #Check ballot is valid
    if len(votes_only) == 9:
        print(f"vote is valid")
        return votes_only
    else:
        print(f"invalid vote")
        dst = r'C:\Users\houma\PycharmProjects\CountElectionVotes\spoiled-ballots'

        # use the shutil.move() function to move the file
        shutil.move(ballot_file, dst)


read_in_ballot(ballot)
