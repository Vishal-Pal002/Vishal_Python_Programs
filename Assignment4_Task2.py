filename = "output.txt"

text_to_write = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(text_to_write + "\n")
print(f"Data successfully written to {filename}.")

additional_text = input("\nEnter additional text to append: ")
with open(filename, "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.\n")

print(f"Final content of {filename}:")
with open(filename, "r") as file:
    content = file.read()
    print(content)

