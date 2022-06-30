import inspect


def print_name_and_value_func(func):
    arg_values = str(inspect.signature(func)).replace("(", "").replace(")", "")
    func_names = func.__name__.capitalize().replace("_", " "), arg_values

    if len(arg_values) > 0:
        print(*func_names, sep=": ")
    else:
        print(*func_names)


def open_browser(browser_name):
    pass

def go_to_company_name_homepage(page_url):
    pass

def find_registration_button_on_login_page(page_url, button_text):
    pass


given_functions = open_browser, go_to_company_name_homepage, find_registration_button_on_login_page

for i in given_functions:
    print_name_and_value_func(i)
