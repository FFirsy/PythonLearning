def login(password_attempt,real_password):
    if not password_attempt:
        return "Empty input"
    elif password_attempt == real_password:
        return "Login successful"
    else:
        return "Wrong password"
