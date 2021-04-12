import json

def find_diff(f,s):
	result = []
	com_keys = list(f.keys()) + list(s.keys())
	com_keys = set(com_keys)
	if type(f) != type(s):
		return "Type doesn't Match"
	else:
		for i in com_keys:
			if i in f.keys() and isinstance(f[i],dict):
				temp = ''
				if i in s.keys() and isinstance(s[i], dict):
					temp += "in" + i + str(find_diff(f[i], s[i]))
				else:
					temp += "in" + i + str(find_diff(f[i], {}))
				result.append(temp)
			else:
				temp1 = ''
				if i in f.keys() and i in s.keys():
					if f[i] != s[i]:
						temp1 += "%s changed from %s to %s" %(i, f[i], s[i])
				elif i in f.keys():
					temp1 += "%s added to %s " %(i, f[i])
				else:
					temp1 += "%s added to %s " %(i, s[i])
				result.append(temp1)
		return result

if __name__ == "__main__":
	first_json = {"name":"Ajith", "age":23, "team":{"name":"fir","file":"yes","check":{"name":"gry"}}}
	second_json = {"name":"Ajith1", "age":26, "team":{"name":"fir1","file":"yes1"}}
	print find_diff(first_json, second_json)
