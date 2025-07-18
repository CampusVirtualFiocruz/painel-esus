def create_user(user, password):
    return {
        "login": user,
        "password": password,
        "data": {
            "username": user,
            "cns": "0000000000",
            "uf": "",
            "municipio": "",
            "profiles": ["admin"],
        },
    }


users = [
    create_user(user[0], user[1])
    for user in zip(
        ["nste", "ndar", "bent", "ify"], 
        ["jJN#529", "vrK853^", "8rB5*66", "2A+L6n0"]
    )
]
