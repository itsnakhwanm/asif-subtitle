def warning_sign(message):
    confirm = input(f"{message} [Y/n] ")
    if confirm in ["Y","y"]:
        return True
    else:
        return False

def multiple_confirmation(messages):
    for i in messages:
        confirm = input(f"{i} [Y/n] ")
        if confirm in ["Y","y"]:
            continue
        else:
            break
    return True
