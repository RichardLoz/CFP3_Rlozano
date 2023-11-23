aventura = "X"
familiar = "Y" 
codigo = input("Ingrese el codigo verificador: ")
precio = int(input("Ingrese su precio "))


if codigo[-1] == "x" and precio > 50000:
    print("Aventura")

    if codigo[-1] == "Y" and precio < 20000 or precio > 50000:
        print("familiar")

else: 
    print (f"la entrada pertemece a generales")




# if  (entradas   50.000 and aventura == "x"):
#     print(f"La entrada pertemece ala categoria aventura ")
#     if (entradas > 20.00 or entradas < 50.000 and familiar == "Y"):
#         print(f"La entrada pertenece ala categoria familiar ")
    

# else :
#    print(f"{entradas} pertenece a entradas generales") 
   