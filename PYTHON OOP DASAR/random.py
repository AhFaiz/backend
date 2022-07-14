import random
x = random.randint(2,99) #outputna bilangan antara 2 dan 99
print(x)

print(random.random()) #outputnya data float

pilihan = ['kertas','gunting','batu']
x = random.choice(pilihan) #outputnya hasil acak dari list
print(x)

pilihan = ['toyota','ferrari','hyundai','lamborghini','bugatti']
random.shuffle(pilihan) #outputnya ngerandom value yang ada di dalam list
print(pilihan)