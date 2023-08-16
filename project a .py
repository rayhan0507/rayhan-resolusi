harga = [10, 20, 30, 40, 50, 60]

def distribusi(num):
    price = num/2
    return price <= 20

result = [distribusi(num) for num in harga]
print(result)