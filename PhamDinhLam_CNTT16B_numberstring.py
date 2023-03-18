bai1='Thirty' + 'Days' + 'Of' + 'Python'
bai2= 'Coding' + 'For' + 'All'
#bai3
company='Coding For All'
#bai4
print(company)
#bai5
print(len(company))
#bai6
print(company.upper())
#bai7
print(company.lower())
#bai8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#bai9
x=slice(7,len(company))
#bai10
print(company[x])
#bai11
print(company.find('Coding',0,len(company)-1))
#bai12
print(company.replace('Coding','Python',1))
#bai13
print(company.replace('All','Everyone',1))
#bai14
print(company.split())
#bai15
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))
#bai16
print(company[0])
#bai17
print(ord(company[len(company)-1]))
#bai18

print(company[10])
#bai19
#bai20
print(company.index('C',0,len(company)-1))
#bai21
print(company.index('F',0,len(company)-1))
#bai22
print(company.rfind('l',0,len(company)-1))
#bai23
print('You cannot end a sentence with because because because is a conjunction'.find('because',0,100))
#bai24
print('You cannot end a sentence with because because because is a conjunction'.rindex('because',0,100))
#bai25
print('You cannot end a sentence with because because because is a conjunction'.replace('because ','',5))
#bai26
print('You cannot end a sentence with because because because is a conjunction'.find('because ',0,100))
#bai27
if company.index('Coding',0,len(company)-1)==0:
    print("True")
else:
    print("False")
#bai28
if company.rindex('Coding',0,len(company)-1)==len(company)-1:
    print("True")
else:
    print("False")
#bai29
print(' Coding For All '.strip())
#bai30
if '30DaysOfPython'.isidentifier:
    print("True")
else:
    print("False")
if 'thirty_days_of_python'.isidentifier:
    print("True")
else:
    print("False")
