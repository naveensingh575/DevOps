#syntax

if [[ string ]]
then
  statement
fi

if (( numeric ))
then
  statment
fi

if condition is true
then
   do this
fi

to check file or directory exist -e , is type file -f, is type dirctory -d , read permission -r, w

for e.g
#!/usr/bin/bash
echo $1
if [[ -e $1 ]]
then
        echo $1 exists
        if [[ -f $1 ]]
        then
                echo $1 is file
        else
                if [[ -d $1 ]]
                then
                        echo $1 is directory
                else
                        if [[ -L $1 ]]
                        then
                                echo $1 is link
                        else
                                echo $1 is not a file, directory and link
                        fi
                fi
        fi
else
        echo "file doen't exist"
fi
