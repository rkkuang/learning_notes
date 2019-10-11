#!/bin/bash
#bash dlsh_parallel.sh https://www.bilibili.com/video/av58129929/\?p\= 3 10 ./PrinciplesofComputerOrganization
baseurl=$1
startnum=$2
endnum=$3
savepath=$4

echo $baseurl
echo $startnum
echo $endnum
echo $savepath

#echo $(($startnum+1))

#read -p "Please input a base url, e.g. https://www.bilibili.com/video/av58129929/?p=: " baseurl
#read -p "input a number for which video you want to start: " startnum
#read -p "input a number for which video you want to end: " endnum
#read -p "input the save path: " savepath

#https://www.cnblogs.com/xudong-bupt/p/6079849.html
#https://www.cnblogs.com/Spider-spiders/p/9233225.html

#https://blog.csdn.net/dubendi/article/details/78931979

#subproc=10
for i in {$(($startnum))..$(($endnum))};do
	{
		echo $i
		you-get $baseurl$i -o $savepath
	}&
done
