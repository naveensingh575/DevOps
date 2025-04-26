#!/bin/bash/
user=$1
group=$2
#add user
useradd $user
#create admin grp
groupadd $group
#attach admin group to user
usermod -aG $group $user
#check group config
sudo tail /etc/group
#enable sudo config for group
echo "%$group ALL=(ALL) ALL" > /etc/sudoers.d/admin
sudo vsudo -c
#check user having all permissions
sudo userdel user4
#logout and delete user
