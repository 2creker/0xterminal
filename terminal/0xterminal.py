import array
import re
def write_words():
  print('введите слова: ')
  a = input()
  s = ""
  count = 0

  for i in a:
    if re.match(r'[A-Z>]', i):
      s = s + i
  s2 = ''
  for i in s:
    if i == '>':
      count += 1
    else:
      s2 = s2 + i
      count = 0
    if count > 3:
      s2 = s2 + ' '
      count = 0
  b = s2.split()
  for i in b:
    if i == 'NN':
      b.remove(i)
  print(b)
  for i in b:
    if len(b[0]) != len(i):
      print('\n\n-КОЛ-ВО СИМВОЛОВ В СЛОВАХ НЕ СОВПАДАЕТ!!!! \n\n')
      b = write_words()
      return b
  return b

def show_words(massive = []):
  print('\n')
  count = 0
  for i in massive:
    count += 1
    print('|\t', count, ' \t| ', i, end = '\t|\n' )

def sovpadeniya(massive = []):
  count = 0
  words_count = 0
  schetchik_slov = 0
  print('\n\n|        №\t|     слова\t|   совпадения\t|')
  print('-------------------------------------------------')
  for i in massive:
    schetchik_slov += 1
    print(end = '')
    print('|\t', schetchik_slov, ' \t| ', i, end = '\t| ')
    for j in massive:
      if i != j:
        for k in range(len(massive[0])):
          if i[k] == j[k]:
            count += 1
        if count != 0:
          words_count += 1
          #print(j, '-', count, end = ' \\\ ')
          count = 0
    print('\t', words_count, '\t|')
    words_count = 0

def perebor_in_memory(massive = []):
  num = input('\n\n-выберите слово(порядковый номер): ')
  while re.match(r'[А-Яа-яA-Za-z!@#$%^&*()_+=\[\]{}|\\:;"\'<>,./?0]', num):
    print('\n\nERROR - не тот символ!!!!\n\n\n')
    num = input('\n\n-выберите слово(порядковый номер): ')
  num = int(num)
  while num > len(massive):
    print('\n\nERROR - номер больше кол-ва слов!!!!\n\n\n')
    num = int(input('\n\n-выберите слово(порядковый номер): '))
  print('------', massive[num - 1], '------')
  sovpad = input('-введите кол-во совпадений: ')
  while re.match(r'[А-Яа-яA-Za-z!@#$%^&*()_+=\[\]{}|\\:;"\'<>,./?]', sovpad):
    print('\n\nERROR - не тот символ!!!!\n\n\n')
    sovpad = input('-введите кол-во совпадений: ')
  sovpad = int(sovpad)
  while sovpad > len(massive[0]):
    print('\n\nERROR - номер больше кол-ва букв!!!!\n\n\n')
    sovpad = int(input('-введите кол-во совпадений: '))
  n = 0
  memory = []
  for i in massive:
    count = 0
    if massive[num - 1] != i:
      for k in range(len(massive[num - 1])):
        if massive[num - 1][k] == i[k]:
          count += 1
      if count == sovpad:
        memory.insert(n, i)
        n += 1
  return memory

def perebor_for_memory(massive1 = [], massive2 = []):
  n = 0
  memory = []
  a = perebor_in_memory(massive2)
  for i in massive1:
    for j in a:
      if i == j:
        memory.insert(n, j)
        n += 1
  return memory


command = 'go'
while command != 'exit':
  mas_str = write_words()
  print('\n' * 100)
  sovpadeniya(mas_str)
  memory_str = perebor_in_memory(mas_str)
  mas_str = memory_str
  sovpadeniya(mas_str)
  command = input('\n\nпродолжить/перезапуск (y/r)? для выхода(exit): ')
  while str(command) != 'r' and str(command) != 'y' and str(command) != 'exit':
    command = input('\n\nпродолжить/перезапуск (y/r)? для выхода(exit): ')
  while command == 'y':
    perebor_str = perebor_for_memory(memory_str, mas_str)
    memory_str = perebor_str
    mas_str = perebor_str
    sovpadeniya(mas_str)
    command = input('\n\nпродолжить/перезапуск (y/r)? для выхода(exit): ')
    while str(command) != 'r' and str(command) != 'y' and str(command) != 'exit':
      command = input('\n\nпродолжить/перезапуск (y/r)? для выхода(exit): ')