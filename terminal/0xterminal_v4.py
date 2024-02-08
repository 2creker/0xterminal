import array
import re
import time

def kod_elem(stroka=''):
    refreshStroka = []
    stroka = stroka.split('<span class="">')
    count = 0
    for i in stroka:
        count += 1
        if count % 33 == 0:
            refreshStroka.append('_')
        if i[:3] == '&lt':
            refreshStroka.append('<')
        elif i[:3] == '&gt':
            refreshStroka.append('>')
        else:
            refreshStroka.append(i[0])
    print(refreshStroka)
    refreshStroka.remove(refreshStroka[0])
    return refreshStroka


def write_words():
  file = open('stroka.txt', 'r')
  a = file.read()
  file.close()
  kod_stroka = kod_elem(a)
  #print(kod_stroka)
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
  return b, kod_stroka

def show_words(massive = []):
  print('\n')
  count = 0
  for i in massive:
    count += 1
    print('|\t', count, ' \t| ', i, end = '\t|\n' )


def sovpadeniya(massive = [], mas2 = []):
  count = 0
  words_count = 0
  schetchik_slov = 0
  #print('\n\n|        №\t|     слова\t|   совпадения\t|')
  #print('-------------------------------------------------')
  file = open('slova.txt', 'w')
  num = file.write('')
  file.close()
  print('START_SUKA')
  kod_count = -1
  for i in massive:
    kod_count += 1
    schetchik_slov += 1
    stroka = ''
    #print('sovpadeiya - ', mas2)
    #print(end = '')
    #print(schetchik_slov, i)
    for j in massive:
      if i != j:
        for k in range(len(massive[0])):
          if i[k] == j[k]:
            count += 1
        if count != 0:
          words_count += 1
          #print(j, '-', count, end = ' \\\ ')
          count = 0
    #print(words_count)
    stroka = stroka + str(schetchik_slov) + ',' + str(i) + ',' + str(words_count) + ',' + str(mas2[kod_count]) + ','
    file = open('slova.txt', 'a')
    num = file.write(stroka)
    num = file.write("\n")
    file.close()
    words_count = 0
    stroka = ''


def perebor_in_memory(massive = [], mas2 = []):
  #print('perebor_in_memory - ', mas2)
  #num = input('\n\n-выберите слово(порядковый номер): ')
  time.sleep(5)
  file = open('nomer_w.txt', 'r')
  num = file.read()
  file.close()
  while re.match(r'[А-Яа-яA-Za-z!@#$%^&*()_+=\[\]{}|\\:;"\'<>,./?0]', num):
    print('\n\nERROR - не тот символ!!!!\n\n\n')
    time.sleep(5)
    file = open('nomer_w.txt', 'r')
    num = file.read()
    file.close()
  num = int(num)
  while num > len(massive):
    print('\n\nERROR - номер больше кол-ва слов!!!!\n\n\n')
    time.sleep(5)
    file = open('nomer_w.txt', 'r')
    num = file.read()
    file.close()
  print('------', massive[num - 1], '------')
  time.sleep(5)
  file = open('kol_sovpad.txt', 'r')
  sovpad = file.read()
  file.close()
  while re.match(r'[А-Яа-яA-Za-z!@#$%^&*()_+=\[\]{}|\\:;"\'<>,./?]', sovpad):
    print('\n\nERROR - не тот символ!!!!\n\n\n')
    time.sleep(5)
    file = open('kol_sovpad.txt', 'r')
    sovpad = file.read()
    file.close()
  sovpad = int(sovpad)
  while sovpad > len(massive[0]):
    print('\n\nERROR - номер больше кол-ва букв!!!!\n\n\n')
    time.sleep(5)
    file = open('kol_sovpad.txt', 'r')
    sovpad = file.read()
    file.close()
  n = 0
  memory = []
  memory_kod_elem = []
  kod_elem_count = -1
  for i in massive:
    kod_elem_count += 1
    count = 0
    if massive[num - 1] != i:
      for k in range(len(massive[num - 1])):
        if massive[num - 1][k] == i[k]:
          count += 1
      if count == sovpad:
        memory.insert(n, i)
        memory_kod_elem.insert(n, mas2[kod_elem_count])
        n += 1
  return memory, memory_kod_elem

def perebor_for_memory(massive1 = [], massive2 = [], mas3 = []):
  #print('perebor_for_memory - ', mas3)
  n = 0
  memory = []
  memory_kod_elem = []
  a, b = perebor_in_memory(massive2, mas3)
  kod_elem_count = -1
  for i in massive1:
    kod_elem_count += 1
    for j in a:
      if i == j:
        memory.insert(n, j)
        memory_kod_elem.insert(n, mas3[kod_elem_count])
        n += 1
  return memory, memory_kod_elem

def count_kod_elem(mas1 = [], mas2 = []):
  defend = len(mas1[0])
  count = 0
  n = []
  for i in mas2:
    count += 1
    if re.match(r'[A-Z]', i):
      n.append(count)
  d = 0
  first_elem_kod = []
  for i in range(len(n)):
    if i == d:
      first_elem_kod.append(n[i])
      d += defend
  return first_elem_kod

command = 'go'
while command != 'exit':
  mas_str, kod_elem_stroka = write_words()
  #print(kod_elem_stroka)
  fek = count_kod_elem(mas_str, kod_elem_stroka)
  #print(fek)
  #print('\n' * 100)
  sovpadeniya(mas_str, fek)
  memory_str, kod_elem_stroka = perebor_in_memory(mas_str, fek)
  mas_str = memory_str
  fek = kod_elem_stroka
  sovpadeniya(mas_str, fek)
  file = open('kol_sovpad.txt', 'r')
  command = file.read()
  file.close()
  while str(command) != 'r' and str(command) != 'y' and str(command) != 'exit':
    file = open('kol_sovpad.txt', 'r')
    command = file.read()
    file.close()
  while command == 'y':
    perebor_str, kod_elem_stroka = perebor_for_memory(memory_str, mas_str, kod_elem_stroka)
    memory_str = perebor_str
    fek = kod_elem_stroka
    mas_str = perebor_str
    sovpadeniya(mas_str, fek)
    file = open('kol_sovpad.txt', 'r')
    command = file.read()
    file.close()
    while str(command) != 'r' and str(command) != 'y' and str(command) != 'exit':
      file = open('kol_sovpad.txt', 'r')
      command = file.read()
      file.close()