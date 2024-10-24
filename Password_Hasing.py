import bcrypt

def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(hashed_password, user_password):
    # Check the hashed password against the provided password
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

if __name__ == "__main__":
   
    password = "supersecretpassword"
    hashed = hash_password(password)
    
    print(f"Original password: {password}")
    print(f"Hashed password: {hashed}")

    # Check the password
    result = check_password(hashed, "supersecretpassword")
    print(f"Password match: {result}")

    # Check with a wrong password
    result = check_password(hashed, "wrongpassword")
    print(f"Password match: {result}")
