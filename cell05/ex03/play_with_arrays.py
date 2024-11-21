original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = [x + 2 for x in original_array if x > 5]

unique_original = set(original_array)
unique_new = set(new_array)

print(f"{list(unique_original)}$")
print(f"{sorted(unique_new)}$")