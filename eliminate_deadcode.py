with open("output") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
used = {} #var: (0: unused 1:used) (line number of last use on LHS)
remove_lines=[]
def add_to_used(d , v, line):
	if v in d.keys():
		if(d[v][0]==0):
			remove_lines.append(d[v][1])
		d[v][0] = 0
		d[v][1] = line
	else:
		if(('[' in v) and (']' in v)):
			v = v.split('[')[0]
		print("added " , v)
		d[v] = [0,0]
		d[v][0] = 0
		d[v][1] = line
def mark_used(used, l):
	for x in l:
		if(('[' in x) and (']' in x)):
			z = x.split('[')
			x = z[0]
			b = z[1]
			if b in used.keys():
				used[b][0]=1			
		if x in used.keys():
			print("mark " , x)
			used[x][0] = 1
i=0
content2 = content
remove_lines = [1]	
while(remove_lines != [] or content!=[]):
	remove_lines=[]	
	i=0	
	used={}
	for x in content:
		i+=1
		y = x.split("\t")
		print(y)
		if('=' in y):
			z = y.index('=')
			if(y[z+1]!= '='):
				mark_used(used, y[z+1:])
				add_to_used(used , y[z-1] , i)
				 
		else:
			mark_used(used, y) 
	for x in used.keys():
		if(used[x][0]==0):
			remove_lines.append(used[x][1])
	#print(remove_lines)
	if(remove_lines == []):
		break
	remove_lines = set(remove_lines)

	remove_lines = list(remove_lines)

	remove_lines.sort()
	print(remove_lines)
	temp=[]
	for index in range(len(content)):
		if(index+1 not in remove_lines):
			temp.append(content[index])
	content = temp
	if(content ==[]):
		break
	print(content)
			
		
f= open("output_optimized","w")
for x in content:
		f.write(x)
		f.write('\n')
f.close()
