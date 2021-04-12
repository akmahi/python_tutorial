''' 
	params: 
		expr = input expression	
		k = input dictionary
'''

def test(ex,k):
	t = ex.split()
	temp = []
	no_var = ['and', 'or']
	for i in t:
		if i.startswith('('):
			temp.append(i[1:])
		elif i.endswith(')'):
			temp.append(i[:-1])
		else:
			temp.append(i)
	for j in temp:
		if j not in k.keys() and j not in no_var:
			k[str(j)] = ""

	ex = ex.replace('and', '+')
	return eval(ex, k)


if __name__ == '__main__':
	expr = 'A and (C or D)'
	k = {'A':'Hello', 'B': 'World', 'C': 'Buddy'} 
	print test(expr,k)






