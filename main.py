class books:
    def __init__(self, name, author, date):
        self.name = name
        self.author = author
        self.date = date
    def display_info(self):
        print(f"Название: {self.name}, Автор: {self.author}, Год выпуска: {self.date}")
book1 = books("Война и мир", "Лев Толстой", 1869)
book2 = books("Евгений Онегин", "Пушкин", 1833)
book1.display_info()
book2.display_info()
