def arithmetic_arranger(problems, show_answers=False):
    # print(f'DATA: {["3801 - 2", "45 + 43", "123 + 49", "123 + 49"]}')

    if len(problems) > 5:
        return 'Error: Too many problems.'
        # raise ValueError('Error: Too many problems.')

    operators = []
    numbers1 = []
    numbers2 = []
    for problem in problems:
        parts = problem.split()
        if len(parts)!= 3:
            return 'Error: Invalid problem format.'
            # raise ValueError('Error: Invalid problem format.')
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
            # raise ValueError("Error: Operator must be '+' or '-'.")
        if not parts[0].isdigit() or not parts[2].isdigit():
            return 'Error: Numbers must only contain digits.'
            # raise ValueError('Error: Numbers must only contain digits.')
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            # raise ValueError('Error: Numbers cannot be more than four digits.')
        
        operators.append(parts[1])
        numbers1.append(parts[0])
        numbers2.append(parts[2])

        # Calculate answers if required
    if show_answers:
        answers = []
        for i in range(len(numbers1)):
            if operators[i] == '+':
                answers.append(str(int(numbers1[i]) + int(numbers2[i])))
            else:
                answers.append(str(int(numbers1[i]) - int(numbers2[i])))
    # print(f'ANSWERS: {answers}')

        # Arrange problems
    arranged_problems = ''
    for i in range(len(numbers1)):
        max_length = max(len(numbers1[i]), len(numbers2[i]))
        arranged_problems += numbers1[i].rjust(
            max_length + 6
            if i != 0
            else max_length + 2
        )
    arranged_problems += '\n'
    
    for i in range(len(numbers2)):
        max_length = max(len(numbers1[i]), len(numbers2[i]))
        arranged_problems += operators[i].rjust(5 if i != 0 else 0 ) + numbers2[i].rjust(max_length + 1)
    arranged_problems += '\n'

    for i in range(len(operators)):
        max_length = max(len(numbers1[i]), len(numbers2[i]))
        arranged_problems += ('-' * (max_length + 2)).rjust(max_length + 6 if i != 0 else 0)
    

    if show_answers:
        arranged_problems += '\n'
        for i in range(len(answers)):
            max_length = max(len(numbers1[i]), len(numbers2[i]))
            arranged_problems += answers[i].rjust(max_length + 6 if i != 0 else max_length + 2)
       
    # print(arranged_problems)
    return arranged_problems

# arithmetic_arranger(["3801 - 2", "45 + 43", "123 + 49", "123 + 49"], True)
# arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"], True)