def array_of_names(persons):
    # Create an array to hold the full names
    full_names = []
    
    # Loop through the dictionary to format the names
    for first, last in persons.items():
        # Capitalize first and last names and combine them
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    
    # Return the array of full names
    return full_names

# Dictionary of persons (example)
persons = { 
    "jean": "valjean", 
    "grace": "hopper", 
    "xavier": "niel", 
    "fifi": "brindacier" 
}

# Call the function and print the result
print(array_of_names(persons))