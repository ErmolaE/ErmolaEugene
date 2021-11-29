import business_logic as bl


def show_message(message):
    """
    Function show_message show message

    """
    print(message)


def get_query():
    """
    Function get_query get number

    """
    return input("Input number or '(':\n")


def ui_operator(func_valid, oper):
    """
    Function ui_operator get number and operator and show current result

    func_valid(func) -- validation function  
    oper(str) --  operator

    """
    number = get_query()
    message = func_valid(number)
    while message != True:
        show_message(message)
        number = get_query()
        message = func_valid(number)
    if number == "(":
        bl.add_oper(oper)
        ui_open()
    else:
        bl.add_items(oper, number)
        result = bl.final_result()
        show_message(result)


def ui_open():
    """
    Function ui_open open bracket

    """
    number = get_query()
    message = bl.valid_float(number)
    while message != True:
        show_message(message)
        number = get_query()
        message = bl.valid_float(number)
    if number == "(":
        bl.add_oper("(")
        ui_open()
    else:
        bl.add_items("(", number)
        result = bl.final_result()
        show_message(result)


def ui_close():
    """
    Function ui_close close bracket

    """
    bl.add_oper(")")


def ui_equal():
    """
    Function ui_equal get final result and start new expression

    """
    result = bl.final_result()
    show_message(result)
    bl.new_expr(result)


def ui_clear():
    """
    Function ui_clear clear current expression

    """
    show_message(0)
    bl.new_expr(0)


if __name__ == "__main__":
    show_message("0")
    while True:
        operation = input(
            "Please input the operator: '+', '-', '*', '/', ')', '=', 'C', or input 'exit' to end the programm:\n")
        if operation == "+":
            ui_operator(bl.valid_float, "+")
        elif operation == "-":
            ui_operator(bl.valid_float, "-")
        elif operation == "*":
            ui_operator(bl.valid_float, "*")
        elif operation == "/":
            ui_operator(bl.valid_zero, "/")
        elif operation == ")":
            ui_close()
        elif operation == "=":
            ui_equal()
        elif operation == "C":
            ui_clear()
        elif operation == "exit":
            break
        else:
            show_message("incorrect input")
            continue
