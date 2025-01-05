#dictionary
bio_data = {
    'Name' : 'Naveen Kumar' ,
    'Age' : 26 ,
    'Address' : '11/1C, Rail Vihar, MDC-4, Pachkulla-134114, Haryana, India' ,
    'Education' : 'B.TECH in ECE',
    'College' : 'BPIT, Delhi' ,
    'Working at' : 'Infosys' ,
    'Years_of_exp' : 3.6 ,
    'Live' : 'Chandigarh' ,
    'Salary' : '4.92 LPA'
}

#print(bio_data['Live'])
if int(bio_data['Age']) > 18 :
    print('You are eligible to vote')
else:
    print('Minor: not eligible to vote')

if float(bio_data['Years_of_exp']) > 3:
    print(f'You are eligible to become TA in {bio_data['Working at']}' )
else:
    wait =   (3 - float(bio_data['Years_of_exp'])) * 10
    print(f'You are not eligible to become TA in {bio_data['Working at']}, Please wait for {wait} months')
#Inhand_salary = bio_data['Salary'][:4]
#print(Inhand_salary)
if float(bio_data['Salary'][:4]) > 1.5 * float(bio_data['Years_of_exp']):
    print('You salary is according to market standards') 
else:
    print('You should work on your skills and try to switch')

#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
#print(bio_data)
print(type(bio_data))
print(len(bio_data))
#get method is same as index , only that if we by mistake give wrong key it don't give fatal
print(bio_data.get('salary'))
print(bio_data.get('Salary'))
print(bio_data.get('Company'))
#to get keys and values and items
keys = bio_data.keys()
values = bio_data.values()
items = bio_data.items()
print(keys)
print(values)
print(items)

for key , value in items:
    print(f'{key} : {value}')
    

#clear is method which clear the dictionary
bio_data.clear()
print(bio_data)


#to copy
family = { "Self" : "Naveen Kumar",
           "Father" : "Satyavir Singh" ,
           "Mother" : "Sunita Devi" ,
           "Sister" : "Sanju Sangwan" ,
           "Friends" : ['Saurabh' , 'Gaurav' , 'Harsh Pandey', 'Manish Jha' ,'Manish Yadav']}
family1  = family.copy()
print(f'family: {family}')
print(f'famil1:{family1}')
family['Friends'][1] = 'Gaurav Mehra'
print(family)
print(family1)
#To remove pop expact the key which you want to remove from 
#print(family.pop('Friends'))
#To remove popitem remove the last item from dict 
#print(family.popitem())
#Update concate the given dictionary to bigger dict
family.update(bio_data)
print(bio_data)
print(family)
