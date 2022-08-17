x=float(input("digite quantos cigaros você fuma por dia: "))
ano=int(input(" digite quantos anos você fuma :"))
y=(((x * 10)/60)/24)
z=(ano * 365 * 0.007)
p= y + z
print (f"os dias perdidos é de {z:5.2f}")

