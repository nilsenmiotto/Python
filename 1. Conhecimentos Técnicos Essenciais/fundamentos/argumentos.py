import sys

print(len(sys.argv))  # Número de argumentos passados
print(sys.argv)  # Lista de argumentos passados

if(len(sys.argv) == 3):
    banco = sys.argv[1]
    debug = sys.argv[2]
    print("Banco:", banco)
    print("Debug:", debug)
else:
    print("Uso: python argumentos.py <banco> True/False")
    sys.exit(1)