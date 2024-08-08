# Solicita ao usuário a nota do exame
nota = float(input("Digite a nota do exame: "))

# Usa uma expressão condicional para verificar se a nota é suficiente para aprovação
resultado = "Aprovado" if nota >= 5 else "Reprovado"

# Exibe a mensagem correspondente
print(f"O aluno foi {resultado}.")
