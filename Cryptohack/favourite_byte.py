from pwn import xor

flagBytes = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
byte=0x00

for i in range(256):
    flag=xor(flagBytes, byte).decode("utf-8")
    if("crypto" in flag):
        print(flag)
        break
    byte=byte + 0x01