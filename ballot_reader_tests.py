import pytest
import glob
from ballot_reader import Ballot_Reader

test_ballots = glob.glob("ballot_reader_tests_data/*")

# print(files)

br = Ballot_Reader

def test_ballot_read():
    # assert func(3) == 5

    for ballot in test_ballots:
        assert br.read_in_ballot(ballot) != None

    
def test_ballot_sort():


    for ballot in test_ballots:
        cleaned_data, ballot_workbook = ballot_reader.read_in_ballot(ballot)


def test_ballot_count():
    pass