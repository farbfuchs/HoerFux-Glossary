import yaml
import sys
import random

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

def main():
    path = "./glossary.yml"
    data = load_yaml(path)
    randomKey = random.choice(list(data.keys()))
    randomValue = data[randomKey]
    print("Welcome Text to the HoerFux-Glossary \n The entry of the day is \n {} -> {} \n".format(randomKey, randomValue))
    seeAll = input("Do you want to see all words in the HoerFux-Glossary (y/n)")
    
    if seeAll == 'y':
        print("All words in glossary: \n")
        [print(keys) for keys in data]
        print("\n")

    askGlossary = input("Would you like to see the meaning of a word in the HoerFux-Glossary (y/n)?")    
    
    while askGlossary == 'y':
        key = input("Enter a word: ")
        if key in data:
            value = data[key]
            print("Value:", value)
        else:
            print("Word not found!")

        askGlossary = input("Do you want to enter another word (y/n)?")

    

if __name__ == "__main__":
    main()
