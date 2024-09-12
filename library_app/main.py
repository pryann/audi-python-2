import books

while True:
    command = input("""
      Válaszd ki melyik műveletet szeretnéd végrehajtani
      1. Könyvek listázása
      2. Könyv keresése
      3. Könyv frissítése
      4. Könyv létrehozása
      5. Köny törlése
      6. Kilépés                   
        """)

    if command == "1":
        books.list_books()
    elif command == "2":
        books.find_book_by_id()
    elif command == "3":
        books.update_book()
    elif command == "4":
        books.create_book()
    elif command == "5":
        books.remove_book()
    elif command == "6":
        break
    else:
        print("Kérlek 1 és 6 között válasz valamailyen parancsot!")
