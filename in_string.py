def check_vowels():
    # Código a implementar utilizando input.
    nombre = input().lower()
    
    
    a= ("a" in nombre)
    e= ("e" in nombre)
    i= ("i" in nombre)
    o= ("o" in nombre)
    u= ("u" in nombre)
    
    
    
    print(f'Contiene a: {a}')
    print(f'Contiene e: {e}')
    print(f'Contiene i: {i}')
    print(f'Contiene o: {o}')
    print(f'Contiene u: {u}')
    


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
