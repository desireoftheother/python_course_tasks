import random
import example_module

print(f"This is the example_modules __name__ var: {example_module.__name__}")
print(f"This var is acessible both inside this module and example_module, here is its value: {example_module.example_var}")
print(f"This is a random var:{random.random():10.4f}")
print(f"This is a dir() call for random module: {dir(random)}")
