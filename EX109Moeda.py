def increase(price=0, taxe=0, format=False):
    res = price + (price * taxe / 100)
    return res if format is False else moeda(res)


def decrease(price=0, taxe=0, format=False):
    res = price - (price * taxe / 100)
    return res if format is False else moeda(res)


def double(price=0, format=False):
    res = price * 2
    return res if format is False else moeda(res)



def half(price=0, format=False):
    res = price / 2
    return res if format is False else moeda(res)


def moeda(price=0, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.', ',')
    #o comando [replace] faz com que substitua um 'x' caracter do python
    #por um 'y' caracter escolhido neste caso: '.' por ','