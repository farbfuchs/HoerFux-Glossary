import yaml
import sys
import random

"""Helper function to load YAML data from file."""
def load_yaml(path):
    try:
        with open(path, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data
    except FileNotFoundError:
        print("File not found!")
        sys.exit()
    except yaml.YAMLError as error:
        print("YAML parsing error:", error)
        sys.exit() 

"""Main entry point of the program."""
def main():
    path = "./glossary.yml"
    data = load_yaml(path)

    # Random selection
    random_key = random.choice(list(data.keys()))
    random_value = data[random_key]
    print("Welcome to the HoerFux-Glossary \n \n Random selection from glossary \n {} -> {} \n".format(random_key, random_value))

    # See all values
    see_all = input("Do you want to see all words in the HoerFux-Glossary (y/n)")    
    if see_all == 'y':
        print("All words in glossary: \n")
        [print(keys) for keys in data]
        print("\n")

    ask_glossary = input("Would you like to see the meaning of a word in the HoerFux-Glossary (y/n)?")    
    
    # Loop for input
    while ask_glossary == 'y':
        key = input("Enter a word: ")
        if key in data:
            value = data[key]
            print("Value:", value)
        else:
            print("Word not found!")

        ask_glossary = input("Do you want to enter another word (y/n)?")

    print("Thank you for using HoerFux-Glossary!")
    

if __name__ == "__main__":
    main()
