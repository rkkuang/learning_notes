#!/bin/bash
#comment
echo "Hello world"
myName="renkun"
declare -r NUM1=5
num2=4
num3=$((NUM1+num2))
num4=$((NUM1-num2))
num5=$((NUM1*num2))
num6=$((NUM1/num2))

echo "5+4=$num3"
echo "5-4=$num4"
echo "5*4=$num5"
echo "5/4=$num6"

echo $((5**2))
echo $((5%4))

rand=5
let rand+=4
echo "$rand"

echo "rand++ = $((rand++))"
echo "++rand = $((++rand))"
echo "rand-- = $((rand--))"
echo "--rand = $((--rand))"

num7=1.2
num8=3.4
num9=$(python3 -c "print($num7+$num8)")
echo $num9

cat<< END
This text
prints on
many lines
END













