import argparse
import sys

def encryptAndDecrypt(n,word,dec):
	alpha = ["A","B","C","D","E",
	"F","G","H","I","J","K","L",
	"M","N","O","P","Q","R","S",
	"T","U","V","W","X","Y","Z","."]
	wordList = list(word.upper())
	newWord = ""

	for i in wordList:
		alphaIndex = alpha.index(i)
		if dec == True:
			xn = alphaIndex-n
		elif dec == False:
			xn = alphaIndex+n
		xnMod = xn%27
		newWord = newWord+alpha[xnMod]
	return(newWord)


def main():
	parser = argparse.ArgumentParser(description="A python 3 tool to encrypt and decrypt messages using the Caesar cipher.\
	Use '.' for spaces and omit punctuation. Either -e OR -d IS required to run the program.")
	parser.add_argument("s", type=int, help="The number of letters to shift the message by.")
	parser.add_argument("m", help="Message to encrypted/decrypted.")
	parser.add_argument("-e", "--encrypt", action="store_true", help="encrypt the message.")
	parser.add_argument("-d", "--decrypt", action="store_true", help="decrypt the message.")
	args = parser.parse_args()

	if args.encrypt:
		print(encryptAndDecrypt(args.s,args.m,False))
	elif args.decrypt:
		print(encryptAndDecrypt(args.s,args.m,True))
	else:
		print(args)


if __name__ == '__main__':
    sys.exit(main())