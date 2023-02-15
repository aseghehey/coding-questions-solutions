
# number = "23511011501782351112179911801562340161171141148"
number = "7297118101329732781059910132689712132"
# number = input('give: ')
# number = number[::-1] # reverse it

'''
A-Z: 65-90
a-z: 97-112
' ': 32
'''
res = ''
l, r = 0,1

# print(int(number[0:2]))
print(number)
while r < len(number):
    print(l, r)
    curnumber = int(number[l:r+1])
    if 32 <= curnumber <= 122:
        res += chr(curnumber)
        l = r + 1
        r += 2
    else:
        r += 1
    # print(curnumber, l, r)

print(res)