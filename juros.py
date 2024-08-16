def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): # Define o nome da função "calcular_juros_atraso", nessa função está inserido as variáveis de valor principal, texa juros anual e dias de atraso.
    
    taxa_juros_diaria = taxa_juros_anual / 365 / 100 # Nessa linha a variável de taxa_juros_diaria é definida, essa variável representa a divisão do valor da taxa de juros anual por 365, que representa um ano, e posteriormente por 100, tendo assim a taxa de juros diária 

    
    juros = valor_principal * taxa_juros_diaria * dias_atraso # Nessa linha a variavel juros é definida, ela representa a multiplicação do valor principal, com a taxa de juros diária e pelo juros diário, obtendo assim o valor do jutps

    valor_total = valor_principal + juros # Nessa linha está definido a variável do valor total, que é representada pela soma do valor principal e pelo juros
    return valor_total, juros # Nessa linha está retornando o 

valor_principal = 1000.00 # Nessa linha é definido o valor da variável valor_principal, que é 1000.00
taxa_juros_anual = 5.0 # Nessa linha é definido o valor da variável taxa_juros_anual, que é 5
dias_atraso = 30 # Nessa linha é definido o valor da variável dias_atraso, que é 30
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso) # Nessa linha é onde acontece todas as operações da função calcular_juros_atrasado
print(f"Valor total a ser pago: R${valor_total:.2f}") # Nessa linha é printada pro usuário o valor total a ser pago, nesse caso
print(f"Valor dos juros: R${juros:.2f}")