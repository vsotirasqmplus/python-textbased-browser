"""
def hidden_operation(operand):
    if oper == "and":
        return operand and hidden_operand
    elif oper == "or":
        return operand or hidden_operand
    elif oper == "not":
        return not operand
"""
def solve():
    # Write your code here
    if hidden_operation(False) and not hidden_operation(True):
        print('not')
    else:
        param = [1, 2, 3, 4]
        hidden_operator = hidden_operation(param)
        if hidden_operator == param:
            param = False
            hidden_operator = hidden_operation(param)
            print('or')
            print(hidden_operator)
        else:
            print('and')
            print(hidden_operator)
"""
Another good example:

def solve():
    h_true = hidden_operation('@43')
    h_false = hidden_operation(False)
    if h_true == '@43':
        print('or', h_false, sep='\n')
    elif not h_false:
        print('and', h_true, sep='\n')
    else:
        print('not')
"""
