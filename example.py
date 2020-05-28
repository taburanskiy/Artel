from random import randint

combo_num = 0
sequence = False

combo = {
    1: 'Bingo',
    2: 'Combo',
    3: 'Casino',
    4: 'Cheater',
    5: 'Royal Flash'
}

def combinator(value):
  return combo.get(value)

def input_number():
    try:
        num = int(input('Веддіть число '))
        if num >0 and num <=3:
            return num
        else: 
            print("Число не в діапазоні від 1 до 3")
    except ValueError:
        print('Введено не число!!!!')
        input_number()


while True:
  x = randint(1,3)
  print('Число загадане')
  while True:
    num = input_number()
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

