import re 
data = ['int','char','float','void']
f = open("program.c","r") 
st = f.read()
flag = False
table = {}
fun={}
st = st.split('\n')
ch=""
for i in st:
	i= i.replace(';',' ;')
	i = i.replace(')',' )')
	i = i.replace('(',' (')
	i = re.split(',|\s',i)
	print(i)
	for j in range(len(i)):
		if i[j] in data:
			j+=1
			
			if i[j+1]=='(':
				try:	

					j+=2
					while i[j]!=')':
						if i[j] not in data:
							fun[i[j]]=i[1]
						j+=1
				except:
					break
				
			else:
				try:
					
					while i[j]!=';':
						table[i[j]]=i[0]
						j+=1
				except:
					break
			
		else:	
			break
print(table.items())
print(fun.items())
