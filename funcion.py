def analisis(linea):
    partes = linea.split()
    print(partes)
    return partes


linea = "Hola dime tu clave, para poder entrar"
partes = analisis(linea)

res = [p.replace('a', '*').replace(',','') for p in partes]

print(res)