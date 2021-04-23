from utils import *

# --parity bit drop table
pc1Table = [57, 49, 41, 33, 25, 17, 9, 
        1, 58, 50, 42, 34, 26, 18, 
        10, 2, 59, 51, 43, 35, 27, 
        19, 11, 3, 60, 52, 44, 36, 
        63, 55, 47, 39, 31, 23, 15, 
        7, 62, 54, 46, 38, 30, 22, 
        14, 6, 61, 53, 45, 37, 29, 
        21, 13, 5, 28, 20, 12, 4 ]


# Number of bit shifts 
shift_table = [1, 1, 2, 2, 
                2, 2, 2, 2, 
                1, 2, 2, 2, 
                2, 2, 2, 1 ]
  
# Key- Compression Table : Compression of key from 56 bits to 48 bits
pc2Table = [14, 17, 11, 24, 1, 5, 
            3, 28, 15, 6, 21, 10, 
            23, 19, 12, 4, 26, 8, 
            16, 7, 27, 20, 13, 2, 
            41, 52, 31, 37, 47, 55, 
            30, 40, 51, 45, 33, 48, 
            44, 49, 39, 56, 34, 53, 
            46, 42, 50, 36, 29, 32 ]

#function to generate permuted choice 1 table
#size : size of key
def generatePC1Table(size):
	if size==64:
		return pc1Table

	arr=[i for i in range(1,size+1) if i%8!=0]
	shuffle(arr)
	return arr

#function to generate permuted choice 2 table
#size : size of key after passing through permuted choice 1
def generatePC2Table(size):
	if size==56:
		return pc2Table

	if size==28:
		removeBits=[i for i in range(1,size+1)]
		removeBits=sample(removeBits,4)

		arr=[i for i in range(1,size+1) if i not in removeBits]

		return arr

	if size==112:

		removeBits=[i for i in range(1,size+1)]
		removeBits=sample(removeBits,16)

		arr=[i for i in range(1,size+1) if i not in removeBits]

		return arr		

#function for permuted choice 1 and permuted choice 2 boxes
#key : input key to box
#pcTable : table which box follows
def permutedChoice(key,pcTable):
	return permute(key,pcTable,len(pcTable))

#function to shift the bits of key on the left side w.r.t shift_table created above
#key : input key to left shift box
#roundNumber : number of round which is currently in process
def leftShift(key,roundNumber):
	roundNumber-=1
	roundNumber%=len(shift_table)
	left=key[:len(key)//2]
	right=key[len(key)//2:]
	outLeft=left[shift_table[roundNumber]:]+left[:shift_table[roundNumber]]
	outRight=right[shift_table[roundNumber]:]+right[:shift_table[roundNumber]]

	return (outLeft+outRight)

#function to generate keys for every round
#numRounds : number of rounds
#key : key after passing through permuted choice 1
#pc2Table : permuted choice 2 table
def generateRoundKeys(numRounds,key,pc2Table):
	arr=[]
	for i in range(numRounds):
		key=leftShift(key,i+1)
		arr.append(permutedChoice(key,pc2Table))
	return arr

# key="AABB09182736CCDD"
# key=hex2bin(key)

# x=generatePC1Table(len(key))

# key=permutedChoice(key,x)

# y=generatePC2Table(len(key))
# print(y==pc2Table)

# key1=leftShift(key,1)
# key2=leftShift(key1,2)
# key1=permutedChoice(key2,y)
# print(bin2hex(key1))