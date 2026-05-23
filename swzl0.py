import sys

code = open(sys.argv[1]).read().split("\n")
for i in range(len(code)):
    code[i] = code[i].split(' ')

try:
    input = sys.argv[2]
except:
    input = ''

def getin(idx):
    try:
        return input[idx]
    except:
        return 256        

def gcp(part):
    if part == 0:
        try:
            return code[index][part]
        except IndexError:
            exit()
    else:
        return int(code[index][part])

def unts(u):
    return -2**31*u>>31+u%2**31

def nothing():
    print('', end='')

mb = 12
mem = [0] * 2**mb
index = 0
halted = 0

while True:
    match gcp(0):
        case "rem":
            nothing()
        case "set":
            mem[gcp(1)%(2**mb)] = gcp(2)%(2**32)
        case "xor":
            mem[gcp(3)%(2**mb)] = mem[gcp(1)%(2**mb)]^mem[gcp(2)%(2**mb)]
        case "out":
            print(chr(mem[gcp(1)%(2**mb)]), end='')
        case "jgt":
            if mem[gcp(1)%(2**mb)] > mem[gcp(2)%(2**mb)]:
                index += unts(gcp(4)%(2**32))-1
            else:
                index += unts(gcp(3)%(2**32))-1
        case "jeq":
            if mem[gcp(1)%(2**mb)] == mem[gcp(2)%(2**mb)]:
                index += unts(gcp(4)%(2**32))-1
            else:
                index += unts(gcp(3)%(2**32))-1
        case "in":
            mem[gcp(1)%(2**mb)] = ord(getin(gcp(2)%(2**32)))
        case "nand":
            mem[gcp(3)%(2**mb)] = 2**32+~(mem[gcp(1)%(2**mb)]&mem[gcp(2)%(2**mb)])
        case "halt":
            exit()
        case _:
            nothing()
    index+=1
