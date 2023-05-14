example_var = "This variable is accessible both within this module and whenever it's being imported"

print("This is what happens when you are importing your module inside of another script")

if __name__ == "__main__":
    print("This is what happens when you are running this module as independent script")
    print(__name__)
