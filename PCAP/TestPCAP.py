import random

str1 = [0,1,2,3,4,5,6,7,8,9]
str2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str3 = ['!','@','#','$','%','^','&','(',')','_','+']

upcasedecider = random.randint(0,1)
if upcasedecider == 0:
    pwdstr1 = str(str2)
    pwdstr1.capitalize()
elif upcasedecider == 1:
    pwdstr1 = str(str2)
    pwdstr1.lower()

genpwd = pwdstr1+pwdstr1
print(str(genpwd[0:8]))