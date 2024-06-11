# def suma(num1, num2):
#     """_summary_
#         Suma de dos numeros enteros
#     Args:
#         num1 (int): _description_
#         num2 (int): _description_

#     Returns:
#         int: Suma de dos numeros enteros
        
#     >>> suma(4,8)
#     22
#     >>> suma(19,2)
#     21
#     """
#     return num1 + num2


# Para ejecutarlo ==> python -m doctest Testing.py -v ==> POR CMD
  
    

def invertir_cadena(palabra):
    """_summary_
    Funcion que invierte una cadena

    Args:
        palabra (str): _description_
    
    Returns:
        str: Palabra invertida
    
    >>> invertir_cadena("Python")
    'nohtyP'
    
    >>> invertir_cadena("Perro")
    'orrPe'
    """
    return palabra[::-1]

