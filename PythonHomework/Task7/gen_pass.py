import random
import string


def ui_input():
    while True:
        try:
            pass_len = int(input("Please, input password length:\n"))
            if pass_len > 0:
                break
            else:
                print('Incorrect input!')
        except ValueError:
            print('Incorrect input!')
            continue
    while True:
        need_spec_char = input("Are special characters needed? Please enter y or n (yes or no):\n")
        if need_spec_char == "y" or need_spec_char == "n":
            break
        else:
            print('Incorrect input!')
            continue
    return pass_len, need_spec_char


def gen_pass(pass_len, need_spec_char):
    spec_char = string.punctuation
    char = string.ascii_letters + string.digits
    res_pass = ''
    for i in range(pass_len):
        if need_spec_char == "y":
            res_pass += random.choice(char + spec_char)
        if need_spec_char == "n":
            res_pass += random.choice(char)
    return res_pass


def ui_out(pass_len, need_spec_char):
    while True:
        yield gen_pass(pass_len, need_spec_char)


if __name__ == '__main__':
    while True:
        x = input('Do you want a new password? Please enter y or n (yes or no):\n')
        if x == "y":
            pass_len, need_spec_char = ui_input()
            password = iter(ui_out(pass_len, need_spec_char))
            print(next(password))
            continue
        elif x == "n":
            break
        else:
            print('Incorrect input!')
            continue
