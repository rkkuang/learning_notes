#!/bin/bash

read -p "How old are you : " age

case $age in
	[0-4])
		echo "Too young for school"
		;;
	5)
		echo "Go to Kindergarten"
		;;
	[6-9]|1[0-8])
		grade=$((age-5))
		echo "Go to grade $grade"
		;;
	*)
		echo "You are too old for school"
		;;
esac

can_vote=0
#age=18
((age>=18?(can_vote=1):(can_vote=0)))
echo "Can vote: $can_vote"

