from src import User

if __name__ == '__main__':
    new_user = User('Ted')
    print(new_user.get_greeting_string())