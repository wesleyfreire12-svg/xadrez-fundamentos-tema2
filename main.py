class Xadrez Erro(Exception):
    """Classe para tratar erros customizados no jogo."""
    pass

class Peca:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def validar_posicao(self, x, y):
        # Técnica avançada: Validação preventiva
        if not (0 <= x < 8 and 0 <= y < 8):
            raise Xadrez Erro(f"Posição ({x}, {y}) é inválida para o tabuleiro 8x8.")
        return True

class Tabuleiro:
    def __init__(self):
        self.__grade = [[None for _ in range(8)] for _ in range(8)] # Atributo privado

    def posicionar_peca(self, peca, x, y):
        try:
            if peca.validar_posicao(x, y):
                self.__grade[x][y] = peca
                print(f"Sucesso: {peca.nome} colocada em ({x}, {y})")
        except Xadrez Erro as e:
            print(f"Falha de Fundamentos: {e}")

if __name__ == "__main__":
    tabuleiro = Tabuleiro()
    bispo = Peca("Bispo", "Branco")
    
    # Testando técnica de tratamento de erro
    tabuleiro.posicionar_peca(bispo, 2, 2) # Deve funcionar
    tabuleiro.posicionar_peca(bispo, 10, 5) # Deve disparar o erro tratado
