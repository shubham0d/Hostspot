import random

def randomIdGenerator():
    hashId = random.getrandbits(128)
    return hashId
