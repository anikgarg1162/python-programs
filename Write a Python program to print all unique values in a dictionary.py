test_list =[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
{"V":"S009"},{"VIII":"S007"}]

print("The original list : " + str(test_list))

res=[]
for i in test_list:
	res.extend(list(i.values()))
res=list(set(res))

print("The unique values in list are : " + str(res))
