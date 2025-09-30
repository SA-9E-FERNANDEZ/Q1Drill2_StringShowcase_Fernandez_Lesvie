from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    # Get input values
    name = document.querySelector("#name").value.strip()
    age = document.querySelector("#age").value.strip()
    school = document.querySelector("#school").value.strip()

    # Clear previous output
    document.querySelector("#output").innerText = ""

    # Build message
    message = f"""My name is {name}.
I am {age} years old.
I study at {school}.
"""

    display(message, target="output")
