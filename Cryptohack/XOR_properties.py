from pwn import xor

bytekey1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
bytedata2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
bytedata3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
bytedata4 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

bytekey2 = xor(bytedata2, bytekey1)
bytekey3 = xor(bytedata3, bytekey2)
flag = xor(bytedata4, bytekey1, bytekey2, bytekey3)

print(flag.decode('utf-8'))
