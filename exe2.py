print(f"A soma é:{soma}")
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a seguanta nota: '))
nota3 =int(input('Digite a terceira nota:'))

# Calcula a soma e a média das notas
soma = nota1 + nota2 + nota3
media = soma /3

#Mostra a soma e ameia
print(f"Soma das notas: {soma:.22f}")
print(f"Meida das notas: {media:.2f}")

# Verida se o aluno foi promovido pu retido
if media >= 70:
    print("Aluno promovido.")
else:
    print("Aluno retido.")