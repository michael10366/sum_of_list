#sum_of_list


# def sum_of_list():	#寫在FUNCTION內
# 	inputlist = []
# 	x = 0
# 	while True:
# 		inputdata = input('請輸入清單，按q離開')
# 		if inputdata == 'q':
# 			break
# 		inputlist.append(inputdata)	
	
# 	for i in inputlist:
# 		x = x + int(i)

# 	print(inputlist)
# 	return x


# print(sum_of_list())

def sum_of_list(inputdata):    #寫在FUNCTION外
		x = 0
		for i in inputdata:
			x = x + int(i)
		print(inputdata)
		return x

data = []
while True:
	userinput = input('請輸入數字,輸入q離開')
	if userinput == 'q':
		break
	data.append(userinput)

print(sum_of_list(data))