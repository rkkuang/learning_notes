#!/bin/bash

# positional parameter

echo "1st Argument : $1"
sum=0
while [[ $# -gt 0 ]];do
	num=$1
	sum=$((sum+num))
	shift
done

echo "Sum: $sum"
#./bash_pos_para.sh 3 4 1 43 1 2323  2 2 121 21 21 21 2 1 2 1
