import matplotlib.pyplot as plt
import char_recognition as cr

fraction = []

hidden_sizes = [25, 50, 100, 200, 400]
for h in hidden_sizes:
    f = cr.main(do_plots=False, hidden_layer_size=h)
    fraction.append(f)


plt.plot(hidden_sizes, fraction)
plt.xlabel("hidden layer size")
plt.ylabel("success fraction")
plt.tight_layout()
plt.savefig("hidden_layer_trends.png", dpi=150)

for h, e in zip(hidden_sizes, fraction):
    print(h, e)
