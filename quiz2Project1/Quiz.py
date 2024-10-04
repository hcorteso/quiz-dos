from typing import final

nombre = "luis Vejarano"
salario = 785000
dias = 7

prima = (salario*dias)/360
cesantias = (salario*dias)/360
interesesCesantias = (cesantias*0.12)/dias
vacaciones = (salario*dias)/720


print(f"Señor {nombre} para los {dias} laborados y salario {salario}, su liquidacion se compone asi: "
      f" Prima: {prima}"
      f" Cesantias: {cesantias}"
      f" Intereses a las cesantias: {interesesCesantias}"
      f" Vacaciones: {vacaciones}"
      f" Liquidación : {prima+cesantias+interesesCesantias+vacaciones}")


