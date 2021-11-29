l = ["(", 0]


def expr_append(item):
    """
    Function new_result add new item in list

    item -- math operator, "(", ")" or number

    """
    l.append(item)


def get_list():
    """
    Function get_list get list-expression

    """
    global l
    return list(l)


def func_addition(arg1, arg2):
    """
    Function func_addition does addition

    arg1(float) -- first argument
    arg2(float) -- second argument

    """
    return arg1+arg2


def func_subtraction(arg1, arg2):
    """
    Function func_subtraction does subtraction

    arg1(float) -- first argument
    arg2(float) -- second argument

    """
    return arg1-arg2


def func_multiplication(arg1, arg2):
    """
    Function func_multiplication does multiplication

    arg1(float) -- first argument
    arg2(float) -- second argument

    """
    return arg1*arg2


def func_division(arg1, arg2):
    """
    Function func_division does division

    arg1(float) -- first argument
    arg2(float) -- second argument

    """
    return arg1/arg2


def new_expr(old_result):
    """
    Function new_expr clear list-expression and add old result

    old_result(float) -- old result or zero (if push "C")

    """
    global l
    l = ["(", old_result]
