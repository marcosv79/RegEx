import re

er = r'(\+|-)?\d+\.\d+([e|E](\+|-)?\d+)?'
er_regex = re.compile(er)

t1 = "-3423.12413432"
t2 = "+12312.58912"
t3 = "3.14"

list_tocheck = [+36.423, -3.45e7, 5.41e-8, -0.45E22, 4.56, t1, t2, t3]
list_tocheck = [str(x) for x in list_tocheck]

for element in list_tocheck:
    if er_regex.fullmatch(element):
        print(f"{element} é um exemplo válido de constante com virgula flutuante")
    else:
        print(f"{element} não é um exemplo válido de constante com virgula flutuante")