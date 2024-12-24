#!/usr/bin/bash
echo "Please input the name of the person"
read person
echo "Please input the greting message"
read greetMsg
function greet() {
 #echo " $greetMsg , $person "
 echo " $person , $greetMsg "
}
greet $greetMsg $person
