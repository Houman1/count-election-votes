# docker exec -it -v C:\Users\houma\PycharmProjects\CountElectionVotes:/ballot_reader --name ballot_counter ubuntu:latest

docker build -f Dockerfile -t ballot_reader:dev .
docker run -it -v /mnt/c/Users/houma/PycharmProjects/CountElectionVotes:/ballot_reader --name ballot_counter ballot_reader:dev

