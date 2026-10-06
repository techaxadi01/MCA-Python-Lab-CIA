import numpy as np
import pandas as pd

arr = np.array([1, 2, 3])
df = pd.DataFrame({"numbers": arr})

print("NumPy:", arr, "| sum:", arr.sum())
print("Pandas:\n", df)