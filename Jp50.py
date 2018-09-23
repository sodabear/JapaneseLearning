import random
a = 'あいうえおかきくけこ'
b = 'さしすせそたちつてと'
c = 'なにぬねのはひふへほ'
d = 'まみむめもやゆよらりるれろわをわを'

aa =' a i u e okakikukeko'
bb ='sasisusesotatituteto'
cc ='naninunenohahifuheho'
dd ='mamimumemoyayuyorarirurerowawo'

aaa = [[a[i] , aa[i*2:i*2+2]] for i in range(10)]
bbb = [[b[i] , bb[i*2:i*2+2]] for i in range(10)]
ccc = [[c[i] , cc[i*2:i*2+2]] for i in range(10)]
ddd = [[d[i] , dd[i*2:i*2+2]] for i in range(16)]
#print(aaa)
#print(bbb)
#print(ccc)
#print(ddd)

row1 = input() 
store = ["aaa", "bbb", "ccc", "ddd"]
dic ={ "aaa": aaa, "bbb": bbb, "ccc": ccc, "ddd":ddd}	

for i in range(4):
	if row1 == store[i]:
		row = dic[store[i]]
		break
	else:
		print("invaild input")

while True: 
	if row1 != "ddd":
		x = random.randint(0,9)	
	else: 
		x = random.randint(0,15)

	print('what is ', row[x][0], '?')
	y = input()
	if y != row[x][1]:
		print('wrong. remember answer: ', row[x][1])
	else:
		print('right')

	print("-----Next-------")

# add timer feature to this
# expanding feature of adutograding
print(row)
