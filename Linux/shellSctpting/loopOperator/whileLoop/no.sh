#syntax
#while condition is true
# do
#    statement
# done

#for e.g
#!/usr/bin/bash
echo "please enter the number"
read number
while [ $number -le 10 ]
do
    echo "$number"
    number=$(( number+1 ))
done
echo "loop is completed"







