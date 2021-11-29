import data_logic as dl


def valid_float(number):
    """
    Function valid_float does validation input number on float

    """
    if number == "(":
        return True
    else:
        try:
            float(number)
            return True
        except ValueError as error:
            return error


def valid_zero(number):
    """
    Function valid_zero does validation input number on float and not equal zero

    """
    if number == "(":
        return True
    else:
        try:
            float(number)
            assert float(number) != 0, "can not be divided by zero "
            return True
        except AssertionError as error:
            return error
        except ValueError as error:
            return error


def del_segment(l, i):
    """
    Function del_segment delete list's segment around the operator

    l(list) -- list-expression 
    i(int) -- operator position

    """
    del l[i-1:i+1]
    return l


def inter_result(l):
    """
    Function inter_result does intermediate result

    l(list) -- list-intermediate expression 

    """
    n_l = l
    while "*" in n_l or "/" in n_l:
        for i in range(len(n_l)):
            if n_l[i] == "*" or n_l[i] == "/":
                if n_l[i] == "*":
                    n_l[i+1] = dl.func_multiplication(n_l[i-1], n_l[i+1])
                    del_segment(n_l, i)
                    break
                if n_l[i] == "/":
                    n_l[i+1] = dl.func_division(n_l[i-1], n_l[i+1])
                    del_segment(n_l, i)
                    break
    while len(n_l) > 1:
        for i in range(len(n_l)):
            if n_l[i] == "+":
                n_l[i+1] = dl.func_addition(n_l[i-1], n_l[i+1])
                del_segment(n_l, i)
                break
            if n_l[i] == "-":
                n_l[i+1] = dl.func_subtraction(n_l[i-1], n_l[i+1])
                del_segment(n_l, i)
                break
    return n_l[0]


def final_result():
    """
    Function inter_result does final result 

    """
    n_l = dl.get_list()
    bkt_value = n_l.count("(")-n_l.count(")")
    if bkt_value > 0:
        for i in range(bkt_value):
            n_l.append(")")
    while len(n_l) > 3:
        i_l = [i for i, x in enumerate(n_l) if x == "("]
        for i in range(i_l[-1]+1, len(n_l)):
            if n_l[i] == ")":
                n_l[i_l[-1]] = inter_result(list(n_l[(i_l[-1]+1):i]))
                del n_l[i_l[-1]+1:i+1]
                break
    return n_l[0]


def add_items(oper, number):
    """
    Function add_items transfers items in data

    oper(str) -- math operator, "(", ")"  
    number(float) --  number

    """
    dl.expr_append(oper)
    dl.expr_append(float(number))


def add_oper(oper):
    """
    Function add_oper transfers oper in data

    oper(str) -- math operator, "(", ")"  

    """
    dl.expr_append(oper)


def new_expr(result):
    """
    Function new_expr end old expression

    result(float) -- old result  

    """
    dl.new_expr(result)
