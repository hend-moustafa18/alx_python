import sys

# Get the number of arguments
num_args = len(sys.argv) - 1

# Print the number of arguments
if num_args == 0:
    print("Number of argument(s): .")
else:
    print(f"Number of argument{'s' if num_args > 1 else ''}: {num_args}")

# Print the list of arguments
for i, arg in enumerate(sys.argv[1:]):
    print(f"{i + 1}: {arg}")