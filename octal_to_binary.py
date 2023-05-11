def OctToBin(o):
    return bin(int(o, 8))
print(end="")
num=input()
b=OctToBin(num)
print(b[2:])