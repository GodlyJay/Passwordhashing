import bcrypt
import schedule 
import time

def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(hashed_password, user_password):
    # Check the hashed password against the provided password
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def update_hash(password):
    # Update the hashed password every 1 minutes
    global hashed
    hashed = hash_password(password)
    print(f"Hashed password updated: {hashed}")

if __name__ == "__main__":
    password = "supersecretpassword"
    hashed = hash_password(password)
    
    print(f"Original password: {password}")
    print(f"Hashed password: {hashed}")

    # Check the password
    result = check_password(hashed, "supersecretpassword")
    print(f"Password match: {result}")

    # Schedule the hash update every 1 minutes
    schedule.every(1).minutes.do(update_hash, password)

    while True:
        schedule.run_pending()
        time.sleep(1)

