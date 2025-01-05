#!/usr/bin/bash
echo "Please input the operation you want"
read oprt
echo "Please input two no."
read num1
read num2
echo "Please $oprt $num1 and $num2"
output=0
if [[ $oprt == "add"  ]]
then
	output=` expr $num1 + $num2 ` 
fi

if [[ $oprt == "subtract" ]]
then
	output=` expr $num1 - $num2 `
fi

if [[ $oprt == "multiply" ]]
then
	output=$(($num1 * $num2))
fi

if [[ $oprt ==  "divide" ]]
then
	output=$(($num1 / $num2))
fi

echo " The $oprt of $num1 and $num2 is $output "
