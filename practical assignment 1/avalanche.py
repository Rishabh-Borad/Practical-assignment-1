from DES import *
import matplotlib.pyplot as plt

#function to test avalanche effect
def avalanche(roundCipherText1,roundCipherText2):
	difference=[]
		
	for i in range(len(roundCipherText1)):
		diff=0
		for j in range(len(roundCipherText1[i])):
			if roundCipherText1[i][j]!=roundCipherText2[i][j]:
				diff+=1
		difference.append(diff)
	return difference


# msg="0000000000000000"
# msg1="0000000000000001"
# kk="00000011001011010010011000100011100001100000111000110010"

# key="AABB09182736CCDD"
# numRounds=16

# halfwidth=32

# key=hex2bin(key)
# key1=key
# # global pc1Table
# pc1Table=generatePC1Table(len(key))
# key=permutedChoice(key,pc1Table)
# # global pc2Table
# pc2Table=generatePC2Table(len(key))
# # global keys
# keys=generateRoundKeys(numRounds,kk,pc2Table)

# ct,roundCipherText=encrypt(msg,keys,numRounds,halfwidth)
# ct1,roundCipherText1=encrypt(msg1,keys,numRounds,halfwidth)
# difference=avalanche(roundCipherText,roundCipherText1)
# print(difference)