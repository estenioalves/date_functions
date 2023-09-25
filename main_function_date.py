from functions import *

print("############\n")
print("Qual a data de vencimento?\n")
print("############\n")

due_date = input('Insira a data DIA/MES/ANO:\n')

print(verify_due(due_date))
