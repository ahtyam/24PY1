bytes_in_kilobyte_count = 1024
kilobytes_in_megabyte_count = 1024

symbol_volume_in_bytes = 4
symbols_in_string_count = 25
bytes_in_string_count = symbol_volume_in_bytes * symbols_in_string_count

strings_in_page_count = 50
bytes_in_page_count = bytes_in_string_count * strings_in_page_count

pages_in_book_count = 100
bytes_in_book_count = bytes_in_page_count * pages_in_book_count

floppy_volume_in_megabytes = 1.44
floppy_volume_in_kilobytes = floppy_volume_in_megabytes * kilobytes_in_megabyte_count
floppy_volume_in_bytes = floppy_volume_in_kilobytes * bytes_in_kilobyte_count

books_in_floppy_count = int(floppy_volume_in_bytes // bytes_in_book_count)

print("Количество книг, помещающихся на дискету:", books_in_floppy_count)
