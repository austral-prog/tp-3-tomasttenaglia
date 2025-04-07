def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
    print(texto[:3].lower())
    
    mitad = int(len(texto) / 2)
    total = len(texto)
    print(texto[mitad-1:mitad+2].lower())
    
    print(f'{texto[0:5]}{texto[total-2:]}'.lower())
    
    
    
    
    
    
    

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
