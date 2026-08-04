from POO.desafios.desafio032.classe32 import ContaBancaria

def main():
    cc = ContaBancaria(222, "jamerson", 10_000,'123456')
    print('tentando mudar o nome...')
    cc.nome = 'nonune'
    print(cc)
if __name__ == '__main__':
    main()