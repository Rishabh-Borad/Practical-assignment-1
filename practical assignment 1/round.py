from expansionPermutation import *

#F function of each round
#msg : input message block
#key : key for given round
#permutationTable : permutation table
#expansionTable : expansion table
def F(msg,key,permutationTable,expansionTable):
	msg = expansionPermutation(msg,expansionTable)
	msg = xor(msg,key)
	msg = sBoxfn(msg)
	msg = permutation(msg,permutationTable)
	return msg

#single round of DES algorithm
#msg : input message block
#key : key for given round
#permutationTable : permutation table
#expansionTable : expansion table
def round(msg,key,permutationTable,expansionTable):
	left=msg[:len(msg)//2]
	right=msg[len(msg)//2:]
	outLeft=right
	# outRight=left
	outRight=xor(left,F(right,key,permutationTable,expansionTable))

	return outLeft+outRight


# pt = "2323"
# key = "012345"
# pt=hex2bin(pt)
# key=hex2bin(key)
# # x,y=generatePermutationTable(len(pt)//2),generateExpansionTable(len(pt)//2)
# x= [1, 4, 5, 2, 8, 6, 7, 3]
# y= [4, 1, 6, 5, 2, 7, 8, 3, 8, 4, 3, 2]
# print("x=",x)
# print("y=",y)
# msg=round(pt,key,x,y)
# print(bin2hex(msg))