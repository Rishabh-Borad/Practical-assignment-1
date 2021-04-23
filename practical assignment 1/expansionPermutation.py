from permutation import *

# Expansion Table
exp = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5, 
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11, 
         12, 13, 12, 13, 14, 15, 16, 17, 
         16, 17, 18, 19, 20, 21, 20, 21, 
         22, 23, 24, 25, 24, 25, 26, 27, 
         28, 29, 28, 29, 30, 31, 32, 1 ]

#function to generate expansion table for given size of message
#size : length of message to expantion permutation box
def generateExpansionTable(size):
	if size==32:
		return exp

	arr = generatePermutationTable(size)
	x = sample(arr,len(arr)//2)
	return arr+x

#function to permute input message w.r.t expansion permutation table
#expansionPermutationTable : expansion permutation table generated using above function
def expansionPermutation(msg,expansionPermutationTable):
	return permute(msg,expansionPermutationTable,len(expansionPermutationTable))

# msg="0123"
# msg=hex2bin(msg)
# print(msg)
# x=generateExpansionTable(len(msg))
# print(x,len(x))
# print(expansionPermutation(msg,x))
# print(bin2hex(expansionPermutation(msg,x)))