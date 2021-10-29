def edit_message(message):
    if "False" in message:
        message = message.replace("False", "false")
    if "True" in message:
        message = message.replace("True", "true")
    if "None" in message:
        message = message.replace("None", "null")
    return message
