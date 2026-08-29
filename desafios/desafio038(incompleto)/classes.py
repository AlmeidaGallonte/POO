class Produto:
    def __init__(self, produto: str, preço: float):
        self.Produto = produto
        self.Preço = preço

    def __str__(self):
        return f'{self.Produto} (R${self.Preço:.2f})'


class Carrinho:
    def __init__(self, produtos=None):
        self.produtos = produtos if produtos is not None else []

    @property
    def total(self):
        return sum(p.Preço for p in self.produtos)

    
    def __add__(self, other):
        novos_produtos = self.produtos + [other]
        return Carrinho(novos_produtos)

    def __str__(self):
        
        itens = "\n".join(str(p) for p in self.produtos)
        return f'{itens}\n= Total: R$ {self.total:,.2f}'
    

            

    