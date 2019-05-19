rent_list = [[1,5],[4,10],[5,9],[11,16],[16,20],[17,23]]
# rent_list = [[0,6],[6,10],[11,16],[17,20],[20,21],[22,23]]
def rent(rent_list):
	# rent_list = sorted(rent_list)
	# print(rent_list)
	flat_list = [item for sublist in rent_list for item in sublist]
	# print(flat_list)
	x = 0
	for i in flat_list:
		if x > i:
			return 'Не хватит одной ракеты, чтобы выполнить все заказы'
		else:
			x = i
	return 'Все заказы выполнимы'



print(rent(rent_list))
