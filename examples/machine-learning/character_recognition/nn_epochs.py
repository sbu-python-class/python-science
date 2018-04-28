import matplotlib.pyplot as plt
import char_recognition as cr

epoch = []
fraction = []

for e in range(1, 10):
    f = cr.main(do_plots=False, n_epochs=e)
    epoch.append(e)
    fraction.append(f)

plt.plot(epoch, fraction)
plt.xlabel("number of training epochs")
plt.ylabel("success fraction")
plt.tight_layout()
plt.savefig("epoch_trends.png", dpi=150)

for e, f in zip(epoch, fraction):
    print(e, f)
