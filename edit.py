#example for adding a book to database
the_legendary_mechanic = Book(title="The Legendary Mechanic",author="Qi Peijia",form="Web Novel",length = "1463",status = "C",date_start = datetime.date(2023,1,3),date_end = datetime.date(2023,3,27))
session.add(the_legendary_mechanic)
session.commit()

#deleting first line in table
session.delete(session.query(Book).first())
session.commit()

#print table
books = session.query(Book)
for book in books:
    print(book.title)
