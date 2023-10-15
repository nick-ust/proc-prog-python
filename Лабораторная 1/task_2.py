# TODO Найдите количество книг, которое можно разместить на дискете
memory = 1.44   # Mb
symbol_size = 4    # b

Kb_in_Mb = 1024
b_in_Kb = 1024

pages = 100
lines_per_page = 50
symbols_per_line = 25

memory_in_bytes = memory * Kb_in_Mb * b_in_Kb
symbols_in_book = pages * lines_per_page * symbols_per_line
book_size = symbol_size * symbols_in_book

books = int(memory_in_bytes // book_size)

print("Количество книг, помещающихся на дискету:", books)
