import hashlib
import cProfile

def generate_hash(base_hash, amount):
    counter = 0
    while True:
        text = (base_hash + str(counter)).encode()
        hash_ = hashlib.md5(text).hexdigest()
        if hash_.startswith("0" * amount):
            break
        counter +=1 
    return counter
    
print(generate_hash('ckczppom', 5))
print(generate_hash('ckczppom', 6))
