
a = int(input('Digite um número a: '))
b = int(input('Digite um numero b: '))
c = int(input('Digite um numero c: '))

if c + b > a and a + c > b and a + b > c:
      if a == b and b == c and c == a:
            print('Equilátero')
      if a != b and b != c and c != a:
            print('Escaleno')
      if (a==b!=c) and (a==c!=b) and (b==c!=a):
            print('Isóceles')
else:
      print('Não é um triângulo')
