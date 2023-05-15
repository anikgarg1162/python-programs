def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final


dict = {'a': 222, 'b': 111, 'c': 555}
print("Sum :", returnSum(dict))
