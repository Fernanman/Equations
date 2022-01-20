def ignore_operations(expression):
    sub_expressions = {}
    sub = ""
    possible_answers = set()

    for char in expression:
        sub += char
        
        try:
            if len(sub) > 1:
                sub_expressions[sub] = eval(sub)
                sub = char
        except SyntaxError:
            pass
    
    possible_answers.add(eval(expression))

    for key in sub_expressions:
        new_expression = ""
        for key2 in sub_expressions:
            if key in expression:
                new_expression = expression.replace(key, str(sub_expressions[key]))
                possible_answers.add(eval(new_expression))
            print(key2, new_expression)
            if key2 in new_expression:
                new_expression = new_expression.replace(key2, str(sub_expressions[key2]))
                possible_answers.add(eval(new_expression))
