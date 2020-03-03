class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


book = Book('Python rocks', 'Jose', 200)

# do you have a string representation in this class is called by book object
print(book)
# same thing is done by string representation
print(str(book))
# get the length of pages
print(len(book))
# delete variables
# del book

print(book)

