import hashlib

value = chr(0x24 ^ 0x43)
value += chr(0 ^ 0x64)

print "value: " + value
print "flag: PCTF{" + hashlib.sha256(value).hexdigest() + "}"
