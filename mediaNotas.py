notaG1 = float(input("Insira a nota do G1: "))
notaG2 = float(input("Insira a nota do G2: "))

mediaNotas = (notaG1 + notaG2)/2

if mediaNotas >= 9:
    print("Você foi APROVADO com conceito A. A sua nota do G1 foi", notaG1, "e a sua nota do G2 foi", notaG2, ". Sua média final é igual a", mediaNotas)
elif mediaNotas < 9 and mediaNotas >= 7.5:
    print("Você foi APROVADO com conceito B. A sua nota do G1 foi", notaG1, "e a sua nota do G2 foi", notaG2, ". Sua média final é igual a", mediaNotas)
elif mediaNotas < 7.5 and mediaNotas >= 6:
    print("Você foi APROVADO com conceito C. A sua nota do G1 foi", notaG1, "e a sua nota do G2 foi", notaG2, ". Sua média final é igual a", mediaNotas) 
elif mediaNotas < 6 and mediaNotas >= 4:
    print("Você foi REPROVADO com conceito D. A sua nota do G1 foi", notaG1, "e a sua nota do G2 foi", notaG2, ". Sua média final é igual a", mediaNotas)   
elif mediaNotas < 4 and mediaNotas >= 0:
    print("Você foi REPROVADO com conceito E. A sua nota do G1 foi", notaG1, "e a sua nota do G2 foi", notaG2, ". Sua média final é igual a", mediaNotas)                   