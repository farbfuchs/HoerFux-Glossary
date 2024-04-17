import yaml
import sys

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
    path = input("Enter the YAML file path: ")
    data = load_yaml(path)
    key = input("Enter the dictionary key to access: ")
    
    if key in data:
        value = data[key]
        print("Value:", value)
    else:
        print("Key not found!")

if __name__ == "__main__":
    main()
