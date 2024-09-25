# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).
def verificar_aprovacao():
    aprovados = 0
    total_alunos = 5

    for i in range(total_alunos):
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        
        if nota >= 7:
            aprovados += 1

    print(f"Número de alunos aprovados: {aprovados}")

verificar_aprovacao()