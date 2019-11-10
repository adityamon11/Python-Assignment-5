def main():
	x = int(input("Enter a number"));
	pattern(x);

def pattern(x):
	if(x>0):
		print("*",end = " ");
		x= x-1
		pattern(x);


if __name__ == '__main__':
	main();