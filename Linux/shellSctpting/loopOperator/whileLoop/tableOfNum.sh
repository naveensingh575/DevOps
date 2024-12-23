#!/usr/bin/bash
echo "Please tell the no. whoes table you need"
read num
itr=1
arg=1
while test $itr -le 10
do
	#$arg=` expr $num  *  $itr `
	arg=$(( $num * $itr ))
	echo " $num $itr ja is equal to $arg"
	itr=` expr $itr  +  1 `
done

echo " Table of $num is printed above"
