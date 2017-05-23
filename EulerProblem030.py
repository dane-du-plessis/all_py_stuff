i=2 # start with 2
total = 0
while i <= 999999:
    temp = i
    trialNumber = 0
    while temp != 0:
        digit = temp%10 # extract last digit
        temp  = temp//10  # discard last digit from temp
        trialNumber += digit**5
    if trialNumber == i:
        print(i)
        total += i
    i += 1
