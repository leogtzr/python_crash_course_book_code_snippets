while True:
    user_input = input("? ('q' to exit): ")
    if user_input == 'q':
        break

    o_occurrences = user_input.lower().count('o')
    print(f"'o' appears {o_occurrences} times")
