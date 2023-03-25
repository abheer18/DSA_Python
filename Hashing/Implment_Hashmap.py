class Hashmap():
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_value(self, key, val):

        #get index using hash function
        hashed_key = hash(key) % self.size

        #going to corresponding bucket
        bucket = self.hash_table[hashed_key]


        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record

            #checking if key already their, update it then
            #otherwise just append the key, value pair

        if found_key:
            bucket[index] = (key,val)
        else:
            bucket.append((key, val))

    #return the search value

    def get_value(self, key):

        # get index using hash function
        hashed_key = hash(key) % self.size

        # going to corresponding bucket
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_val
        else:
            return "No record found"

    def delete_value(self,key):

        # get index using hash function
        hashed_key = hash(key) % self.size

        # going to corresponding bucket
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(index)
        return

    def printt(self):
        return " ".join(str(item) for item in self.hash_table)


hash_table = Hashmap(50)

print("******HASHING IMPLEMENTATION******\n")

while True:
    print("1 ✔ SET THE VALUE")
    print("2 ✔ GET THE VALUE")
    print("3 ✔ DELETE THE VALUE")
    print("4 ✔ PRINT THE HASHTABLE/HASHMAP\n")

    ch = int(input("Enter the choice [1-4] : "))
    if(ch == 1):
        key = int(input("Enter the key: "))
        val = input("Enter the value: ")
        print(hash_table.set_value(key,val))

    elif(ch == 2):
        key = input("Enter the key: ")
        print(hash_table.get_value(key))

    elif(ch == 3):
        key = input("Enter the key you want to delete: ")
        print(hash_table.delete_value(key))

    elif(ch == 4):
        print(hash_table.printt())





