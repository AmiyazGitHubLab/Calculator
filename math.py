value = list(input())
pointer = 0
parsed = []
join = ""
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
