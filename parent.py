local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

# in the same file, add the following below the User class
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())

print(__name__)

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
  
# Now try running the file directly. You should see the file is being executed directly printed in the console.
# Execute child.py You should see The file is being executed because it is imported by another file. The file is called: parent
# How is this useful? We can use this conditional to prevent blocks of code from executing unless the file is being run directly. 
# Why would we want to do this? Consider a situation where one class depends on another, as in the Users with Bank Accounts assignment. 
# In our product document we might create a lot of test code to make sure we can create new products and execute methods. 
# When we import products to the store file as a module, we don’t want to see all of those tests run every time we execute the 
# store file, so inside of our product document, we might have something like below:

