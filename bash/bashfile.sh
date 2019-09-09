#!/bin/bash

file1="./testfile1"
file2="./testfile2"

if [ -e "$file1" ];then
	echo "file1 exists"

	if [ -f "$file1" ];then
		echo "$file1 is a normal file"
	fi

	if [ -r "$file1" ];then
		echo "$file1 is readable"
	fi

	if [ -w "$file1" ];then
		echo "$file1 is writable"
	fi
fi


