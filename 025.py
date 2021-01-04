divisor = 20201227

subject = 7

card_public_key = 17773298
door_public_key = 15530095

def transform(subject, loop_size):
    key = 1
    for _ in range(loop_size):
        key *= subject
        key = key % divisor
    
    return key

def brute_key(key):
    value = 1
    loop_size = 0

    while value != key:
        loop_size += 1
        value *= subject
        value = value % divisor

    return loop_size

card_loop_size = brute_key(card_public_key)
door_loop_size = brute_key(door_public_key)

print(card_loop_size, door_loop_size)

print(transform(door_public_key, card_loop_size))
print(transform(card_public_key, door_loop_size))