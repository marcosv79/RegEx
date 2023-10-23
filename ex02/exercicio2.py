import ply.lex as lex, sys

tokens = (
    "QUANTIA",
    "CANCELAR",
    "PRODUTO",
)

t_ignore = " \n"

def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}'")
    t.lexer.skip(1)

def t_QUANTIA(t):
    r'(QUANTIA[ ])((e\d|c\d{1,2})(,[ ]*(e\d|c\d{1,2}))*)'
    bbr = lexer.lexmatch.group(3)
    moedas = bbr.split(', ')
    lista_moedas = ["c1","c2", "c5", "c10", "c20", "c50", "e1", "e2"]
    valores = {"c1": 0.01, "c2": 0.02, "c5": 0.05, "c10": 0.10, "c20": 0.20, "c50": 0.50, "e1": 1.00, "e2": 2.00}
    global saldo
    inserido = 0 
    invalidas = []
    print_invalidas = ""
    for m in moedas: 
        if m in lista_moedas:
            saldo += valores[m]
            inserido += valores[m]
        else:
            invalidas.append(m)
    
    if len(invalidas) != 0:
        print_invalidas = "(" + ','.join(invalidas) + " não aceite(s)!) "
              
    print("> " + print_invalidas + f"valor inserido: €{inserido:.2f} (saldo: €{saldo:.2f})")


def t_CANCELAR(t):
    r"CANCELAR"
    global saldo
    saldo = int(saldo*100)
    devolvido = saldo
    if saldo == 0:
        print("Não há dinheiro a ser devolvido")
    else:
        moedas = [200, 100, 50, 20, 10, 5, 2, 1]
        m_format = ["e2", "e1", "c50", "c20", "c10", "c5", "c2", "c1"]
        print_troco=f""
        counter = 0
        for i, m in enumerate(moedas):
            if(saldo // m > 0):
                n_coins = saldo // m
                saldo -= n_coins*m

                if(counter > 0):
                    print_troco += f", {n_coins} moeda(s) de {m_format[i]}"
                else:
                    print_troco += f"{n_coins} moeda(s) de {m_format[i]}"
                counter += 1

        print("valor devolvido: €{:.2f} ".format(devolvido/100) + f"({print_troco})")

produtos = {"twix": {"preco": 2.30, "stock": 10},
            "kitkat": {"preco": 1.80, "stock": 5},
            "snickers": {"preco": 2.00, "stock": 3}}

def t_PRODUTO(t):
    r'(PRODUTO=)(twix|kitkat|snickers)'
    t.value = lexer.lexmatch.group(10)
    global produtos
    produto = t.value
    if produtos[produto]["stock"] == 0:
        print(f"Produto {produto} indisponível", file=sys.stderr)
        t.lexer.skip(1)
    else:
        t.preco = produtos[produto]["preco"]
        #produtos[produto]["stock"] -= 1
        return t

saldo = 0.0
lexer = lex.lex()

print("Bem-vindo(a) à máquina de vendas automática!")

while True:

    entrada = input("> ").strip()
    lexer.input(entrada)
    for token in lexer:
        if token.type == "QUANTIA":
            pass
        elif token.type == "PRODUTO":
            #token.value = lexer.lexmatch.group(10)
            if token.preco > saldo:
                print(f"preço: €{token.preco:.2f} (quantia insuficiente) (saldo: €{saldo:.2f})")
            elif produtos[token.value]["stock"] == 0:
                print(f"Produto {token.value} indisponível")
            else:
                produtos[token.value]["stock"] -= 1
                saldo -= token.preco
                print(f"Compra efetuada com sucesso! Saldo restante: €{saldo:.2f}")
        else:
            print("Valor inválido. Tente novamente.")

