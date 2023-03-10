import fake_random
import example_module

print(f"This is the example_modules __name__ var: {example_module.__name__}")
print(f"This var is acessible both inside this module and example_module, here is its value: {example_module.example_var}")
