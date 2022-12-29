#!/usr/bin/env python3
# _*_ coding: utf8 _*_

# importando o método randint do módulo random
from random import randint

# Módulo click para argumentos
from click import argument as c_argument
from click import command as c_command
from click import option as c_option

# Criação de um set
s = set()

# Textos de ajuda para os parâmetros
h_numeros = 'Quantidade de números apostados (padrão 6)'
h_apostas = 'Quantidade de apostas (padrão 1)'
h_cartela = 'Quantidade de números na cartela (padrão 60)'


# Configuração dos parâmetros do script
@c_command()
@c_option('--numeros', '-n', type=int, default=6, help=h_numeros)
@c_option('--apostas', '-a', type=int, default=1, help=h_apostas)
@c_option('--cartela', '-c', type=int, default=60, help=h_cartela)
def apostar(numeros: int = 6, apostas: int = 1, cartela: int = 60) -> None:
    # Criação de um set
    s = set()

    # Quantoss dígitos a quantidade de número tem
    digitos = len(str(cartela))

    for i in range(apostas):
        # Enquanto o tamanho de s for menor que numeros
        while (len(s) < numeros):
            # Adicionar um número aleatório de 1 a quantidade de números
            # possíveis para se apostar
            n = str(
                    randint(1, cartela)
                   ).zfill(digitos)

            s.add(n)

        s = str(sorted(s))
        s = s.replace('[', '')
        s = s.replace(']', '')
        s = s.replace("'", '')
        print(s)
        s = set()


# Definição da função main
def main() -> None:
    apostar()


# Execução
if __name__ == '__main__':
    main()
