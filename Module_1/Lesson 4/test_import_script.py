import random
import example_module
from ..example_module_2 import ex_var_2

print(f"This is the example_modules __name__ var: {__name__}")
print(f"This var is acessible both inside this module and example_module, here is its value: {example_module.example_var}")
print(f"This is a random var:{random.random():10.4f}")
print(f"This is a dir() call for random module: {dir(random)}")
print(example_module.example_var)
print(ex_var_2)
