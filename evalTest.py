def eval_loop():
    userInstruction0 = None
    while True:
        userInstruction = input('Instruction please: ')
        if userInstruction == 'done':
            print(eval(userInstruction0))
            break
        print(eval(userInstruction))
        userInstruction0 = userInstruction

        
