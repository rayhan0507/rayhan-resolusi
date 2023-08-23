# kalkulator jarak

def kilometer_to_miles(km):
    miles = km * 0.621371
    return miles

def miles_to_kilometer(miles):
    km = miles / 0.621371
    return km


print("kalkulator jarak")
print("pilih salah satu")

print(" ")

print("1. kilometer ke miles")
print("2. miles ke kilometer")


def main():
    choice = int(input("pilih 1 atau 2: "))

    if choice == 1:
       km = float(input("pilih jumlah km"))
       miles = kilometer_to_miles(km)
       print(f"km: {km} = {miles} miles")

    elif choice == 2:
        miles = float(input("pilih jumlah miles"))
        km = miles_to_kilometer(miles)
        print(f"{miles} miles = {km} km")
    else:
        print("error cuma bisa ketik 1 sampai 2")

if __name__ == "__main__":
    main()