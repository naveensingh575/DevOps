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
