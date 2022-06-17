import numpy as np
import random
from utils import add_class

output_el = Element('output').element

arr = np.array([22, 58, 57, 87, 34, 5])

# pyscript.write('output', f"{arr}")
output_el.innerHTML = f"{arr}"

def shuffle_array(*args):
  # Suffle
  shuffled = sorted(arr, key=lambda k: random.random())

  # Change color
  add_class(output_el, "text-blue-500")

  output_el.innerHTML = shuffled
  # pyscript.write('output', shuffled)