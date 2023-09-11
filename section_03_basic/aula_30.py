"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega


# Meu código anteriormente
# if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
#     if velocidade > RADAR_1:
#         print("Multado...")
#     else:
#         print("Boa viagem...")

enter_range = local_carro > LOCAL_1 - RADAR_RANGE
leave_range = local_carro > LOCAL_1 + RADAR_RANGE
is_in_range = enter_range and not leave_range

above_speed_limit = velocidade > RADAR_1

if is_in_range and above_speed_limit:
    print("Você foi multado por excesso de velocidade!")
else:
    print("Boa viagem!")
