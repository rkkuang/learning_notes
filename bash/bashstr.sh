#!/bin/bash

str1=""
str2="Sad"
str="Happy"

if [ "$str1" ];then
	echo "$str1  is not null"
fi

if [ -z "$str1" ];then
	echo "$str1 has no value"
fi
