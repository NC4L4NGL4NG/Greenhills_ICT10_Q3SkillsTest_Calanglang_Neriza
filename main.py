from pyscript import display, document

def handle_signup(event):
    user_input = document.querySelector("#username")
    pass_input = document.querySelector("#password")
    message = document.querySelector("#message")

    if not user_input.value or not pass_input.value:
        message.innerText = "Please fill in all fields."
    
    elif len(pass_input.value) < 3:
        message.innerText = "Password is too short."
    
    else:

        message.innerText = "Account created. You may now log in using your credentials."
