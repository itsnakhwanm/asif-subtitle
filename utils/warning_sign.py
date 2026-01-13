def warning_sign(message):
    confirm = input(f"{message} [Y/n] ")
    if confirm in ["Y","y"]:
        return True
    else:
        return False
