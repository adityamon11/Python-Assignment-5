def main():
	x = int(input("Enter a number"));
	sumA=0;
	summation(x,sumA);
	
def summation(x,sumA):
	if(x!=0):
		sumA=(sumA+(x%10))
		x=x//10;
		summation(x,sumA);
	else:
		print(sumA);
		

	

if __name__ == '__main__':
	main();