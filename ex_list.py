list_data = [input()]
for elem in input().split():
	if elem.isdigit(): # If elem is a digit, then convert to int.
		list_data.append(int(elem))
	else:
		list_data.append(elem)


