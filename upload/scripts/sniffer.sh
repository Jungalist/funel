#!/bin/bash


qstatOutput=`qstat | wc -l`

while [ $qstatOutput -gt 0 ]
do
     echo Not yet
     sleep 5
     qstatOutput=`qstat | wc -l`
done

echo Finished!
