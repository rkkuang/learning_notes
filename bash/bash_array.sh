#!/bin/bash

fav_nums=(3.14 2.718 0.618 71 11 30)
echo "Pi: ${fav_nums[0]}"

fav_nums[6]=1.618

echo "GR: ${fav_nums[6]}"

fav_nums+=(100 700)

for i in ${fav_nums[*]};do
	echo $i
done


for i in ${fav_nums[@]};do
	echo $i
done


echo "Array Length: ${#fav_nums[@]}"

echo "Index 3 Length: ${#fav_nums[3]}"

sorted_nums=($(for i in "${fav_nums[@]}";do
echo $i;
done | sort))


for i in ${sorted_nums[*]};do
	echo $i
done

unset 'sorted_nums[1]'
unset sorted_nums







