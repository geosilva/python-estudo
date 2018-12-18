#-*- coding: utf-8 -*-

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Primeira Nota: "))
nota2 = float(input("Segunda Nota: "))
nota3 = float(input("Terceira Nota: "))
nota4 = float(input("Quarta Nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4
print("A média das Notas é: %.2f" %media)
