# coding: utf-8
import random
import os
import math

#flag = b"ctf4b{xxx___censored___xxx}"
pre_flag = [0] * 42

# Please remove here if you wanna test this code in your environment :)
#flag = os.getenv("FLAG").encode()

cipher = [4396, 22819, 47998, 47995, 40007, 9235, 21625, 25006, 4397, 51534, 46680, 44129, 38055, 18513, 24368, 38451, 46240, 20758, 37257, 40830, 25293, 38845, 22503, 44535, 22210, 39632, 38046, 43687, 48413, 47525, 23718, 51567, 23115, 42461, 26272, 28933, 23726, 48845, 21924, 46225, 20488, 27579, 21636]

for i in range(len(cipher)):
    for j in range(len(cipher)-1):
        # if j == 27:
        #     print(f"i:{i} j:{j} ciper:{cipher[i]}")
        f = math.sqrt(cipher[i] - j)
        if f.is_integer():
            print(f"i:{i} j:{j} f:{f}")
            pre_flag[j] += f
            break

for i in range(len(cipher)-1):
    if pre_flag[i] == 0:
        print(i)

for i in range(len(cipher)-1):
    if i == 27:
        print(cipher[i])

print(pre_flag)
print(len(pre_flag))

flag = [99]

for i in range(len(cipher)-1):
    flag.append(pre_flag[i] - flag[i])

#random.shuffle(cipher)

print(len(flag))

ans = ""

for i in range(len(flag)):
    ans += (chr(int(flag[i])))

print(ans)
