class Brand:
    def __init__(self, name = "BMW", color = "white"):
        self.name = name
        self.color = color
        self.tipe = None

class Type(Brand):
    def __init__(self, name = "bmw", tipe = "SEDAN"):
        super().__init__(name)
        self.tipe = tipe

        
    
    def display_info(self):
        if self.tipe:
            print(f"brand: {self.name}")
            print(f"tipe: {self.tipe}")
            print(f"color: {self.color}")

tipe = Type()
tipe.display_info()

for i in range(4):
    print(" ")

# cara 2

class Brand:
    def __init__(self, name):
        self.name = name
        self.type = type

class Jenis:
    def __init__(self, tipe = "SUV"):
        self.tipe = tipe
        self.brand = None
        
    def set_brand(self, brand):
        self.brand = brand

    def display_info(self):
        if self.brand:
            print(f"brand: {self.brand.name}")
            print(f"tipe: {self.tipe}")
            
brand1 = Brand("toyota")
tipe = Jenis()
tipe.set_brand(brand1)
tipe.display_info()
