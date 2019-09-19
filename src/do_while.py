def do_while(int_a, a_bool=False):
    while a_bool or int_a <= 100:
        a_bool = False
        print("The value of variable = ", int_a)
        int_a = int_a + 10


do_while(110, True)  # Always execute once
do_while(10)  # execute in loop


