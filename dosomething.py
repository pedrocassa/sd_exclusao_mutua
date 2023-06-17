from twoPhaseLocking import TwoPhaseLocking

tpl = TwoPhaseLocking()

def doSomething():
    # Iniciar uma transação
    tpl.start_transaction("T1")
    
    # Ler um item
    valor = tpl.read_item("T1", "item1")
    print(valor)

    # Escrever um item
    tpl.write_item("T1", "item1", "novo_valor")

    # Encerrar uma transação
    tpl.end_transaction("T1")
