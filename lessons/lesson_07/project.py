users = []

def register_user(users, name, age):
    """
    Registers a user to the users list.
    """
    user = {"name": name, "age": age}
    users.append(user)
    print(f"User registered {user}")


def update_user_age(users, name, new_age):
    """
    Updates user's age based on the given name
    """
    for user in users:
        if user["name"] == name:
            user["age"] = new_age
            print(f"User {name}'s age has been updated to {new_age}")
            return
    print(f"No user named {name} is present in the users list.")


def find_user(users, name):
    """
    Finds a user by name and returns the user
    """

    for user in users:
        if user["name"] == name:
            return user 

    return None

def display_all_users(users):
    """
    Displays all information for all users.
    """
    print("Registered users:")
    for id, user in enumerate(users, 1):
        print(f"{id} - Name: {user['name']} Age: {user['age']}")


def main():

    users = []
    register_user(users=users, name="Alice", age=15)
    register_user(users=users, name="Bob", age=20)
    register_user(users=users, name="Dexter", age=15)
    register_user(users=users, name="Emily", age=16)
    print(users)
    display_all_users(users)



main()
