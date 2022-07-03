note = float(input("Informe a média do aluno: "))
isBehaved = True if input("É um aluno comportado (s/n)? ") == "s" else False

if note >= 9 and isBehaved:
    print("Parabéns! Continue assim")
elif note >= 7:
    print("O aluno foi aprovado por média")
elif note > 5 and note < 7:
    print("O aluno está em recuperação")
elif note < 0:
    print("Informe uma nota válida!")
else:
    print("O aluno foi reprovado!")
