def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):
    total_notas = 0
    num_alunos = len(notas)
    aprovados = []
    reprovados = []

    for aluno, nota in notas.items():
        total_notas += nota
    if nota >= nota_minima_aprovacao:
        aprovados.append(aluno)
    else:
        reprovados.append(aluno)

    media_turma = total_notas / num_alunos

    return media_turma, aprovados, reprovados

notas = {
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

nota_minima_aprovacao = 70

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")