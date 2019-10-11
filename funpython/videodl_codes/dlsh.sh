#!/bin/bash
#baseurl=$0
#start=$1
#end=$2
#savepath=$3
read -p "Please input a base url, e.g. https://www.bilibili.com/video/av58129929/?p=: " baseurl
read -p "input a number for which video you want to start: " start
read -p "input a number for which video you want to end: " end
read -p "input the save path: " savepath

# str to int: ${{a}}

#startnum=${{start}}
#endnum=${{end}}

for i in {$(($start))..$(($end))};do
	you-get $baseurl$i -o $savepath
done


