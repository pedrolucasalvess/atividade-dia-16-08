def calcular_area_comodos(): # Nessa linha é definido a função que será utilizada, a calcular_area_comodos
    total_area = 0 # Nessa linha é definido a variável total_area como 0, para q

    while True:

        largura = float(input("Digite a largura do cômodo (em metros): ")) # Nessa linha é criado a variável largura, que é definida pelo um input que só pode receber valor float perguntando o tamanho da largura do cômodo em metros
        comprimento = float(input("Digite o comprimento do cômodo (em metros): ")) # Nessa linha é criado a variável comprimento, que é definida pelo um input que só pode receber valor float perguntando o comprimento do cômodo em metros

        area_comodo = largura * comprimento # Nessa linha é criado a variável area_comodo, ela é definida pela multiplicação das variáveis largura e comprimento
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") 

        total_area += area_comodo

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower() # Nessa linha é criado a variável mais_comodos, junto com ela tem umu input perguntando para o usuário se ele deseja inserir ou não mais um cômodo, para responder em s/n, é utilizado as funcões .strip e .lower para tirar os espaços entre o texto que será inserido pelo usuário e também para deixar todas as palavras em letra minúscula, respectivmente
        if mais_comodos != 's': # Nessa linha é criado uma condição, se a reposta do usuário for diferente de s, ele finaliza a execução
            break # Nessa linha a execução é terminada

    return total_area # Nessa linha ele retorna o valor total da área 

area_total = calcular_area_comodos()
print(f"A área total da casa é: {area_total:.2f} metros quadrados.") # Nessa linha é printado para o usuário a área total da casa em metros quadrados