paisA:float = 25000000
paisB:float = 18900000
año = 2022
while(True):
  paisA*=1.02
  paisB*=1.03
  año+=1
  if(paisB>paisA):
    print("Población país A " + str(paisA) + " - " + "Población país B " + str(paisB))
    print("El año en el que el país B superará al país A será en el " + str(año))
    break
    
