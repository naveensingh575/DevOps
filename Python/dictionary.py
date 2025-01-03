#dictionary
bio_data = {
    'Name' : 'Naveen Kumar' ,
    'Age' : '26' ,
    'Address' : '11/1C, Rail Vihar, MDC-4, Pachkulla-134114, Haryana, India' ,
    'Education' : 'B.TECH in ECE',
    'College' : 'BPIT, Delhi' ,
    'Working at' : 'Infosys' ,
    'Years_of_exp' : '3.6' ,
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
    print('You should work on you skills and try to switch')
