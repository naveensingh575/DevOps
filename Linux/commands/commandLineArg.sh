The argument passed with script name are known as command line arguments
for e.g ./add.sh 2 3
These can be access by $0 .. $n
$0 - is the script itself i.e ./add.sh
$1 - fisrt command line argument value i.e 2
$2 - second command line argument value i.e 3
$# - count of command line inputs i.e 2
$3 - third argument i.e empty


add.sh
#!/usr/bin/bash
echo $0
echo $1
echo $2
num=`expr $1 + $2`
echo "the sum of two number is $num"
echo $#
echo third argument have $3 value

./add.sh 5 7
  o/p - 
  ./add.sh
  5
  7
  the sum of two number is 12
  2
  rgird argument have   value
  

