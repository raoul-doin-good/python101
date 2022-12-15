my_file = open("my_file.txt", "w")

my_file.write("Hallo")
my_file.close()

read_file = open("my_file.txt")
for line in read_file.readlines():
    print(line)
