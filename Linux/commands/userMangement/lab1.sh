#!/bin/bash/
#we will do first lab
#task
#1. add user 
#2. check password by tail
#3. set passwrd
#4. add comment for user
#5. check passwd by tail again
#6. remove user with home directory
#7. again check passwd with tail

newUser=$1

#1. add user
useradd $newUser
#2. check password by tail
sudo tail /etc/passwd/
#3. set passwrd
passwd $newUser
#4. add comment for user
usermod -c "Operator one" $newuser	
#5. check passwd by tail again
sudo tail /etc/passwd/
#6. remove user with home directory
userdel $newUser
#7. again check passwd with tail
sudo tail /etc/passwd/
