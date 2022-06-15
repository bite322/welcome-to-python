a: int = 12
b: int = 45
c: int = 75

def main():
	global a
	global b
	global c
	if a > b and a > c:
		max = a
	elif b > a and b > c:
		max = b
	elif c > a and c > b:
		max = c
	print(max)
	pass


if __name__ == "__main__":
	main()