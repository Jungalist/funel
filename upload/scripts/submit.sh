#!/bin/bash
scp -i /home/seb/.ssh/id_rsa $1 b3037306@10.9.16.167:data
#$ -cwd
#$ -V
#$ -l h_rt=07:59:59
#$ -l h_vmem=1G

name=$(basename $1 ".arff")

ssh -t -t -i /home/seb/.ssh/id_rsa b3037306@10.9.16.167 << HERE
 qsub scripts/dummy.sh $name
 bash scripts/sniffer.sh
 #if job completed, run next one
 #echo "An error has occured. Cannot submit job to HPC"
 exit
HERE


