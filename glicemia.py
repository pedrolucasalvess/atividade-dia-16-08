def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): # Nessa linha é criado a função diagnosticar_diabetes, dentro dela estão inseridas as variáveis glicemia_em_jejum e glicemia_pos_prandial

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: # Nessa linha é criado a 
        return "Diabetes"
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
        return "Pré-diabetes"
    else:
        return "Normal"

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
print(f"O diagnóstico é: {resultado}")