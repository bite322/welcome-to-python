a: int = 12
b: int = 45
c: int = 75
d: int = 32

def sort_a_b_c_d():
	global a
	global b
	global c
	global d
	arr = [a, b, c, d]
	arr.sort(reverse = True)
	a = arr[0]
	b = arr[1]
	c = arr[2]
	d = arr[3]

	pass

def main():
	print("=== BEFORE sort_a_b_c_d() ===")
	print("A: {0}".format(a))
	print("B: {0}".format(b))
	print("C: {0}".format(c))
	print("D: {0}".format(d))

	sort_a_b_c_d()

	print("=== AFTER sort_a_b_c_d() ===")
	print("A: {0}".format(a))
	print("B: {0}".format(b))
	print("C: {0}".format(c))
	print("D: {0}".format(d))
	pass

if __name__ == "__main__":
	main()