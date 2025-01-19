def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = ""
    second_line = ""
    dashes = ""
    answers_line = ""
    
    for problem in problems:
        parts = problem.split()
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Oblicz szerokość kolumny i odpowiedź
        width = max(len(parts[0]), len(parts[2])) + 2
        top = parts[0].rjust(width)
        bottom = parts[1] + " " + parts[2].rjust(width - 2)
        line = "-" * width
        
        # Oblicz odpowiedź, jeśli show_answers == True
        if show_answers:
            if parts[1] == '+':
                answer = str(int(parts[0]) + int(parts[2]))
            else:
                answer = str(int(parts[0]) - int(parts[2]))
            answers_line += answer.rjust(width) + "    "
        
        # Dodaj do linii wynikowych
        first_line += top + "    "
        second_line += bottom + "    "
        dashes += line + "    "
    
    # Tworzenie finalnego tekstu
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes.rstrip()
    if show_answers:
        arranged_problems += "\n" + answers_line.rstrip()
    
    return arranged_problems

# Przykład wywołania
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
