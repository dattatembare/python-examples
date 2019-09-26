def do_while(int_a, a_bool=False):
    while a_bool or int_a <= 100:
        a_bool = False
        print("The value of variable = ", int_a)
        int_a = int_a + 10


do_while(110, True)  # Always execute once
do_while(10)  # execute in loop


def do_while_using_while(int_a):
    def a_loop(_a):
        print("Do something with _a = ", _a)

    i = 0
    while i == 0:
        print(f'Inside do ... {int_a}')
        a_loop(int_a)
        if int_a > 100:
            int_a = int_a - 100
        i += 1
    else:
        while int_a <= 100:
            a_loop(int_a)
            int_a = int_a + 10


do_while_using_while(10)
do_while_using_while(120)
