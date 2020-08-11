import sys

bytes1=[]
bytes2=[]
bytes3=[]
f1 = open("C:\\Users\\JBU_Lee\\Desktop\\BoB9기\\정시형멘토님\\ctr.zip\\gpl-3.0.txt","rb")
f2 = open("C:\\Users\\JBU_Lee\\Desktop\\BoB9기\\정시형멘토님\\ctr.zip\\cipher_oracle.bin","rb")
while True:
    byte = f1.read(1)
    if byte == b"":break
    bytes1.append(ord(byte))

while True:
    byte = f2.read(1)
    if byte == b"":break
    bytes2.append(ord(byte))

print(bytes1)
print(bytes2)

key = bytes([_a ^ _b for _a, _b in zip(bytes1, bytes2) ])
print(key)

f1.close()
f2.close()

f3 = open("C:\\Users\\JBU_Lee\\Desktop\\BoB9기\\정시형멘토님\\ctr.zip\\cipher_challenge.bin","rb")
while True:
    byte = f3.read(1)
    if byte==b"": break
    bytes3.append(ord(byte))

decrypt = bytes([_a ^ _b for _a, _b in zip(bytes3, key)])
print(decrypt)
f3.close()

f = open("C:\\Users\\JBU_Lee\\Desktop\\BoB9기\\정시형멘토님\\ctr.zip\\decrpyt_cipher_challenge.bin", "wb")
f.write(decrypt)
f.close()


