def main():
	x = int(input("Enter a number"));
	pattern(x);

def pattern(x):
	if(x>0):		
		x= x-1
		pattern(x);
		print(x+1,end = " ");

if __name__ == '__main__':
	main();