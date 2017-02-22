import sys
import time
import argparse
from caesar_cipher import encryptAndDecrypt as encDec

def bruteForce(encryptedWord,start_time):
	alpha = ["A","B","C","D","E",
	"F","G","H","I","J","K","L",
	"M","N","O","P","Q","R","S",
	"T","U","V","W","X","Y","Z","."]
	for i in range(len(alpha)):
		print(encDec(i,encryptedWord,False) + "\n" + (len(encryptedWord)*"-"))
	return ("Done in: %s seconds" % str(time.time()-start_time))

def main():
	parser = argparse.ArgumentParser(description="A brute-force attack on the Caesar Cipher.")
	parser.add_argument("em", help="The encrypted message.")
	args = parser.parse_args()
	start_time = time.time()

	if args.em:
		print(bruteForce(args.em,start_time))
	else:
		print(args)

if __name__ == '__main__':
	sys.exit(main())