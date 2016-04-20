#!/bin/bash
# $1 = name of project
# $2 = path to data file
# $3 = id of job in database

# $4 = setting 1-4
# $5 = permutations
# $6 = biohel runs
# $7 = attributes kept

#job name e.g. 1_001 instead of 1_001.arff
name=$(basename $2 ".arff")
rsa=/home/seb/.ssh/id_rsa
#linux=b3037306@linux.cs.ncl.ac.uk
hpc=b3037306@10.9.16.167


#Copy data to linux machine then into the hpc

#From home
#scp -i $rsa $2 $linux:data
#ssh -i $rsa $linux "scp /home/u13/b3037306/data/$name.arff $hpc:data/$name.arff"

#From campus
scp -i $rsa $2 $hpc:data/$name.arff



#ssh into HPC and run Funel using the data uploaded
#TODO allow user to change the parameters
# ssh -t -t -i $rsa $linux ssh $hpc << HERE
#  cd scripts/funel
#  ./coprediction.sh $1 ~/data/$name.arff $4 $7 $5 $6 
#  exit
# HERE

#From campus
ssh -t -t -i $rsa $hpc << HERE
 cd scripts/funel
 ./coprediction.sh $1 ~/data/$name.arff $4 $7 $5 $6 
 exit
HERE


#make a results directory on the server
mkdir /home/seb/project/funel/media/results/$name
result=media/results/$name

#copy result from HPC to Linux machine then to server

#From home
#ssh -i $rsa $linux "mkdir result/$name && scp $hpc:scripts/funel/results/$name/co-prediction_network.txt /home/u13/b3037306/result/$name/co-prediction.txt"
#ssh -i $rsa $linux "scp $hpc:scripts/funel/results/$name/results/statistical_test.dat /home/u13/b3037306/result/$name/statistical_test.dat"
#ssh -i $rsa $linux "scp $hpc:scripts/funel/results/$name/results/scores.dat /home/u13/b3037306/result/$name/scores.dat"

# scp -i $rsa $linux:result/$name/co-prediction.txt $result/co-prediction.txt
# scp -i $rsa $linux:result/$name/statistical_test.dat $result/statistical_test.dat
# scp -i $rsa $linux:result/$name/scores.dat $result/scores.dat

#From campus/cruncher
scp -i $rsa $hpc:scripts/funel/results/$name/co-prediction_network.txt $result/co-prediction.txt
scp -i $rsa $hpc:scripts/funel/results/$name/results/statistical_test.dat $result/statistical_test.dat
scp -i $rsa $hpc:scripts/funel/results/$name/results/scores.dat $result/scores.dat



