#functionw with output
def format_name(f_name,m_name,l_name):
    formated_f_name = f_name.title()
    formated_m_name = m_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_m_name} {formated_l_name}")
format_name("RanJeEt","KUMAR","jha")

#another way by using return function
def format_name(f_name,m_name,l_name):
    formated_f_name = f_name.title()
    formated_m_name = m_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_m_name} {formated_l_name}"
formated_string = format_name("SoHan","lal","VERMA")
print(formated_string)
print(format_name("madan","KUmar","singh"))