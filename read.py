data = []
count = 0

with open('reviews.txt', 'r') as f:
	 for line in f:
	 	data.append(line)
	 	# print(len(data))
	 	count += 1 #count = count + 1
	 	if count % 100000 == 0:
	 		print(len(data)) 

print('檔案讀取玩了，總共有', len(data), "筆資料")

# print(len(data))

# print(data)
# print(data[0])
# print("-------")
# print(data[1])


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	#print(sum_len)

print('平均是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度<100')
print(new[0])
print(new[1])