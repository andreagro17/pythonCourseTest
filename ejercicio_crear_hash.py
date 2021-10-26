import hashlib

# file = './01001c.csv'
def hash_create(file): 

    coded_file = file.encode()
    hash_file = hashlib.sha256(coded_file)
    return hash_file.hexdigest()



file = input('Introduce la ruta del fichero')
print('Hexadec format: ', hash_create(file))