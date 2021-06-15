# SOLUTION IN PROGRESS.....
# 0 ,0, 5, 5, 50, 50, 55, 55, 500, 500, 550, 550, 555, 555

n = 32
five_list = []
# fg = [0,5,50,55,500,550,555,5000,5500,5550,5555,50000]

# 1
# 2, 1
# 5000, 5000 + 500, 5500 + 50, 5550 + 5, # 3, 2, 1
# 2 + i = res
# res + 2
# res + 1
# res + 1

fg = [0,5,50]
# res 1, 2, 3, 
res = 2
i = 0
slow = 0

# for x in range(len(fg)-1):
# 	try:
# 		if x < 3:
# 			print(fg[x])
# 		else:
# 			print(fg[(x-1) + res])
# 			res += i
# 			i += 1
# 	except IndexError:
# 		break

for x in range(len(fg)):
	try:
		if i % 2 == 0:
			print("yes")
			fg.append(fg[i] + fg[i - 1])
		elif i % 2 != 0:
			if x < 3:
				fg.append(fg[i] * 10)
			else:
				fg.append(fg[i] * 10)
				slow += 1
	except IndexError:
		break

print(fg)
# for i in range(10000):
# 	if i // 2 in fs:
# 		print(i)
