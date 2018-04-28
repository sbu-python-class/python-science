import matplotlib.pyplot as plt
import char_recognition as cr

fraction = []

training_size = [1875, 3750, 7500, 15000, 30000, 60000]
for t in training_size:
    f = cr.main(do_plots=False, num_training_unique=t)
    fraction.append(f)


plt.plot(training_size, fraction)
plt.xlabel("training sample size")
plt.ylabel("success fraction")
plt.tight_layout()
plt.savefig("training_size_trends.png", dpi=150)

for h, e in zip(training_size, fraction):
    print(h, e)
