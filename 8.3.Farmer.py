summa = int(input())
number = int(input())
def buy(rec, sum, number, lst = None):
	if lst == None:
		lst = []
	else:
		lst = lst.copy()
	if rec == 2:
		if (summa % (number * 5) == 0) and (summa - number * 5 == 0):
			list.append(number)
			print(lst)
		else:
			return
	if rec == 0:
		lst.append(0)
		i = 0
		while sum >= 0:
			i += 1
			sum -= 20
			number -= 1
			lst[0] = i
			buy(1, sum, number, lst)
	if rec == 1:
		lst.append(0)
		i = 0
		while sum >= 0:
			buy(2, sum, number, list)
			i += 1
			sum -= 10
			number -= 1
			lst[1] = i
buy(0, sum, number)