value = list(input())
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
    else:
        join += workingValue
    if pointer == len(value):
        if not len(join) == 0:
            parsed.append(join)
        break
#Parsing end
#Lexing start
pointer = 0
lexTree = parsed
priorities = []
while True:
        reading = lexTree[pointer]
        print(reading)
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
        pointer += 1
        if pointer == len(parsed):
            break
#Lexing end
#Calculating start

#Calculating end
