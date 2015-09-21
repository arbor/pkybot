import xtea

key = "ba9132192c168024076091cce416e50e".decode("hex")

enc = []
plain = []
start = ScreenEA()

# needs to be a multiple of 8
for i in range(24):
    enc.append(chr(Byte(start+i)))
       
x = xtea.new(key, mode=xtea.MODE_ECB)
plain = x.decrypt("".join(enc))

print plain
