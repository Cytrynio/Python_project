# #import math

# #print(math.gcd(24,36))

# #def lista():
# #    lis = '4111-1111-4555-1142'
# #    owca = str.maketrans({"1":"5","4":"1"})
#  #   tlumacz = lis.translate(owca)
#  #   print(tlumacz)

# #lista()

# add_1 = lambda x: x * 2

# result = add_1(4)

def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = ""
    second_line = ""
    dashes = ""
    answers_line = ""


    for problem in problems:
        parts = problem.split()
    if parts[1] not in ["+","-"]:
            return "Error: Operator must be ' +' or '-'."
    if not (parts[0].isdigit() and parts[0].isdigit()):
        return 'Error: Numbers must only contain digits.'
    if len(parts[0]) > 4 or len(parts[2]) > 4:
        return 'Error: Numbers cannot be more than four digits.'


    width = max(len(parts[0])), len(parts[2]) + 2
    top = parts[0].rjust(width)
    bottom = parts[1] + " " + parts[2].rjust(width - 2)
    line = "-" * width 

    if show_answers:
        if parts[1] == '+':
            answer = str(int(parts[0] + parts[2]))
        else:
            answer = str(int(parts[0] - parts[2]))
        answer_line += answer.rjust + "    "
    
    first_line += top + "    "
    second_line += bottom + "    "
    dashes += line + "    "

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip()
    if show_answers:
         arranged_problems += "\n" + answers_line.rstrip()
         return arranged_problems

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))