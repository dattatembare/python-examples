if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_list = list(arr)
    max_num = max(my_list)
    second_last = max_num - 1
    while second_last not in my_list:
        second_last -= 1
    print(second_last)
