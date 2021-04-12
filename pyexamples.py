"""
Evaluate given expression which has factorials and exponential terms.
input = 1+2*5+3
output = 18
"""
def check_number(k):
	return '0' <= k <= '9'

def ev_ate(s):
	length_of_expr = len(s.strip())
	if length_of_expr < 3:
		return "Invalid Expr"
	else:
		result = int(s[0])
		for i in range(1,length_of_expr,2):
			op_ran = s[i]
			last_val = s[i+1]
			if not check_number(last_val):
				return -1
			else:
				if op_ran == '+':
					result = result + int(last_val)
				elif op_ran == '-':
					result = result - int(last_val)
				elif op_ran == '*':
					result = result * int(last_val)
				elif op_ran == '/':
					result = result / int(last_val)
		return result

if __name__ == '__main__':
	print ev_ate('1+2*5+3')

"""
Find the  Is_square from given points
input 1 = (2,1), (10,20), (5,6), (10,10)    Output =  False
input 2 = (20,10), (10,20), (20,20),(10,10) Output = True 
"""


def is_square(p1,p2,p3,p4):
	l = abs(p1[0]-p2[0])-abs(p3[0]-p4[0])
	k = abs(p1[1]-p2[1])-abs(p3[1]-p4[1])
	return l == k


if  __name__ == '__main__':
	print is_square((20,10), (10,20), (20,20),(10,10))
	print is_square((2,1),(10,20), (5,6), (10,10))


"""
Insert 0 after consecutive (K times) of 1 is found.

Input:
Number of bits: 12
Bits: 1 0 1 1 0 1 1 0 1 1 1 1
Consecutive K: 2

Output:
1 0 1 1 0 0 1 1 0 0 1 1 0 1 1 0
"""

def add_zero(s):
	result = []
	for i in range(0,len(s),2):
		if s[i] == s[i+1]:
			result.append(s[i])
			result.append(s[i+1])
			result.append('0')
		else:
			result.append(s[i])
			result.append(s[i+1])
	return result

if __name__ == '__main__':
	print (add_zero('101101101111'))
	print (add_zero('1111'))