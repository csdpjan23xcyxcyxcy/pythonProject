import string
import random
import hashlib

f = open("output2.txt", "r")
f2 = open("salted6.txt", "x")
f3 = open("pass6.txt", "x")


for x22 in f:
    ha = random.choice(string.ascii_lowercase + string.digits)
    if len(x22) < 20:
        new_pre_salt = x22[5] + x22[6] + x22[7] + x22[8] + x22[9] + x22[10].strip() + ha
        md5 = hashlib.md5(str(new_pre_salt).encode()).hexdigest()
        print(new_pre_salt, file=f3)
        print(md5, file=f2)


