verbose = False
def fact(n):
	if n==0:
		return 0
	j=1
	for i in range(1,n):
		j*=i+1
	return j
while True:
    value = list(input("> "))
    if verbose:
        print(value)
    pointer = 0
    parsed = []
    join = ""
    #Parsing start
    while True:
        workingValue = value[pointer]
        pointer+=1
        if workingValue == " ":
            continue
        isNumber = False
        try:
            int(workingValue)
            isNumber = True
        except:
            if workingValue==".":
                isNumber = True
        if not isNumber:
            if not len(join) == 0:
                parsed.append(join)
                if verbose:
                	print(parsed)
                join = ""
            parsed.append(workingValue)
            if workingValue=="!":
            	if verbose:
            		print(parsed)
            	parsed.append("")
            if verbose:
            	print(parsed)
        else:
            join += workingValue
        if pointer == len(value):
            if not len(join) == 0:
                parsed.append(join)
            if verbose:
                print(parsed)
            break
    #Parsing end
    #Lexing start
    pointer = 0
    lexTree = parsed
    priorities = []
    while True:
    	reading=lexTree[pointer]
    	if reading=="^" or reading=="!":
    		priorities.append(pointer)
    	pointer+=1
    	if pointer==len(parsed):
    		break  		
    pointer=0
    while True:
            reading = lexTree[pointer]
            if reading == "*" or reading == "/":
                priorities.append(pointer)
            pointer += 1
            if pointer == len(parsed):
                break
    pointer = 0
    while True:
            reading = lexTree[pointer]
            if reading == "+" or reading == "-":
                priorities.append(pointer)
                if verbose:
                    print(priorities)
            pointer += 1
            if pointer == len(parsed):
                break
    #Lexing end
    #Calculating start
    alloffsets={}
    total=0
    for i in priorities:
        total+=i
    for i in range(total+1):
        alloffsets[i]=0
    pointer = 0
    offset = 0
    if not len(parsed) == 1:
        location = priorities[pointer]
    if verbose:
        print(lexTree)
    while True:
        if len(parsed) == 1:
            break
        location = priorities[pointer]
        if verbose:
                print(alloffsets)
        for i in range(location):
                if alloffsets[i]  < location:
                    location -= alloffsets[i]
        operation = lexTree[location]
        if operation == "!":
            first = lexTree[location-1]
            value = fact(float(first))
            lexTree.pop(location+1)
            lexTree.pop(location)
            lexTree.pop(location-1)
            lexTree.insert(location-1,str(value))
            alloffsets[location]=alloffsets[location]+2
        elif operation == "^":
            first = lexTree[location-1]
            second = lexTree[location+1]
            value = float(first) ** float(second)
            lexTree.pop(location+1)
            lexTree.pop(location)
            lexTree.pop(location-1)
            lexTree.insert(location-1,str(value))
            alloffsets[location]=alloffsets[location]+2
        elif operation == "*":
            first = lexTree[location-1]
            second = lexTree[location+1]
            value = float(first) * float(second)
            lexTree.pop(location+1)
            lexTree.pop(location)
            lexTree.pop(location-1)
            lexTree.insert(location-1,str(value))
            alloffsets[location]=alloffsets[location]+2
        elif operation == "/":
            first = lexTree[location-1]
            second = lexTree[location+1]
            value = (float(first) / float(second))
            lexTree.pop(location+1)
            lexTree.pop(location)
            lexTree.pop(location-1)
            lexTree.insert(location-1,str(value))
            alloffsets[location]=alloffsets[location]+2
        elif operation == "+":
            first = lexTree[location-1]
            second = lexTree[location+1]
            value=float(first)+float(second)
            lexTree.pop(location+1)
            lexTree.pop(location)
            lexTree.pop(location-1)
            lexTree.insert(location-1,str(value))
            alloffsets[location]=alloffsets[location]+2
        elif operation == "-":
            first = lexTree[location-1]
            second = lexTree[location+1]
            value = float(first) - float(second)
            lexTree.pop(location+1)
            lexTree.pop(location)
            lexTree.pop(location-1)
            lexTree.insert(location-1,str(value))
            alloffsets[location]=alloffsets[location]+2
        pointer += 1
        if verbose:
            print(lexTree)
        if pointer == len(priorities):
            break
    #Calculating end
    final=float(lexTree[0])
    if final.is_integer():
        print(int(final))
    else:
        print(final)
