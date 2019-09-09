#!/bin/bash
#regular expressions

read -p "Validate Date : " date
#e.g. 20190909
pat="^[0-9]{8}$"

if [[ $date =~ $pat ]];then
	echo "$date is valid"
else
	echo "$date is not valid"
fi


read -p "Enter 2 Numbers to sum : " num1 num2
sum=$((num1+num2))
echo "$num1 + $num2 = $sum"

read -sp "Enter the secret code: " secret
if [ "$secret" == "pswd" ];then
	echo "Enter"
else
	echo "Wrong password"
fi

OIFS="$IFS"
IFS=","
read -p "Enter 2 numbers to add separated by a comma and random spaces: " num1 num2
num1=${num1//[[:blank:]]/}
num2=${num2//[[:blank:]]/}
sum=$((num1+num2))
echo "$num1 + $num2 = $sum"
IFS="$OIFS"

name="renkun"
echo "${name}'s toy"

samp_srt="The dog climed the tree"
echo "${samp_srt//dog/cat}"

echo "I am ${name:=renku}"





