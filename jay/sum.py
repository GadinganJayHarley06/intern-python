def allsum_recursive(mylist):
	if len(mylist) == 1:
		return mylist[0]
	return(mylist[0]+allsum_recursive(mylist[1:]))

print(allsum_recursive((50, 40, 3, 25, 25)))