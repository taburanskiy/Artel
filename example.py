from random import randint
combo_num = 0

combo = {
    1: 'Bingo',
    2: 'Combo',
    3: 'Casino',
    4: 'Cheater',
    5: 'Royal Flash'  
}

def combinator(value):
  return combo.get(value)
 
sequence = False
while True:
  x = randint(1,3)
  print('Число загадане')
  while True:
    num =int(input('Веддіть число'))
    if num == x :
      if sequence == True: 
        combo_num += 1
        print(combinator(combo_num))
      else: 
        sequence = True
        combo_num = 1
        print(combinator(combo_num))
      break
    else:
      sequence = False
      continue