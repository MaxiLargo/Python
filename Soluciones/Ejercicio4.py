# 3kg por cada centimetro hasta 3 metros
# 2kg por cada cm arriba de los 3 metros

# 2m => 200 cm => 600kg
# 3m => 300 cm => 900kg
# 5 => 500 cm => 300 cm => 900kg 
#                  +
#                200 cm => 400kg   == 1300kg


def peso_pino(pino:int)->int:
     res:int = 0
     if(pino<=3):
          res = (pino*100)*3
     else:
          res = 900 + (((pino-3)*100)*2)
      
     return res

print(peso_pino(5))

def es_peso_util(peso:int)->bool:
     res:bool = False 
     if (peso>=400 and peso <= 1000):
          res = True
     return res

print(es_peso_util(390))

def sirve_pino()
     