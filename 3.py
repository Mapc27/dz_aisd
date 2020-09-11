a = int(input())
#10000
x = y = 0
for i in ['n','ch','n','ch','n']:
	if i == 'n':
		y += a % 10
	else:
		x += a % 10
	a = a // 10
print(x-y)