class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, key, value):
        if self.head == None:
            self.head = Node(key, value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(key, value)

    def input(self):
        current = input("What kind of dish do you like? Chinese, Indian, Italian, Mexican or Russian: ").lower()
        current_node = self.head
        found_categories = set()
        while current_node:
            if current in current_node.key.lower():
                found_categories.add(current_node.key)
            current_node = current_node.next
        
        if len(found_categories) == 1:
            chosen_category = found_categories.pop()
            print("Here is the information for the", chosen_category, "cuisine:")
            self.print_category_info(chosen_category)
        elif len(found_categories) > 1:
            print("Multiple categories found for your input. Please choose one:")
            for i, category in enumerate(found_categories):
                print(f"{i+1}. {category}")
            choice = input("Enter the number corresponding to your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(found_categories):
                chosen_category = list(found_categories)[int(choice) - 1]
                print("Here is the information for the", chosen_category, "cuisine:")
                self.print_category_info(chosen_category)
            else:
                print("Invalid choice. Please enter a number between 1 and", len(found_categories))
        else:
            print("Sorry, we don't have information about that cuisine.")

    def print_category_info(self, category):
        current_node = self.head
        while current_node:
            if current_node.key.lower() == category.lower():
                print(current_node.value)
            current_node = current_node.next

linked_list = LinkedList()
linked_list.append("Chinese", "Type: Dumplings\nOriginal: Guotie\nRating:4.7")
linked_list.append("Chinese", "Type: Duck Dish\nOriginal: Peking duck\nRating:4.5")
linked_list.append("Chinese", "Type: Noodle Dish\nOriginal: Dan Dan noodles\nRating:4.0")
linked_list.append("Chinese", "Type: Pancake\nOriginal: Jianbing\nRating:4.5")
linked_list.append("Chinese", "Type: Noodle Dish\nOriginal: Biang Biang noodles\nRating:4.2")
linked_list.append("Chinese", "Type: Fried chicken dish\nOriginal: Crispy fried chicken\nRating:4.9")
linked_list.append("Indian", "Type: Bread\nOriginal: Chapati\nRating:3.5")
linked_list.append("Indian", "Type: Street Food\nOriginal: Samosas\nRating:4.1")
linked_list.append("Indian", "Type: Bread\nOriginal: Naan\nRating:4.7")
linked_list.append("Indian", "Type: Dishes\nOriginal: Tandoori\nRating:3.7")
linked_list.append("Indian", "Type: Appetizers\nOriginal: Pakora\nRating:4.9")
linked_list.append("Indian", "Type: Appetizers\nOriginal: Sambar\nRating:5.0")
linked_list.append("Italian", "Type: Pasta\nOriginal: Carbonara\nRating:4.3")
linked_list.append("Italian", "Type: Pizza\nOriginal: Diavola\nRating:4.1")
linked_list.append("Italian", "Type: Fried\nOriginal: Arancini\nRating:4.7")
linked_list.append("Italian", "Type: Pizza\nOriginal: Napoletana\nRating:4.9")
linked_list.append("Italian", "Type: Fried\nOriginal: Panzerotto\nRating:3.5")
linked_list.append("Italian", "Type: Pasta\nOriginal: Pesto\nRating:3.0")
linked_list.append("Mexican", "Type: Soup\nOriginal: Pozole\nRating:4.1")
linked_list.append("Mexican", "Type: Taco\nOriginal: Chicken Taco Torta\nRating:4.9")
linked_list.append("Mexican", "Type: Street food\nOriginal: Elote\nRating:4.9")
linked_list.append("Mexican", "Type: Taco\nOriginal: Grilled Chicken Street Tacos\nRating:4.3")
linked_list.append("Mexican", "Type: Street food\nOriginal: Chalupas\nRating:4.4")
linked_list.append("Russian", "Type: Crepes\nOriginal: Bliny\nRating:4.3")
linked_list.append("Russian", "Type: Soup\nOriginal: Borscht\nRating:4.1")
linked_list.append("Russian", "Type: Soup\nOriginal: Okroshka\nRating:4.6")
linked_list.append("Russian", "Type: Salad\nOriginal: Salad Olivier\nRating:4.7")
linked_list.append("Russian", "Type: Soup\nOriginal: Shchi\nRating:3.3")

linked_list.input()
