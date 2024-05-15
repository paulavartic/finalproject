import json
from utils import organized_operations, pop_up_msg

def main():
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    items = organized_operations(data)

    for i in range(5):
        print (f"{pop_up_msg(items[i])} \n")





if __name__ == "__main__":
    main()