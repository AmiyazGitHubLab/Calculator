verbose = True
while True:
    value = list(input("> "))
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
            pass
        if not isNumber:
            if not len(join) == 0:
                parsed.append(join)
                join = ""
            parsed.append(workingValue)
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
    pointer = 0
    offset = 0
    if len(parsed) == 1:
        break
    location = priorities[pointer]
    while True:
        prev = location
        location = priorities[pointer]
        if prev  < location:
            location -= offset
        operation = lexTree[location]
        if operation == "*":
            first = lexTree[location-1]
            second = lexTree[location+1]
            value = int(first) * int(second)
            lexTree.remove(operation)
            lexTree.remove(first)
            lexTree.remove(second)
            lexTree.insert(location-1,str(value))
            offset+=2
        if operation == "/":
            first = lexTree[location-1]
            second = lexTree[location+1]
            value = round(int(first) / int(second))
            lexTree.remove(operation)
            lexTree.remove(first)
            lexTree.remove(second)
            lexTree.insert(location-1,str(value))
            offset+=2
        if operation == "+":
            first = lexTree[location-1]
            second = lexTree[location+1]
            value = int(first) + int(second)
            lexTree.remove(operation)
            lexTree.remove(first)
            lexTree.remove(second)
            lexTree.insert(location-1,str(value))
            offset+=2
        if operation == "-":
            first = lexTree[location-1]
            second = lexTree[location+1]
            value = int(first) - int(second)
            lexTree.remove(operation)
            lexTree.remove(first)
            lexTree.remove(second)
            lexTree.insert(location-1,str(value))
            offset+=2
        pointer += 1
        if verbose:
            print(lexTree)
        if pointer == len(priorities):
            break
    #Calculating end
print(lexTree[0])

