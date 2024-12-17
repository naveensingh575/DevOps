#!/usr/bin/bash
echo "Write the name of Folder"
read folderName
files=`ls $folderName`

echo ${files[@]}

for file in ${files[@]}
do
        echo $file
done

#to iterate over a list of number
for num in {0..10}
do
        echo "Creating VM $num"
done


#to iterate over a list of number
#echo "Please input the number"
#read number
#echo $number
#for num in {0..$number}
#do
#        echo "Creating VM $num"
#done
