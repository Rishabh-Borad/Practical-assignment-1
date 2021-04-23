from keygeneration import *
from round import *

# Table of Position of 64 bits at initail level: Initial Permutation Table
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2, 
                60, 52, 44, 36, 28, 20, 12, 4, 
                62, 54, 46, 38, 30, 22, 14, 6, 
                64, 56, 48, 40, 32, 24, 16, 8, 
                57, 49, 41, 33, 25, 17, 9, 1, 
                59, 51, 43, 35, 27, 19, 11, 3, 
                61, 53, 45, 37, 29, 21, 13, 5, 
                63, 55, 47, 39, 31, 23, 15, 7] 


# Final Permutaion Table
final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32, 
               39, 7, 47, 15, 55, 23, 63, 31, 
               38, 6, 46, 14, 54, 22, 62, 30, 
               37, 5, 45, 13, 53, 21, 61, 29, 
               36, 4, 44, 12, 52, 20, 60, 28, 
               35, 3, 43, 11, 51, 19, 59, 27, 
               34, 2, 42, 10, 50, 18, 58, 26, 
               33, 1, 41, 9, 49, 17, 57, 25 ]


#function to generate initial permutation table
#size : number of bits in message
def generateIPTable(size):
	if size==64:
		return initial_perm

	arr=[i for i in range(1,size+1)]
	shuffle(arr)
	return arr
	
#function to generate inverse initial permutation table
#ipTable : initial permutation table generated using generateIPTable()
def generateInvIPTable(ipTable):
	return inversePermutation(ipTable)
	
#function to permute message w.r.t. initial permutation table
#msg : message in binary format
#ipTable : initial permutation table
def initialPermutation(msg,ipTable):
	return permute(msg,ipTable,len(ipTable))

#function to permute message w.r.t. inverse initial permutation table
#msg : message in binary format
#ipTable : initial permutation table
def invIP(msg,invIPTable):
	return permute(msg,invIPTable,len(invIPTable))

#function to encrypt an array of messages using DES
#msgArr : array of messages in binary format
#keys : list of round keys
#numRounds : number of rounds
#ipTable : initial permutation table
#invIPTable : inverse initial permutation table
#pT : permutation table
#eT : expansion table
def DES(msgArr,keys,numRounds,ipTable,invIPTable,pT,eT):
	out=[]
	roundOut=[]
	for msg in msgArr:
		x=msg
		msg=initialPermutation(msg,ipTable)
		for i in range(numRounds):
			msg=round(msg,keys[i],pT,eT)
			if i==numRounds-1:
				msg1=msg[len(msg)//2:]
				msg1=msg1+msg[:len(msg)//2]
				msg=msg1
			roundOut.append(msg)

		msg=invIP(msg,invIPTable)
		out.append(msg)
		
	return out,roundOut
