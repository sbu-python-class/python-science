import matplotlib.pyplot as plt
import char_recognition as cr

train_set = cr.TrainingSet()

d = train_set.get_next()
d.plot()
plt.tight_layout()
plt.savefig("example_digit.png", bbox_inches="tight", dpi=150)
