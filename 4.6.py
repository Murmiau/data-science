from itertools import count

for n in count(5):
    if n > 15:
        break
    else:
        print(n)

from itertools import cycle

count = 0
for i in cycle('345'):
    if count > 5:
        break
    print(i)
    count += 1
