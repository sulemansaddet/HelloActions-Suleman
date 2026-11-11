import os

# Read the name from the WHO_TO_GREET environment variable, default to 'Student' if not set
name = os.environ.get('WHO_TO_GREET', 'Student')

# Print the greeting
print(f"Hello {name}!")

# Print the confirmation message
print("This program is running inside GitHub Actions.")
