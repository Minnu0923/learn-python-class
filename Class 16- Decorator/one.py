def login_required(func):
    def inner(name,status):
        if status == False:
            print("Login Required")
        else:
            func(name,status) 
    return inner



def homepage(name,login_status):
    print("Home Page")

def about(name,login_status):
    print("About Page")

@login_required
def profile(name,login_status):
    print("Profile Page")

@login_required
def history_page(name,login_status):
    print("History Page")


homepage("Rahul", True)
about("Rahul", False)
profile("Rahul", False)
history_page("Rahul", False)