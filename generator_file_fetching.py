def read_file(file_path):
    with open(file_path) as file:
        for i in file:
            yield i

file_path = "C:\\Users\\moham\\Desktop\\Ineuron_practice\\simple_document_test.txt"

for line in read_file(file_path):
    print(line)

# with encoding utf-8
def read_file(file_path):
    with open(file_path, encoding="utf-8") as file:
        for i in file:
            yield i

file_path = "C:\\Users\\moham\\Desktop\\Ineuron_practice\\simple_document_test.txt"

for line in read_file(file_path):
    print(line)