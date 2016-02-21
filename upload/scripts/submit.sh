#!/bin/bash
scp -i /home/seb/.ssh/id_rsa $1 b3037306@cs-hpcgateway-mgmt.ncl.ac.uk:results
#SCP into the HPC with the RSA ID and submit the file that has been submitted to the server ready for Funel

#Run the qsub, run the sniffer
ssh -i /home/seb/.ssh/id_rsa b3037306@cs-hpcgateway-mgmt.ncl.ac.uk

#Wrapper



