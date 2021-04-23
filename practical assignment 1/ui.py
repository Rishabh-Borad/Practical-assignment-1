#importing DES library created here
from avalanche import *
#importing tkinter
from tkinter import *

#function to encrypt data
#msg : data in hexadecimal format
#keys : list of round keys
#numRounds : number of rounds to be completed in encryption
#halfwidth : half of the size of message(in binary)
def encrypt(msg,keys,numRounds,halfwidth):
	msgArr=[hex2bin(msg)]

	#generating  proper tables
	global ipTable
	global invIPTable
	global pt
	global et
	ipTable=generateIPTable(2*halfwidth)
	invIPTable=generateInvIPTable(ipTable)
	pt=generatePermutationTable(halfwidth)
	et=generateExpansionTable(halfwidth)

	#enryption using DES()
	x,roundCipherText = DES(msgArr,keys,numRounds,ipTable,invIPTable,pt,et)
	out=""
	for i in x:
		out+=bin2hex(i)

	return out,roundCipherText

#function to decrypt encrypted message
#msg : data in hexadecimal format
#keys : list of round keys
#numRounds : number of rounds to be completed in decryption
#ipTable : initial permutation table generated in encrypt()
#invTable : inverse permutation of initial permutation table
#pt : permutation table for F() of each round, this is also generated in encrypt()
#et : expansion table for F() of each round, this is also generated in encrypt()
def decrypt(msg,keys,numRounds,ipTable,invIPTable,pt,et):
	keys=keys[::-1]
	msgArr=[hex2bin(msg)]
	x,_ = DES(msgArr,keys,numRounds,ipTable,invIPTable,pt,et)
	out=""
	for i in x:
		out+=bin2hex(i)
	return out


#function to read data, encrypt/decrypt it and write it on required text field
#read : text field containing data
#write : text field which will contain output data
#enc : boolean variable to tell the function whether to perform encryption or decryption
#keys : round keys for encryption
#numRounds : number of rounds
#halfwidth : half of size of message to be encrypted/decrypted(in binary)
def putText(read,write,enc,keys,numRounds,halfwidth):
	msg=read.get("1.0",END)
	write.delete("1.0",END)
	if enc:
		x,_=encrypt(msg,keys,numRounds,halfwidth)
		write.insert("1.0",x)
	else:
		write.insert("1.0",decrypt(msg,keys,numRounds,ipTable,invIPTable,pt,et))


#function to set number of rounds and generate keys which depend on number of rounds
def setRounds(nRounds,keyEntry):
	global numRounds
	numRounds=nRounds.get()
	if keyEntry.get("1.0",END)!="\n":
		preprocess(keyEntry,numRounds)

#function to set halfwidth
def setHalfWidth(halfwidths):
	global halfwidth
	halfwidth=halfwidths.get()

#function to test avalanche effect for keys
#msg1 : one of the messages given for encryption
#msg2 : other message given for encryption
#key : key used for encryption
#numRounds : number of rounds for DES
#halfwidth : half of the size of message
def testAvalancheForMessages(msg1,msg2,key,numRounds,halfwidth):
	ipTable=generateIPTable(2*halfwidth)
	invIPTable=generateInvIPTable(ipTable)
	pt=generatePermutationTable(halfwidth)
	et=generateExpansionTable(halfwidth)

	msgArr1=[hex2bin(msg1)]
	msgArr2=[hex2bin(msg2)]

	# key=hex2bin(key)
	pc2Table=generatePC2Table(len(key))
	keys=generateRoundKeys(numRounds,key,pc2Table)

	_,roundCipherText1=DES(msgArr1,keys,numRounds,ipTable,invIPTable,pt,et)
	_,roundCipherText2=DES(msgArr2,keys,numRounds,ipTable,invIPTable,pt,et)

	return avalanche(roundCipherText1,roundCipherText2)


#function to test avalanche effect for keys
#msg : message given for encryption
#key1 : one of the keys, other key will be generated such that it differs from key1 by only 1 bit
#numRounds : number of rounds for DES
#halfwidth : half of the size of message
def testAvalancheForKeys(msg,key1,numRounds,halfwidth):
	ipTable=generateIPTable(2*halfwidth)
	invIPTable=generateInvIPTable(ipTable)
	pt=generatePermutationTable(halfwidth)
	et=generateExpansionTable(halfwidth)

	msgArr=[hex2bin(msg)]
	key2=""
	change=randint(0,len(key1))
	for i in range(len(key1)):
		if i==change:
			key2=key2+str(int(not int(key1[i])==1))
		else:
			key2+=key1[i]
	pc2Table=generatePC2Table(len(key1))
	keys1=generateRoundKeys(numRounds,key1,pc2Table)
	
	pc2Table=generatePC2Table(len(key2))
	keys2=generateRoundKeys(numRounds,key2,pc2Table)
	_,roundCipherText1=DES(msgArr,keys1,numRounds,ipTable,invIPTable,pt,et)
	_,roundCipherText2=DES(msgArr,keys2,numRounds,ipTable,invIPTable,pt,et)

	return avalanche(roundCipherText1,roundCipherText2)

#function to test avalanche effect in DES for different variables
#entry1 : text field containing one of the two inputs which differ by 1 bit
#entry2 : text field containing another message input, if None then entry1 will be one of the keys and another key is generated randomly such that 
#difference between two keys is only of 1 bit
#entry : message field is avalanche for keys is tested and key field otherwise
#numRounds : number of rounds in DES
#halfwidth : half of the size of message/key
#testMessage : boolean variable which tells the function to test for message(True) or keys(False)
def testAvalanche(entry1,entry2,entry,numRounds,halfwidth,testMessage):
	
	avaEntries=[]
	roundNumberEntries=[]
	ava=Tk()
	rl=Label(ava,text="Rounds",font=("Times New Roman",14))
	bl=Label(ava,text="Change in bits",font=("Times New Roman",14))
	msg1=entry1.get("1.0",END)
	msg2=""
	if entry2 != None:
		msg2=entry2.get("1.0",END)
	key=entry.get("1.0",END)

	if testMessage:
		ava.title("Avalanche for messages")
		key=hex2bin(key)
		pc1Table=generatePC1Table(len(key))
		key=permutedChoice(key,pc1Table)
		out=testAvalancheForMessages(msg1,msg2,key,numRounds,halfwidth)
		
		avaEntries=[Text(ava,width=10,height=1) for i in range(numRounds)]
		roundNumberEntries=[Label(ava,text=str(i),font=("Times New Roman",14)) for i in range(1,numRounds+1)]
		for i in range(numRounds):
			avaEntries[i].insert("1.0",str(out[i]))
			roundNumberEntries[i].grid(row=9+i,column=0)
			avaEntries[i].grid(row=9+i,column=1)
	else:
		ava.title("Avalanche for keys")
		msg1=hex2bin(msg1)
		pc1Table=generatePC1Table(len(msg1))
		msg1=permutedChoice(msg1,pc1Table)
		out=testAvalancheForKeys(key,msg1,numRounds,halfwidth)
		
		avaEntries=[Text(ava,width=10,height=1) for i in range(numRounds)]
		roundNumberEntries=[Label(ava,text=str(i),font=("Times New Roman",14)) for i in range(1,numRounds+1)]
		for i in range(numRounds):
			avaEntries[i].insert("1.0",str(out[i]))
			roundNumberEntries[i].grid(row=9+i,column=0)
			avaEntries[i].grid(row=9+i,column=1)

	rl.grid(row=0,column=0)
	bl.grid(row=0,column=1)
	ava.mainloop()


#function to print all keys
#keys : list of keys for all rounds
def printAllKeys(keys):
	keyOut=Tk()
	keyOut.title("keys")
	numRounds=len(keys)
	avaEntries=[Text(keyOut,width=10,height=1) for i in range(numRounds)]
	roundNumberEntries=[Label(keyOut,text=str(i),font=("Times New Roman",14)) for i in range(1,numRounds+1)]

	for i in range(numRounds):
		avaEntries[i].insert("1.0",bin2hex(keys[i]))
		roundNumberEntries[i].grid(row=i,column=0)
		avaEntries[i].grid(row=i,column=1)

	keyOut.mainloop()


#function to generate round keys
#keyEntry : text field containing key in hexadecimal format
#numRounds : number of rounds
def preprocess(keyEntry,numRounds):
	key=keyEntry.get("1.0",END)
	key=hex2bin(key)
	global pc1Table
	pc1Table=generatePC1Table(len(key))
	key=permutedChoice(key,pc1Table)
	global pc2Table
	pc2Table=generatePC2Table(len(key))
	global keys
	keys=generateRoundKeys(numRounds,key,pc2Table)
	
	
#required initialisations
numRounds=16
halfwidth=32

keys=[]

root=Tk()
root.title("DES")

frame=LabelFrame(root,text="",padx=10,pady=10)

#Plaintext Label
ptl=Label(root,text="PLAINTEXT",font=("Times New Roman",14))
#Ciphertext Label
ctl=Label(root,text="CIPHERTEXT",font=("Times New Roman",14))
#Key Label
keyl=Label(root,text="KEY",font=("Times New Roman",14))

#Key text field
keyEntry=Text(root,width=50,height=1)
#Plaintext field
pte=Text(root,width=50,height=10)
#Ciphertext field
cte=Text(root,width=50,height=10)

#-----------------------------------------avalanche---------------------------------------------


ml1=Label(root,text="PLAINTEXT1",font=("Times New Roman",14))
ml2=Label(root,text="PLAINTEXT2",font=("Times New Roman",14))
kl=Label(root,text="KEY",font=("Times New Roman",14))

#message for avalanche field
m1=Text(root,width=50,height=1)
#message for avalanche field
m2=Text(root,width=50,height=1)
#key for avalanche field
k=Text(root,width=50,height=1)


kl1=Label(root,text="KEY",font=("Times New Roman",14))
ml=Label(root,text="PLAINTEXT",font=("Times New Roman",14))
#key for avalanche field
k1=Text(root,width=50,height=1)
#key for avalanche field
# k2=Text(root,width=50,height=1)
#message for avalanche field
m=Text(root,width=50,height=1)

#test avalanche for message button
tam=Button(root,text="Test avalanche for messages",font=("Times New Roman",14),command=lambda:testAvalanche(m1,m2,k,numRounds,halfwidth,True))
#test avalanche for key button
tak=Button(root,text="Test avalanche for keys",font=("Times New Roman",14),command=lambda:testAvalanche(k1,None,m,numRounds,halfwidth,False))

#------------------------------------------------------------------------------------------------

#Button to set key
keyb=Button(root,text="set key",command=lambda:preprocess(keyEntry,numRounds))
#Encryption button
ptb=Button(root,text=">>Encipher>>",font=("Times New Roman",14),command=lambda:putText(pte,cte,True,keys,numRounds,halfwidth))
#Decryption button
dtb=Button(root,text="<<Decipher<<",font=("Times New Roman",14),command=lambda:putText(cte,pte,False,keys,numRounds,halfwidth))

#button to print all keys
printKeys=Button(root,text="print keys",command=lambda:printAllKeys(keys))


#variables to get value of numRounds and halfWidth from radio buttons
nRounds=IntVar()
halfwidths=IntVar()

#label for number of rounds
nRLabel=Label(frame,text="Number of rounds",font=("Times New Roman",14))
#label for halfwidth
hLabel=Label(frame,text="halfWidth",font=("Times New Roman",14))
#label for space
sLabel=Label(frame,text="   ",font=("Times New Roman",14))

#Radiobuttons for numRounds
r1=Radiobutton(frame,text=" 1",value="1",variable=nRounds,command=lambda:setRounds(nRounds,keyEntry))
r2=Radiobutton(frame,text=" 8",value="8",variable=nRounds,command=lambda:setRounds(nRounds,keyEntry))
r3=Radiobutton(frame,text="16",value="16",variable=nRounds,command=lambda:setRounds(nRounds,keyEntry))
r4=Radiobutton(frame,text="32",value="32",variable=nRounds,command=lambda:setRounds(nRounds,keyEntry))

#Radiobuttons for halfWidth
h1=Radiobutton(frame,text="16",value="16",variable=halfwidths,command=lambda:setHalfWidth(halfwidths))
h2=Radiobutton(frame,text="32",value="32",variable=halfwidths,command=lambda:setHalfWidth(halfwidths))
h3=Radiobutton(frame,text="64",value="64",variable=halfwidths,command=lambda:setHalfWidth(halfwidths))


#Positioning of all the fields in UI
ptl.grid(row=0,column=0,pady=10)
ctl.grid(row=0,column=2,pady=10)
keyl.grid(row=3,column=1)

pte.grid(row=1,column=0,rowspan=2)
cte.grid(row=1,column=2,rowspan=2)
keyEntry.grid(row=4,column=1)

keyb.grid(row=5,column=1)
ptb.grid(row=1,column=1,padx=15)
dtb.grid(row=2,column=1,padx=15)

printKeys.grid(row=5,column=2)

frame.grid(row=5,column=0)

nRLabel.grid(row=0,column=0)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)
r4.grid(row=4,column=0)

sLabel.grid(row=0,column=1)

hLabel.grid(row=0,column=2)
h1.grid(row=1,column=2)
h2.grid(row=2,column=2)
h3.grid(row=3,column=2)

ml1.grid(row=6,column=0)
kl.grid(row=8,column=0)
ml2.grid(row=10,column=0)
m1.grid(row=7,column=0)
k.grid(row=9,column=0)
m2.grid(row=11,column=0)
tam.grid(row=12,column=0)


ml.grid(row=6,column=2)
kl1.grid(row=8,column=2)
k1.grid(row=9,column=2)
m.grid(row=7,column=2)
# k2.grid(row=10,column=2)

tak.grid(row=10,column=2)

root.mainloop()
