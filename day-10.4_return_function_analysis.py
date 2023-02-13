def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return """you didn't provide any ,\033[31m inputs"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
print(format_name(input("what is your f_name: ") ,input("what is your l_name: ")))