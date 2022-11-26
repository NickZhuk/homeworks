line = input()
first_word = line[:line.find(' ')]
second_word = line[line.find(' ') + 1:]
print(second_word + ' ' + first_word)
