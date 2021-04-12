# Allow only range of One Billion

'''
	params:
		default_input = input number
		
'''

def div_based_on_len(k,s):
	if k == 1:
		return first[s]
	elif k == 2:
		result = ''
		div = int(s/10)
		rem = s%10
		if s > 19:
			result = second[div] + first[rem]
		else:
			result = first[s] 
		return result
	elif k == 3:
		div = int(s / 100)
		rem = s % 100
		return first[div] + "Hundred " + div_based_on_len(len(str(rem)),rem)
	elif k == 4 or k == 5:
		div = int(s/1000)
		rem = s % 1000
		if y > 19:
			return first[div] + "Thousand " + div_based_on_len(len(str(rem)),rem)
		else:	
			return second[div] + "Thousand " + div_based_on_len(len(str(rem)),rem)
	elif k == 6:
		div = int(s / 1000)
		rem = s % 1000
		return  div_based_on_len(len(str(div)),div) + "Thousand " + div_based_on_len(len(str(rem)),rem)
	elif k == 7 or k == 8:
		div = int(s/1000000)
		rem = s % 1000000
		if div > 19:
			return second[div] + "Million " + div_based_on_len(len(str(rem)),rem) 
		else:
			return first[div] + "Million " + div_based_on_len(len(str(rem)),rem) 
	elif k == 9:
		div = int(s/1000000)
		rem = s % 1000000
		return div_based_on_len(len(str(div)),div)  + "Million " + div_based_on_len(len(str(rem)),rem) 
	elif k == 10:
		div = int(s/1000000000)
		rem = s % 1000000000
		if div > 19:
			return second[div] + "Billion " + div_based_on_len(len(str(rem)),rem) 
		else:
			return first[div] + "Billion " + div_based_on_len(len(str(rem)),rem) 
	else:
		return "Input Range Allow Only--ONE BILLION "


if __name__ == '__main__':
	
	first = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
		"Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
		"Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
		"Seventeen ", "Eighteen ", "Nineteen "]

	second = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
	default_input = '15454845859'
	length_of_given_no = len(default_input)
	output = div_based_on_len(length_of_given_no,int(default_input)) 
	output = output + "Dollar"
	print output
