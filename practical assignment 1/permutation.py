from sBox import *

# Straight Permutaion Table
per = [ 16,  7, 20, 21,
        29, 12, 28, 17, 
         1, 15, 23, 26, 
         5, 18, 31, 10, 
         2,  8, 24, 14, 
        32, 27,  3,  9, 
        19, 13, 30,  6, 
        22, 11,  4, 25 ]

#function to generate permutation table for given size of input message block
#size : length of input to permutation box
def generatePermutationTable(size):
        if size==32:
                return per
        return generateTable(size)

#function to permute input message w.r.t. permutation table
#msg : input message
#permutationTable : permutation table
def permutation(msg,permutationTable):
        return permute(msg,permutationTable,len(permutationTable))

# msg="1234"
# msg=hex2bin(msg)
# permutationTable=generatePermutationTable(len(msg))
# print(bin2hex(permutation(msg,permutationTable)))