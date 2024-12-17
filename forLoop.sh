#!/usr/bin/bash
echo "Write the name of Folder"
read folderName
files=`ls $folderName`

echo ${files[@]}

for file in ${files[@]}
do
        echo $file
done
