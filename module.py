    # This will create 'new_file.txt' if it doesn't exist, or overwrite it if it does
with open('new_file.txt', 'w') as f:
        f.write('Hello, world!')

    # This will create 'another_file.txt' but raise an error if it already exists
with open('another_file.txt', 'x') as f:
        f.write('Exclusive content.')