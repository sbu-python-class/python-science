import matplotlib.pyplot as plt
import char_recognition as cr

fraction = []

learning_rate = [0.05, 0.1, 0.2, 0.3, 0.4]
for l in learning_rate:
    f = cr.main(do_plots=False, learning_rate=l)
    fraction.append(f)


plt.plot(learning_rate, fraction)
plt.xlabel("learning rate")
plt.ylabel("success fraction")
plt.tight_layout()
plt.savefig("learning_rate_trends.png", dpi=150)

for l, e in zip(learning_rate, fraction):
    print(l, e)
