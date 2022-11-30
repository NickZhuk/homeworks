for i in range(1, 101, 1):
    if i % 3 == 0:
        print('Fuzz')
    if i % 5 == 0:
        print('Buzz')
    if i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    else:
        print(i)
