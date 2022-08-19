numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
    if i == 1:
        print(f'{1}st')
    elif i == 2 or i == 3:
        print(f'{i}nd')
    else:
        print(f'{i}th')