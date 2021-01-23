import matplotlib.pyplot as plt
import math

principal = 100000
rate = 10
number = 1
period = 5

amount = []
time = []

for i in range(1,21):
    time.append(i)

for period in range(1,21):
    amount.append(principal*((1+rate/100*number)**(number*period)))

plt.title("Power of Compounding(Rate:10% annual)")

plt.plot(time, amount)
plt.xlabel('Time (yr)')
plt.ylabel('Amount (GBP)')

plt.show()

plt.savefig('compounding.png')
