a = int(input('inserir primeiro numero'))
b = int(input('inserir segundo numero')
c = int(input('inserir tercero numero')
if a < c:
    a, c = c, a

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

print(f'A ordem decrescente é {a}, {b} e {c}')
