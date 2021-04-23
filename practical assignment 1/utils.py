from random import shuffle,sample,randint

# Decimal to binary conversion
def dec2bin(num): 
    res = bin(num).replace("0b", "")
    if(len(res)%4 != 0):
        div = len(res) / 4
        div = int(div)
        counter =(4 * (div + 1)) - len(res) 
        for i in range(0, counter):
            res = '0' + res
    return res

#binary to decimal conversion
def bin2dec(binary):
    binary=int(binary)
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    # print(decimal)
    return decimal

# hexadecimal to binary conversion
def hex2bin(s):
    mp = {'0' : "0000", 
          '1' : "0001",
          '2' : "0010", 
          '3' : "0011",
          '4' : "0100",
          '5' : "0101", 
          '6' : "0110",
          '7' : "0111", 
          '8' : "1000",
          '9' : "1001", 
          'A' : "1010",
          'B' : "1011", 
          'C' : "1100",
          'D' : "1101", 
          'E' : "1110",
          'F' : "1111" }
    bin = ""
    for i in range(len(s)):
        if s[i]=='\n':
          return bin
        bin = bin + mp[s[i]]
    return bin
      
# Binary to hexadecimal conversion
def bin2hex(s):
    mp = {"0000" : '0', 
          "0001" : '1',
          "0010" : '2', 
          "0011" : '3',
          "0100" : '4',
          "0101" : '5', 
          "0110" : '6',
          "0111" : '7', 
          "1000" : '8',
          "1001" : '9', 
          "1010" : 'A',
          "1011" : 'B', 
          "1100" : 'C',
          "1101" : 'D', 
          "1110" : 'E',
          "1111" : 'F' }
    hex = ""
    for i in range(0,len(s),4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1] 
        ch = ch + s[i + 2] 
        ch = ch + s[i + 3] 
        hex = hex + mp[ch]
          
    return hex

# xor between msg and key
def xor(msg,key):
  out=""
  # print(len(key),len(msg))
  for i in range(len(msg)):
    out=out+str(int(msg[i])^int(key[i]))
  return out

#function to calculate inverse permutation of a given permutation
#arr : input permutation
def inversePermutation(arr):
    out=[]
    size=len(arr)
    # Loop to select Elements one by one
    for i in range(0, size):
 
        # Loop to print position of element
        # where we find an element
        for j in range(0, size):
 
        # checking the element in increasing order
            if (arr[j] == i + 1):
 
                # print position of element where
                # element is in inverse permutation
                out.append(j+1)
                break
    return out

# Permute function to rearrange the bits
# k = bits to be rearranged
# arr = permutation table
# n = number of output bits
def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation


#function to generate a permutation of given size
#size : length of permutation
def generateTable(size):
  arr=[i for i in range(1,size+1)]
  shuffle(arr)
  return arr

# arr = [2, 3, 4, 5, 1]
# size = len(arr)
# initial_perm = [58, 50, 42, 34, 26, 18, 10, 2, 
#                 60, 52, 44, 36, 28, 20, 12, 4, 
#                 62, 54, 46, 38, 30, 22, 14, 6, 
#                 64, 56, 48, 40, 32, 24, 16, 8, 
#                 57, 49, 41, 33, 25, 17, 9, 1, 
#                 59, 51, 43, 35, 27, 19, 11, 3, 
#                 61, 53, 45, 37, 29, 21, 13, 5, 
#                 63, 55, 47, 39, 31, 23, 15, 7] 
# print(inversePermutation(initial_perm))