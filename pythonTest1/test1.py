# Task 1.
# Write a Python program to create a list containing the following
# numbers: 10, 20, 30, 40, 50.
Task1_numbers = [10, 20, 30, 40, 50]
def sub_task1():
    print(Task1_numbers) # Print the list.
def sub_task2():
    print(Task1_numbers[0]) #Print the first element of the list.
def sub_task3():
    print(Task1_numbers[2]) #Print the third element of the list.
def sub_task4():
    Task1_numbers[1]=25 #Change the second element of the list to 25 and print the updated list.
    print(Task1_numbers)
def sub_task5():
    Task1_numbers.insert(1, 15) #Insert the number 15 at the second position in the list
    print(Task1_numbers)
def sub_task6():
    pass #Creati o functie empty, care sa nu provoace erori la rulare.

Task2_matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
def sub_task7():
    print(Task2_matrix[1][1]) #Print the second element of the second list.

def sub_task8(): #Print all the elements from the first, third and last list.
    print(Task2_matrix[0])  # First
    print(Task2_matrix[2])  # Third
    print(Task2_matrix[-1]) # Last

Task3_dictionary = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
def sub_task9():
    print(Task3_dictionary) #Print the dictionary
def sub_task10():
    print(Task3_dictionary["name"]) #Print the value associated with the key "name".
def sub_task11():
    print(Task3_dictionary["age"]) #Print the value associated with the key "age".
def sub_task12():
    print(Task3_dictionary.get("city")) #Print the value of the "city" key using the get() method.

Task4_fruits=["apple", "banana", "cherry", "apple", "banana", "apple"]


if __name__ == "__main__":
    print("Welcome to the first test of the course!")
