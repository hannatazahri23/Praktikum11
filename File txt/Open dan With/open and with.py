print("="*3,'Membaca File txt',"="*3)
file = open("data.txt", mode ="r")
# print(file.read())
#print(file.readline(), end = "") #baris pertama
#print(file.readline(),) # baris kedua
print(file.readlines())

print(f"Status read : {file.readable()}")
print(f"Status write : {file.writable()}")

print(f"apakah file suda di close : {file.closed}")
file.close()
print(f"apakah file sudah diclose : {file.closed}")

#salah satu teknik membaca file dengan with
print()
print("====Program file menggunakan with====")

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah diclose : {file.closed}")
print(f"apakah file sudah diclosed : {file.closed}")