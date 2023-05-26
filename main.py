
a = float(input('Digite um número a: '))
b = float(input('Digite um numero b: '))
c = float(input('Digite um numero c: '))

if c + b > a and a + c > b and a + b > c:
      if a == b and b == c and c == a:
            print('Equilátero')
      if a != b and b != c and c != a:
            print('Escaleno')
      if a == b and b != c or a == c and c != b or b == c and c != a:
            print('Isósceles')
else:
      print('Não é um triângulo') 
