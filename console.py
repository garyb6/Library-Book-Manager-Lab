import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("John Cleese")
author_repository.save(author1)
author2 = Author("Michael Caine")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("Fawlty Towers", "Comedy", "Harper Collins", author1)
book_repository.save(book1)

book2 = Book("Get Carter", "Crime", "Canongate", author2)
book_repository.save(book2)
