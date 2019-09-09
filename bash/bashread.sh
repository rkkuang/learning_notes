#!/bin/bash

read -p "What is your name? " name
echo "Hello $name"
read -p "How old are you? " age
## >= 16
if [ $age -ge 16 ]
then
	echo "You can dirve"
elif [ $age -eq 15 ]
then
	echo "You can drive next year"
else
	echo "You can't drive"
fi

read -p "Enter a number : " num
if ((num == 10)); then
	echo "Your number equals 10"
fi

if ((num > 10)); then
	echo "It is greater than 10"
else
	echo "It is not greater than 10"
fi

if (( ((num % 2)) == 0)); then
	echo "It is even"
else
	echo "It is old"
fi

if (( ((num>0)) && ((num<11)) ));then
	echo "$num is between 1 and 10"
fi

touch samp_file && vim samp_file
[ -d samp_dir ] || mkdir samp_dir
ls

read -p "Do you want to delete these samp files (y/n): " ifdel
if (( ifdel == "y"  ));then
	rm samp_file
	rm -r samp_dir
fi

























