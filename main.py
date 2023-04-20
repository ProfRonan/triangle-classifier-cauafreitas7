a = int(input('Digite um número a: '))
b = int(input('Digite um numero b: '))
c = int(input('Digite um numero c: '))

x = (c + b > a)
y = (a + c > b)
z = (a + b > c)
print('x')
print('y')
print('z')


if x==False:
   print('Não é um triângulo')
elif y==False: 
   print('Não é um triângulo')
elif z==False: 
   print('Não é um triângulo')

else:
   if a == b and b == c and c == a:
      print('Equilátero')
   elif a != b and b != c and c != a:
      print('Escaleno')
   elif (a==b!=c) and (a==c!=b) and (b==c!=a):
      print('Isóceles')
