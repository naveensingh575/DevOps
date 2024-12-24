#!/usr/bin/bash
echo "Please input the number for which you want to check divisibality"
read num
echo "Please input the range till which you want to check is thwy are divide by {{$num}} "
read range
i=1
#without space variable=value
while test $i -le $range
# test for true or false $varilebe - value  -le less than equal
do
	if test ` expr $i % $num ` -eq 0
	then
		echo " $i is divisible by $num "	
		i=` expr $i + 1 `
	#	echo " $i "
		continue
	fi
	echo " $i is non divisible no by $num"
	i=` expr $i + 1 `
        
done
