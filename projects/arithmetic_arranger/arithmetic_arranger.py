def arithmetic_arranger(problems: list[str], show_answer=False) -> str:
    if len(problems) > 5:
        return "Error: Too many problems"

    first_line: list[str] = []
    second_line: list[str] = []
    third_line: list[str] = []
    answer_line: list[str] = []

    for problem in problems:
        operand1, operator, operand2 = problem.split()
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'"

        try:
            int(operand1)
            int(operand2)
        except ValueError:
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            answer = int(operand1) + int(operand2)
        elif operator == "-":
            answer = int(operand1) - int(operand2)
        
        max_length = max(len(operand1), len(operand2))
        operand1_rjust = 2 + (max_length - len(operand1))
        operand2_rjust = 1 + max_length - len(operand2)
        answer_rjust = (max_length + 2) - len(str(answer))

        first_line.append(' ' * operand1_rjust + operand1)
        second_line.append(operator + ' ' * operand2_rjust + operand2)
        third_line.append('-' * (max_length + 2))
        answer_line.append(' ' * answer_rjust + str(answer))

    result = [
        '    '.join(first_line),
        '    '.join(second_line),
        '    '.join(third_line),
        '    '.join(answer_line)
        ]

    return '\n'.join(result if show_answer else result[:3])


