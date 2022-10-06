import random


# 1. random() Generate a random number
num = random.random()
print (num)

# 2. sample([] list, int num) Get num samples from the list
sample = random.sample([1,2,3,4,5,6], 3)
print(sample)

# 3. uniform(int a, int b) Generate a random number in [a,b]
num = random.uniform(100, 105)
print(num)

# 4. randint(a,b) Generate an integer number in [a,b]
num = random.randint(100, 105)
print(num)

# 5. randrange(start, stop, step) Generate a random number in seq (start, start + step, ..., stop)
num = random.randrange(100, 200, 3)
print(num)

# 6. choice([]) Select a random one from the list
sample = random.choice([999, "Hello", 'a'])
print(sample)

# 7. shuffle([]) Shuffle the list
list = ['H', 'e', 'l', 'l', 'o']
random.shuffle(list)
print(list)