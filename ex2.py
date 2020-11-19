#final code for generating key from signature
import random
import itertools
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import string
from PIL import Image
import time

start = time.time()
#img = Image.open('img2.jpg')
val = input("Enter image")
img = Image.open(val)
img = img.convert("RGBA")
datas = img.getdata()
k=0
newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255 or item[0]==255 or item[1]==255 or item[2]==255:
        newData.append((255, 255, 255, 0))
#        k=k+1
    else:
        newData.append(item)
#print(datas)
img.putdata(newData)
#img.save("temp1.png", "PNG")
#print(k)
#print(len(newData))
newData = [i for i in newData if i[0]!=255 and i[1]!=255 and i[2]!=255 and i[3]!=0 ]
#print(newData)
#print(len(newData))

secure_random = random.SystemRandom()
#choices = secure_random.choice(newData)
#print ("cryptographically secure random choice - ", choices)
l=random.randint(0,len(newData)-1)
choices1 = secure_random.sample(newData,l)
#print(l)
#print ("cryptographically secure random choices - ", choices1)
result = list(itertools.chain(*choices1))
#print(result)
str1 = [str(i) for i in result]
plaintext=int("".join(str1))
#print(plaintext)

#generating key
password = str(plaintext).encode() # Convert to type bytes
salt = b'salt_'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) 
#text=text.replace(" ", "")
#print(text)
#print(hex(int(text, 16) + 0x200))
print(key)
end = time.time()
print(end-start)
