import random, os

class JogoDaForca():

    def __init__(self):

        # Palavras possiveis para o jogo
        self.words = ['carro', 'moto', 'lanchas', 'jetski', 'pedestres', 'banhistas', 'nutella', 'bolo']

        # Palavra escolhida
        self.choosen_word = random.choice(self.words)

        # Lista com as letras ocultas/adivinhadas pelo usuario
        self.correct_letters = ["_" for letter in self.choosen_word]

        # Tentativas maximas
        self.remaining_tries = 6

        # Lista com as letras erradas
        self.wrong_letters = []

        self.in_game()

    def in_game(self):
        """Renderiza as mensagens que aparecem no terminal durante o jogo."""
        while True:
            
            self.clear_terminal()

            print("Bem vindo(a) ao jogo da forca!\n")

            # Imprime as letras adivinhadas
            for letter in self.correct_letters:
                print(letter, end=" ")

            # Imprime as letras usadas e tentativas restantes
            print("\n\nLetras erradas: ", end=" ")
            for letter in self.wrong_letters:
                print(letter, end=" ")
            print(f"\nTentativas restantes: {self.remaining_tries}")

            # Verifica se o jogo acabou
            if self.remaining_tries<=0:
                print(f"Voce perdeu! A palavra era {self.choosen_word}\n")
                break
            elif "_" not in self.correct_letters:
                print("Voce venceu!!! Parabens!!!\n")
                break

            # Pede para o usuario digitar uma letra
            letter = input("\nDigite uma letra: ")

            # Verifica se a letra esta na palavra
            if letter in self.choosen_word:

                # Varre a lista de letras adivinhadas substituindo "_" pela letra informada
                for index, choosen_word_letter in enumerate(self.choosen_word):
                    if letter == choosen_word_letter:
                        self.correct_letters[index] = letter
            else:
                self.remaining_tries-=1
                self.wrong_letters.append(letter)

                




    def clear_terminal(self):
        """Realiza a verificação do sistema operacional corrente e limpa o terminal."""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            


if __name__=="__main__":
    game = JogoDaForca()