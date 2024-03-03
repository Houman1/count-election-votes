FROM ubuntu

# Update the package list
RUN apt-get update

# Install Python and pip
RUN apt-get install -y python3 python3-pip

RUN pip install \
        pytest \
        openpyxl

WORKDIR /ballot_reader
