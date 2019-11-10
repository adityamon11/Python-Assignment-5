def main():
	x = int(input("Enter a number"));
	prod=1;
	if(x>0):
		fact(x,prod);
	else:
		print("1");

def fact(x,prod):
	if(x!=0):
		prod=prod*x;
		x=x-1;
		fact(x,prod);
	else:
		print(prod);



if __name__ == '__main__':
	main();