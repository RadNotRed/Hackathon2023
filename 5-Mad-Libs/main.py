def mad_libs():
    print("Welcome to Mad Libs! Please select a story:")
    print("1. The Amazing Adventurer")
    print("2. The Majestic Filed")
    print("3. An Afternoon on the Beach")
    print("4. The Crazy Scientist")
    print("5. The Scary Farm")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        adjective = input("Enter an adjective: ")
        noun1 = input("Enter a noun: ")
        verb1 = input("Enter a verb: ")
        adverb = input("Enter an adverb: ")
        noun2 = input("Enter a noun: ")
        verb2 = input("Enter a verb ending in -ing: ")
        print(f"The {adjective} {noun1} {verb1} {adverb} through the {noun2} while {verb2}.")

    elif choice == "2":
        verb1 = input("Enter a verb: ")
        adjective1 = input("Enter an adjective: ")
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter a noun: ")
        verb2 = input("Enter a verb ending in -ing: ")
        adjective2 = input("Enter an adjective: ")
        print(f"The {verb1} {adjective1} {noun1} and {noun2} were {verb2} under the {adjective2} sky.")

    elif choice == "3":
        noun1 = input("Enter a noun: ")
        verb1 = input("Enter a verb: ")
        adjective1 = input("Enter an adjective: ")
        noun2 = input("Enter a noun: ")
        verb2 = input("Enter a verb: ")
        adjective2 = input("Enter an adjective: ")
        print(f"A {noun1} was {verb1} on the {adjective1} beach. The {noun2} {verb2} {adjective2} in the sun.")

    elif choice == "4":
        adjective1 = input("Enter an adjective: ")
        noun1 = input("Enter a noun: ")
        verb1 = input("Enter a verb: ")
        adjective2 = input("Enter an adjective: ")
        noun2 = input("Enter a noun: ")
        verb2 = input("Enter a verb: ")
        print(f"The {adjective1} {noun1} {verb1} the {adjective2} {noun2} {verb2}.")

    elif choice == "5":
        verb1 = input("Enter a verb ending in -ing: ")
        noun1 = input("Enter a noun: ")
        adjective1 = input("Enter an adjective: ")
        verb2 = input("Enter a verb ending in -ing: ")
        noun2 = input("Enter a noun: ")
        print(f"The {verb1} {noun1} was very {adjective1} and {verb2} on the {noun2}.")

    else:
        print("Invalid choice. Please try again.")


mad_libs()
