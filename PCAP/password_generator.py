import random

str1 = '0,1,2,3,4,5,6,7,8,9'
str2 = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
str3 = '!,@,#,$,%,^,&,(,),_,+'
numelement = random.choice(str1)
alphaelement = random.choice(str2)
specialelement = random.choice(str3)

def passgen():
    pwdlen = int(input('Provide password length: '))
    useupcase = str(input('Use uppercase letters? (y/n): '))
    usedigit = str(input('Use digits? (y/n): '))
    usespl = str(input('Use special characters? (y/n): '))
    for el in range(pwdlen):
        if useupcase == 'y' or 'Y':
            upcasedecider = random.randint(0,1)
            if upcasedecider == 0:
                pwdstr1 = str(str2)
                pwdstr1.capitalize()
            elif upcasedecider == 1:
                pwdstr1 = str(str2)
                pwdstr1.lower()
    print('Generated password: ')
    return

def exception():
     print('Please enter only 1 or 2')
     return


while True:
    print('-- Password generator --')
    print('-- Choose option --')
    inp = int(input('1: generate password \n2: exit the program\n'))
    if inp == int(2):
        print('Bye!')
        break
    elif inp == int(1):
        passgen()
    else:
        if type(inp) != int():
            exception()

print('End of program')