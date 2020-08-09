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
    return f'{coin}{price:>.2f}'.replace('.', ',')


def resume(price=0, taxeincrease=10, taxedecrease=5):
    print('-'*30)
    print('RESUME'.center(30)) #vai ficar centralizado nos 30 caracteres informados
    print('-' * 30)
    print(f'Price:\t\t{moeda(price)}')
    print(f'Increase:\t{increase(price, taxeincrease, True)}')
    print(f'Decrease:\t{decrease(price, taxedecrease, True)}')
    print(f'Double:\t\t{double(price, True)}')
    print(f'Half:\t\t{half(price, True)}')
    return '-'*30
