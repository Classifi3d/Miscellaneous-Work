from hashlib import sha256
import string
import time

text=[]
    # print(letter,end=" ")
#%%
for letter in string.printable:
    print(sha256(letter.encode("ascii")).hexdigest()) 
    time.sleep(1)

 
        

# %%
for i in range(30):
    print("hey",end=" ")    

# %%
from hashlib import sha256
import string
import time

for letter in string.printable:
    print(letter,end=" ")
    print(sha256(letter.encode("ascii")).hexdigest()) 
    time.sleep(1)

# %%
