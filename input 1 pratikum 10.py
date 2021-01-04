def read(source):
    file = open(source, 'r')
    ganjil = 0
    genap = 0
    for i in file:
        if int(i) % 2 == 0 :
            genap += 1
        elif int(i)% 2 == 1:
                ganjil += 1
    file.close()
    result = {"ganjil" : ganjil,
                   "genap" : genap}
    return result
source = "databilangan.txt"
print("Banyaknya bilangan ganjil: ", read(source).get('ganjil'))
print("Banyaknya bilangan genap: ", read(source).get('genap'))
