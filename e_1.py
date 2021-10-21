#Дан произвольный список, содержащий только числа. 
#Выведите результат сложения всех чисел больше 10. CODEWARS
'''
tm=[10,2,3,4,12,34,18]
sum=0
i=0
while i<len(tm):
    if tm[i]>10:
        sum+=tm[i]
    i+=1
print('sum =', sum)

'''

#Просуммировать неопределенное количество чисел, вводимых пользователем, 
#суммировать до тех пор, пока пользователь не введёт слово «стоп»
''' 
su=0
while True:
    st=input('chislo : ')
    if st==('стоп'):
        break
    su += int(st)
print(su)

'''

#Просуммировать неопределенное количество чисел, 
# вводимых пользователем, суммировать до тех пор, 
# пока пользователь не введёт слово «стоп». 
# Не учитывать числа кратные 5
'''
su=0
while True:
    st=input('chislo : ')
    if st==('стоп'):
        break
    elif int(st) % 5==0:
        continue
    su += int(st)
print(su)
'''
#Написать программу, которая будет выводить на экран
#случайные числа от 1 до 10 до тех пор, пока не 
#выпадет 7.
'''
import random
while True:
    tm=random.randint(0,10)
    print (tm)
    if tm == 7:
        break
'''
#Ввести два целых числа A и B ( A < B ). Вывести в 
#порядке возрастания все целые числа, расположенные 
#между A и B (включая сами числа A и B ), а также 
#количество N этих чисел. [01-08-For2]
 
'''
a=int(input('Enter a: '))
b=int(input('Enter b: '))
i=0
if a<b:
    ls=list(range(a,b+1))
    print (ls)
    print(len(ls))
'''
'''
for i in range (5):
    for j in range (5):
        print (i,j)
'''
ls = [[1,2,3], [3,2,'2'], [3,5,6]]
for i in ls:
    for j in i:
        if type(j)==int:
            print (j)
        else:
            print('Not a number.')

