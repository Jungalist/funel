#!/bin/bash
scp -i /home/seb/.ssh/id_rsa $2 b3037306@10.9.16.167:data

name=$(basename $2 ".arff")

ssh -t -t -i /home/seb/.ssh/id_rsa b3037306@10.9.16.167 << HERE
 cd scripts/funel
 ./coprediction.sh $1 ~/data/$name.arff 2 2
 exit
HERE


