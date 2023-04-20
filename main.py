
a = int(input('Digite um número a: '))
b = int(input('Digite um numero b: '))
c = int(input('Digite um numero c: '))

x = (c + b > a)
y = (a + c > b)
z = (a + b > c)

if a == b and b == c and c == a:
      print('Equilátero')
elif a != b and b != c and c != a:
      print('Escaleno')
elif (a==b!=c) and (a==c!=b) and (b==c!=a):
      print('Isóceles')

else: 
   x==False or y==False or z==False 
   print('Não é um triângulo')
