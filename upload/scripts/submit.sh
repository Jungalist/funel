#!/bin/bash
# $1 = name of project
# $2 = name of path to data file
# $3 = id of job in database

#job name e.g. 1_001 instead of 1_001.arff
name=$(basename $2 ".arff")

#Copy data to linux machine then into the hpc
scp -i /home/seb/.ssh/id_rsa $2 b3037306@linux.cs.ncl.ac.uk:data
ssh -i /home/seb/.ssh/id_rsa b3037306@linux.cs.ncl.ac.uk "scp /home/u13/b3037306/data/$name.arff b3037306@10.9.16.167:data/$name.arff"

#ssh into HPC and run Funel using the data uploaded
#TODO allow user to change the parameters
ssh -t -t -i /home/seb/.ssh/id_rsa b3037306@linux.cs.ncl.ac.uk ssh b3037306@10.9.16.167 << HERE
 cd scripts/funel
 ./coprediction.sh $1 ~/data/$name.arff 1 100
 exit
HERE

#make a results directory on the server
mkdir /home/seb/project/djangoservice/media/results/$name
result=media/results/$name/co-prediction.txt

#copy result from HPC to Linux machine then to server
ssh -i /home/seb/.ssh/id_rsa b3037306@linux.cs.ncl.ac.uk "mkdir result/$name && scp b3037306@10.9.16.167:scripts/funel/results/$name/co-prediction_network.txt /home/u13/b3037306/result/$name/co-prediction.txt"
ssh -i /home/seb/.ssh/id_rsa b3037306@linux.cs.ncl.ac.uk "scp b3037306@10.9.16.167:scripts/funel/results/$name/results/statistical_test.dat /home/u13/b3037306/result/$name/statistical_test.dat"
ssh -i /home/seb/.ssh/id_rsa b3037306@linux.cs.ncl.ac.uk "scp b3037306@10.9.16.167:scripts/funel/results/$name/results/scores.dat /home/u13/b3037306/result/$name/scores.dat"

scp -i /home/seb/.ssh/id_rsa b3037306@linux.cs.ncl.ac.uk:result/$name/co-prediction.txt $result
scp -i /home/seb/.ssh/id_rsa b3037306@linux.cs.ncl.ac.uk:result/$name/statistical_test.dat media/results/$name/statistical_test.dat
scp -i /home/seb/.ssh/id_rsa b3037306@linux.cs.ncl.ac.uk:result/$name/scores.dat media/results/$name/scores.dat

