import requests
sheet_url = "https://api.sheety.co/19c8fef61987ddff56f584e28940f963/useresPartOfFlightProject/users"


def new_user():
    first_name = input("First name: \n")
    last_name = input("Last name: \n")
    email = input("Email: ")
    verficatin = input("please enter your email address again\n")
    if verficatin == email:
        new_data = {
            "user": {
                "firstname": first_name,
                "lastname": last_name,
                "email": email

            }
        }
        return new_data
    else:
        print("Wrong email address")
        return new_user()




new_user = new_user()
response = requests.post(url=sheet_url, json=new_user)
print(response.text)
