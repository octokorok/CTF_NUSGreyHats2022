import secrets
import binascii as bin

FLAG = b'grey{...}'

#assert len(FLAG) == 40

_key = secrets.token_bytes(4)

def encrypt(m,key):
    return bytes([x ^ y for x, y in zip(m,key)])

c = b''
for i in range(0, len(FLAG), 4):
    c += encrypt(bytes(FLAG[i : i + 4]),_key)

# want to get this answer
# 982e47b0840b47a59c334facab3376a19a1b50ac861f43bdbc2e5bb98b3375a68d3046e8de7d03b4

#working backwords. Have to have a decrypt function. XOR is commutative

finalAns = bin.unhexlify('982e47b0840b47a59c334facab3376a19a1b50ac861f43bdbc2e5bb98b3375a68d3046e8de7d03b4')

#find key
getKey = bytes([x ^ y for x, y in zip(b'grey',finalAns[0:4])])

flag = b''
for i in range(0, len(finalAns),4):
    flag += encrypt(finalAns[i:i+4],getKey)
print(flag)
