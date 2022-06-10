from pwn import *

operations = ['add','mul','sub','neg','inc']

def solver(question):
    qnUnit = question.strip().split(' ')
    holdingNumList = []
    for item in reversed(qnUnit):
        if item not in operations:
            holdingNumList.append(int(item))
        else:
            if item == 'neg':
                newNum = holdingNumList.pop() * -1
            elif item == 'inc':
                newNum = holdingNumList.pop() + 1
            else:
                num1 = holdingNumList.pop()
                num2 = holdingNumList.pop()
                if item == 'add':
                    newNum = num1 + num2
                elif item == 'mul':
                    newNum = num1 * num2
                elif item == 'sub':
                    newNum = num1 - num2
            holdingNumList.append(newNum)
    toReturn = str(holdingNumList[0])
    return toReturn

conn = remote('challs.nusgreyhats.org', 15521)
conn.recvuntil(b'Send START when you are ready!\n',drop=True)
conn.sendline(b'START')

for i in range(100):
    challenge = conn.recvline().decode()
    answer = solver(challenge).encode()
    conn.sendline(answer)
    next = conn.recvline()

print(conn.recvline())
print(conn.recvline())
