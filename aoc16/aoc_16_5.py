import hashlib

def get_password(door_code, number_of_hashes):
    password = ""
    counter = 0
    while True:
        new_code = door_code + str(counter)
        new_code = new_code.encode('utf-8')
        if hashlib.md5(new_code).hexdigest().startswith('00000'):
            password += hashlib.md5(new_code).hexdigest()[5]
            print(hashlib.md5(new_code).hexdigest()[5], end="")
        if len(password) == number_of_hashes:
            break
        counter += 1
    print("")
    return password

#get_password('abc', 8)
# get_password('uqwqemis', 8)

def get_advanced_password(door_code, number_of_hashes):
    password = {'0': '_',
                '1': '_',
                '2': '_',
                '3': '_',
                '4': '_',
                '5': '_',
                '6': '_',
                '7': '_'}
    counter = 0
    found = 0
    while True:
        new_code = door_code + str(counter)
        new_code = new_code.encode('utf-8')
        if hashlib.md5(new_code).hexdigest().startswith('00000'):
            hash_ = hashlib.md5(new_code).hexdigest()
            if hash_[5] in password:
                if password[hash_[5]] == '_':
                    password[hash_[5]] = hash_[6]
                    print("".join([password[x] for x in password]))
                    found += 1
        if found == number_of_hashes:
            break
        counter += 1
    print("")
    return password

# get_advanced_password('abc', 8)
get_advanced_password('uqwqemis', 8)
