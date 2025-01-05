#!/usr/bin/bash
#creating a programme to calculate my total expenses
echo "Please tell the how much money you have spent on what thing on which day"
read amount
read description
read date
expenses=0
function dailyExpense() 
{
	echo " Today, on $date I have spent $amount on $description "
	expenses=$(( $expenses + $amount ))
	echo "Till $date, I have spent total $expenses "
}

#dailyExpense $amount $date $amount
#dailyExpense
