#!/usr/bin/env python3

# importando o método randint do módulo random
from random import randint

# Módulo click para argumentos
from click import argument as c_argument
from click import command as c_command

# Criação de um set
s = set()


@c_command
@c_argument(
def apostar(qtd_num_apostados:int=6, apostas:int=1, qtd_num:int=60) -> None:
    # Criação de um set
    s = set()

    # Quantoss dígitos a quantidade de número tem
    digitos = len(str(qtd_num))

    for i in range(apostas):
        # Enquanto o tamanho de s for menor que 6
        while (len(s) < qtd_num_apostados):
            # Adicionar um número aleatório de 1 a quantidade de números
            # possíveis para se apostar
            n = str(
                    randint(1, qtd_num)
                   ).zfill(digitos)

            s.add(n)

        s = str(sorted(s))
        s = s.replace('[', '')
        s = s.replace(']', '')
        s = s.replace("'", '')
        print(s)

def main() -> None:
    pass

if __name__ == '__main__':
    main()

