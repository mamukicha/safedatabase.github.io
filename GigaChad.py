copyright()

from datetime import date, datetime
from fileinput import close
import hashlib
from math import pi
from math import sqrt
from tkinter import *

#down here it is time unit that we are gonna use 

dt = datetime.now()
a = dt.hour
b = dt.minute
c = dt.second
d = dt.microsecond
e = dt.day
f = dt.month
g = dt.year
#this down here is simple math :>
A_code = (a * g, b * f, c * e, d**2)
B_code = (e * g, f ** 2)
C_code = float(a + e)
C1_code = float(b + f)
C2_code = float(c + g)
C3_code = float(2 * d)

D_code = float(e + g)
D1_code = float(2 * f)

Kcode = C_code + C1_code + C2_code + C3_code + D_code +D1_code
if C_code or C1_code or C2_code or C3_code or D_code or D1_code % 2 == 0:
    Kcode + 1

A = int((b - a)*2)
def hello():
    Alist = [3, 14,15,92,65,35,89,79,32,38,46,26,43,38,32,79,50,28,84,19,71,69,39,93,75,105820,97,944,59,23,0,78,16,40,6,28,6,0,89,9,86,2,80,34,82,53,42,11,70,67,98,2,14,8,0,8,6,5,1,3,2,8,2,3,0,6,6,4,7,0,9,3,8,4,4,6,0,9,5,5,0,5,8,2,2,3,1,7,2,5,3,5,9,4,0,8,1,2,8,4,8,1,1,1,7,4,5,0,2,8,4,1,0,2,7,0,1,9,3,5,2,1,1,0,5,5,5,9,6,4,4,6,2,2,9,4,8,9,5,4,9,3,0,3,8,1,9,6,4,4,2,8,8,1,0,9,7,5,6,6,5,9,3,3,4,4,6,1,2,8,4,7,5,6,4,8,2,3,3,7,8,6,7,8,3,16,5,2,7,1,2,0,1,9,0,9,1,4,5,6,4,85,6,6,9,2,3,4,6,0,3,4,8,6,1,0,4,5,4,3,2,6,6,4,8,2,1,3,3,9,3,6,0,7,2,6,0,2,4,9,14,1,2,7,3,7,2,4,5,8,7,0,0,6,6,0,6,3,1,5,5,8,8,1,7,4,8,8,1,5,2,0,9,2,0,9,6,2,8,2,9,2,5,4,0,9,1,7,1,5,3,6,4,3,6,7,8,9,2,59,0,3,6,0,0,1,13,3,0,5,3,0,5,4,8,8,2,0,4,6,6,5,2,1,3,8,4,1,4,6,9,5,1,9,4,1,5,1,1,6,0,9,4,3,3,0,5,72,7,0,3,6,5,7,5,9,5,9,1,9,5,3,0,921,8,6,1,1,7,3,8,19,3,2,6,1,1,7,9,3,1,0,5,1,1,8,5,48,0,7,4,4,6,2,3,799,62,7,4,9,5,6,7,3,5,1,8,8,5,7,5,2,72,4,]
    return Alist

Alist = hello()
n = Alist.count(A)


ko = (Kcode - n) ** 2
super_code = ko * Kcode


sign = super_code**2 + b**2

nah = int(((sign / super_code) ** pi) + 69)

key = str(int(super_code - sqrt(nah) * pi) * C3_code * -1)
#key is salt. its wrecked but it depends on time user registered.
#not done yet :)

password = input("input password: ")
Nlist = ['password123', 'paroli123', '12345678', '123456789',]
if password in Nlist:
    print('wrong password')
    print(input('try again: '))

result = hashlib.md5(b'password')
str2hash = key
result = hashlib.md5(str2hash.encode())
print("bruh : ", end ="")
print(result.hexdigest())
#k is just md5 hashed key (its salt btw). 
k = result.hexdigest()
print("okay now the challenge starts!")
print(k)
def Sha512Hash(Password):
    HashedPassword=hashlib.sha512(Password.encode('utf-8')).hexdigest()
    print(HashedPassword)

for x in range(42069142069001, 42069142069691):
    if x % 2 != 2:
        print('nothing here')
    break
#pep and i are peppers. why? cuz they are predetermined numbers. 
pep = str(x)

i = int((12319121192191191 * 12122111) ** pi)

Sha512Hash(k + key + pep + str(i))

print("decript that one above :) ")

#so we have to decrypt k, nah and i to keys for our database to interact with it.  
#pep = 42069142069001
#k is md5ish encrypted code
#key, 
print("salts: ", k, key)
print('peppers: ', pep, i )
#down below i wanna use something like this but in backend

realkey = input("input key:")
realkey1 = input('input key: ')
realkey2 = input('input key: ')
if realkey != k and realkey1 != key and realkey2 != i:
    print('error')
    print('try again')
    realkey3 = input("input key:")
    realkey4 = input('input key: ')
    realkey5 = input('input key: ')
    if realkey3 != k and realkey4 != key and realkey5 != i:
        print('error')
        print('no more tries')
        close

if realkey == k and realkey1 == key and realkey2 == i:
    print("you passed :)")
    print("peppers: ", pep, i , "salts: ", k, key )
#so to sum up, pep and i are peppers,
#k and key are salts. 
#md5 and sha512 are hashes.
#woah, this is like double hashing, salting and peping, just to protect my data...
#this thing is true chad :) 
