logo = r""" ______     ______     ______   ______   ______     ______        ______     ______     ______     ______  
/\  ___\   /\  __ \   /\  ___\ /\  ___\ /\  ___\   /\  ___\      /\  ___\   /\  __ \   /\  == \   /\  == \ 
\ \ \____  \ \ \/\ \  \ \  __\ \ \  __\ \ \  __\   \ \  __\      \ \ \____  \ \ \/\ \  \ \  __<   \ \  _-/ 
 \ \_____\  \ \_____\  \ \_\    \ \_\    \ \_____\  \ \_____\     \ \_____\  \ \_____\  \ \_\ \_\  \ \_\   
  \/_____/   \/_____/   \/_/     \/_/     \/_____/   \/_____/      \/_____/   \/_____/   \/_/ /_/   \/_/   
                                                                                                           """

maquina = r"""
┌─────────────────────────────────────┐
│        ┌─────────────────────┐      │
│        │    INSIRA A MOEDA   │      │
│        │   ┌─────────────┐   │      │
│        │   │             │   │      │
│        │   └─────────────┘   │      │
│        └─────────────────────┘      │
│                                     │
│       ┌───-┐ ┌─-──┐ ┌───┐ ┌───┐     | 
│       │R$25│ |R$10│ |R$5| │R$1│     │
│       │  │ │ │  | │ │ │ | | | |     |
│       └───-┘ └──-─┘ └───┘ └───┘     │
│                                     │
|                                     |
│                                     |
└─────────────────────────────────────┘
"""

recursos  = {
    "água" : 100,
    "leite" : 50,
    "café" : 76,
    "dinheiro" : 0
}

Menu = {
    "espresso": {
        "ingredientes": {
            "água": 50,
            "café": 20
        },
        "custa": 2.50
    },
    "latte": {
        "ingredientes": {
            "água": 200,
            "leite": 150,
            "café": 25
        },
        "custa": 4.0
    },
    "cappuccino": {
        "ingredientes": {
            "água": 250,
            "leite": 100,
            "café": 25
        },
        "custa": 4.0
    }
}

def printRecursos():
    print("\n=== Ingredientes atuais ===")
    print(f"Água:    {recursos["água"]}ml")
    print(f"Leite:     {recursos["leite"]}ml")
    print(f"Café:    {recursos["café"]}g")
    print(f"dinheiro: R$ {recursos["dinheiro"]}")
    print("===========================\n")

def reestocar(ingrediente):
    while True:
        print(f"Quer reestocar quanto de {ingrediente}?")
        quantidade = int(input())
        recursos[ingrediente] += quantidade
        sair = input("Mais algum ingrediente? ")
        if sair == "não":
            break
        else: 
            print("Qual ingrediente agora?")
            ingrediente = input()
            
    

def checarRecursos(bebida):
    for ingrediente, quantidade in Menu[bebida]["ingredientes"].items():
        if recursos[ingrediente] < quantidade:
            print(f"Desculpa, não há {ingrediente} o suficiente.")
            return False
    return True 

def inserirMoeda():
    print(maquina)
    print("Por favor insira as moedas.")
    quarter = int(input("Quantas moedas de 25 centavos?")) * 0.25
    dimes = int(input("Quantas moedas de 10 centavos?")) * 0.10
    nickels = int(input("Quantas moedas de 5 centavos?")) * 0.05
    pennies = int(input("Quantas moedas de 1 centavos?")) * 0.01
    return quarter + dimes + nickels + pennies

def fazerCafe(bebida):
    for ingrediente, quantidade in Menu[bebida]["ingredientes"].items():
        recursos[ingrediente] -= quantidade
    recursos["dinheiro"] += Menu[bebida]["custa"]
    print(f"\nAqui esta o seu {bebida}. Aproveite!")



while True:
    print(logo)
    print("\nDo que você gostaria?")
    print("Espresso   R$ 2.50")
    print("Latte      R$ 4.00")
    print("Cappuccino R$ 4.00")
    print()
    
    resposta = input("Digite sua escolha: ").lower()
    
    if resposta == "off":
        print("\nDesligando a máquina de café...")
        break

    if resposta == "reporte":
        printRecursos()

    if resposta == "reestocar":
            print("Qual ingrediente quer reestocar? ")
            ingrediente = input()
            reestocar(ingrediente)

    if resposta in Menu:
        if checarRecursos(resposta):
            pagamento = inserirMoeda()
            valor = Menu[resposta]["custa"]

            if pagamento >= valor :
                troco = pagamento - valor
            
                if troco > 0:
                    print(f"\nAqui esta o seu troco R${troco:.2f}.")

                fazerCafe(resposta)
            else:
                print(f"Desculpa mas isso não é dinheiro suficiente. Toma os seu R$ {pagamento:.2f} de volta.")
        else:
            print("Por favor escolha outra bebida ou reestoque os ingredientes.")
    else:
        print("Escolha invalida. Por favor escolha uma bebida do menu.")
