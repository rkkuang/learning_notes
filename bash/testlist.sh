#!/bin/bash
#bash testlist.sh
#https://blog.csdn.net/taiyang1987912/article/details/39897547
city=(1 2 3 4 5)
for i in ${city[@]}
do
	echo $i
done

#https://blog.csdn.net/weixin_33971977/article/details/93213142
#https://forum.ubuntu.org.cn/viewtopic.php?t=264546
lis=(1 3 5 7)
for i in $(seq 0 2 ${#lis[@]})
do
	echo ${lis[$i]} ${lis[$((i+1))]}
	#echo $i
done
