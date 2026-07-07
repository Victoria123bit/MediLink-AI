import bcrypt


# ==========================
# Hash Password
# ==========================

def hash_password(password):

    password = password.encode("utf-8")

    hashed = bcrypt.hashpw(
        password,
        bcrypt.gensalt()
    )

    return hashed.decode("utf-8")


# ==========================
# Verify Password
# ==========================

def verify_password(
    password,
    hashed_password
):

    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )