def increase(price=0, taxe=0):
    res = price + (price * taxe / 100)
    return res


def decrease(price=0, taxe=0):
    res = price - (price * taxe / 100)
    return res


def double(price=0):
    res = price * 2
    return res


def half(price=0):
    res = price / 2
    return res


def moeda(price=0, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.', ',')
    #o comando [replace] faz com que substitua um 'x' caracter do python
    #por um 'y' caracter escolhido neste caso: '.' por ','