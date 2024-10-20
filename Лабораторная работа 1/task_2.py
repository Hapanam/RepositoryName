# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44
pages = 100
lines= 50
chars = 25
bytes = 4
book = pages * lines * chars * bytes
disk = disk * 1024 * 1024
number = disk // book
print("Количество книг, помещающихся на дискету:", round(number))