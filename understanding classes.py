# warna jenis bunga
class Bunga:
    def __init__(self, jenis, warna):
        self.jenis = jenis
        self.warna = warna
    
    def display_color(self):
        print(self.jenis)

rose_flower = Bunga("rose", "red")
print(rose_flower.color)
rose_flower.display_warna()

print(" ")

# membuat pie
class Pie:
    def __init__(self, flavour, ingredients):
        self.flavour = flavour
        self.ingredients = ingredients

    def print_ingredients(self):
        for i in self.ingredients:
            print(i)
        
apple_pie = Pie("apple", ["flour", "eggs", "apples", "butter"])
apple_pie.print_ingredients()

print(" ")

# seri buku dan jumlah seri buku
class BookSeries:
  def __init__(self, name, books):
    self.name = name
    self.books = books
    self.num_books = len(books)


  def print_name(self):
    print(self.name)
    
  def print_books(self):
    print(self.books)

hg = BookSeries("Hunger Games", ["The Hunger Games", "Catching Fire", "Mockingjay"])

hg.print_books()
print(hg.num_books)
