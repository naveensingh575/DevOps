#!/usr/bin/bash/
#Role based access control
#add the group name iam
user=$1
group=$2
groupadd $group
useradd -G $group $user
passwd $user
echo "%$group ALL=(ALL) /sbin/useradd,/sbin/userdel,/bin/passwd" > /etc/sudoers.d/$group
visudo -c
