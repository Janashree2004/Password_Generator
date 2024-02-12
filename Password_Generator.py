import random

Letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers=['0','1','2','3','4','5','6','7','8','9']
Symbols=['~','!','@','#','$','%','^','&','*','(',')','_','-','+','{','}','[',']',',','?',',']
print("Welcome To Code Generator")
N_Letters=int(input("How many letters do you want in your passwords?\n"))
N_Numbers=int(input("How many Numbers do you want in your passwords?\n"))
N_Symbols=int(input("How many Symbols do you want in your passwords?\n"))
Pass=""
for i in range(1,N_Letters+1):
    Char=random.choice(Letters)
    Pass=Pass+Char
for i in range(0,N_Numbers+1):
    Num=random.choice(Numbers)
    Pass=Pass+Num
for i in range(1,N_Symbols+1):
    Sym=random.choice(Symbols)
    Pass=Pass+Sym

print(Pass)