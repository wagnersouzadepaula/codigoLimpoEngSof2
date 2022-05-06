"""JOGO DE COMPUTADOR PARA JOGAR JOKENPO EM PYTHON."""

from funcoes import escolhaDaMaquina, escolhaDoUsuario,definirResultado, imprimeCabecalhoJogo, imprimeFimDoJogo

# MAIN
imprimeCabecalhoJogo()
escolhaDaMaquina = escolhaDaMaquina()
escolhaDoUsuario = escolhaDoUsuario()
definirResultado(escolhaDaMaquina, escolhaDoUsuario)
imprimeFimDoJogo()
