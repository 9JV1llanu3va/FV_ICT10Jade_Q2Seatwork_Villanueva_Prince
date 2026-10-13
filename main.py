from pyscript import document

def checkName(e):
    club_members = ["Frances Miller", "Prince Villanueva", "Neo Macaraig", "Hans Arada", "Isaias Berdin", "Georgina Banal", "Jeremiah Velasco", "Darvine Mitchell"]

    club_members_lower = [member.lower() for member in club_members]

    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()
    full_name = f"{first_name} {last_name}"

    full_name_lower = full_name.lower()

    is_member = full_name_lower in club_members_lower

    messages = (
        f"Sorry! {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the Math club."
    )

    document.getElementById("output1").innerHTML = messages[int(is_member)]