#Import datetime
import datetime

# Welcome message!
print("Welcome to the Error Logger!")

# Function to display the menu
def display_menu():
  print("\nPlease choose an option:") # \n = newLine
  print("1. Log a new error message.")
  print("2. View all error messages.")
  print("3. Quit")
  
#Function to log a new error message with the acctual time
def log_new_error():
  entry = input("Please enter the new error message: ")
  date_time = datetime.datetime.now().strftime("%S:%M:%H-%d.%m.%Y.")
  with open("error.txt", "a") as file:
    file.write(f"{date_time} - {entry}\n")
  print("New error was logged successfully!")
  
#Function to view all error messages with the time logged  
def view_errors():
  try:
    with open("error.txt", "r") as file:
      entries = file.readlines()
      if entries:
        print("\nLogged error messages: ")
        for entry in entries:
          print(entry.strip())
      else:
        print("No logged error was found.")
  except FileNotFoundError:
    print("No error messages were found!")

#The main function of the program - while True
def main():
  while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
      log_new_error()
    elif choice == "2":
      view_errors()
    elif choice == "3":
      print("Thank you for using the Error Logger. Goodbye!")
      break
    else:
      print("You have chosen an invalid option. Please try again.")

# Conditional block to ensure that the main() function is executed only if the script is run directly.
if __name__ == "__main__":
  main()
