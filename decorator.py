
def admin_decorator(func):
    def wrapper(*args,**kwargs):
        user='admin'
        if user=='admin':
            func(*args,**kwargs)
        else:
            login_page()
    return wrapper
def login_decorator(func):
    def wrapper(*args, **kwargs):
        login_status=True
        if login_status:
            func(*args, **kwargs)
        else:
            login_page()
    return wrapper

@login_decorator
@admin_decorator
def admin_view():
    print("Welcome to admin page")

@login_decorator
def home_view():
    print("welcome to home page")

def login_page():
    print("Welcome to login page")


admin_view()