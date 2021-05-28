# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474


# code submitted in:
# https://replit.com/@nahuelcastro/boilerplate-arithmetic-formatter#arithmetic_arranger.py
def arithmetic_arranger(problems, b = False):
    arranged_problems = ''
    max_len = []
    mask = '      ' # six whitespaces
    mask_line = '------' # six '-'
    space = '    '  # four whitespaces
    enter = '\n'

    if(len(problems) > 5):
        return 'Error: Too many problems.'

    for s in problems:
        if(s.find('*') != -1 or s.find('/') != -1):
            return "Error: Operator must be '+' or '-'."
        for c in s:
            if( not (ord('0') <= ord(c) <= ord('9') or ord(c) == ord(' ') or ord(c) == ord('+') or ord(c) == ord('-'))):
                return 'Error: Numbers must only contain digits.'
        s_aux = s.split(' ')
        for x in s_aux:
            if(len(x) > 4):
                return 'Error: Numbers cannot be more than four digits.'

    # set max_len  
    for i in range(len(problems)):
        m = 0
        s_aux = problems[i].split(' ')
        for c in s_aux:
            if(len(c) > m): m = len(c)
        max_len.append(m)

    #first line
    for i in range(len(problems)):
        l = max_len[i] + 2;
        s_aux = problems[i].split(' ')
        s = s_aux[0]
        arranged_problems = arranged_problems + mask[0 : l - len(s)] + s
        if(i != len(problems) - 1): arranged_problems = arranged_problems + space

    arranged_problems = arranged_problems + enter

    #second line
    for i in range(len(problems)):
        l = max_len[i] + 2;
        s_aux = problems[i].split(' ')
        s = s_aux[2]
        operand = s_aux[1]
        arranged_problems = arranged_problems + operand + mask[1 : l - len(s)] + s
        if(i != len(problems)-1): arranged_problems = arranged_problems + space

    arranged_problems = arranged_problems + enter

    #third line
    for i in range(len(problems)):
        l = max_len[i] + 2;
        
        arranged_problems = arranged_problems + mask_line[0:l];
        if(i != len(problems)-1): arranged_problems = arranged_problems + space

    if(not b): 
        return arranged_problems

    arranged_problems = arranged_problems + enter

    #four line
    for i in range(len(problems)):
        l = max_len[i] + 2;
        s_aux = problems[i].split(' ')
        n1 = int(s_aux[0])
        operand = s_aux[1]
        n2 = int(s_aux[2])
        if(operand == '+'): 
            res = n1 + n2
        else:
            res = n1 - n2

        arranged_problems = arranged_problems + mask[0: l - len(str(res))] + str(res)
        
        if(i != len(problems)-1): arranged_problems = arranged_problems + space

    
    return arranged_problems


#test 
res = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
print (res);