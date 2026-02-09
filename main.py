from pyscript import display, document

def handle_signup(event):
    user_input = document.querySelector("#username")
    pass_input = document.querySelector("#password")
    message_div = document.querySelector("#message")

    if not user_input.value or not pass_input.value:
        message_div.innerText = "Please fill in all fields."
    
    elif len(pass_input.value) < 3:
        message_div.innerText = "Password is too short."
    
    else:
        message_div.innerText = "Account created. You may now log in using your credentials."