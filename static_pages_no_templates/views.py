
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

nav = """
    <nav>
        <a href='/'>Home</a> |
        <a href='/contact/'>Contact</a> |
        <a href='/about/'>About Us</a> |
        <a href='/signin/'>SignIn</a>
    </nav>
"""
name = "Kavya"
age = 29
gains = 234.5634224
country = "India"

home_body = f"""
    <ol>
        <li>Name: {name}</li>
        <li>Age: {age}</li>
        <li>Gains: {gains:.2f}</li>
        <li>Country: {country}</li>
    </ol>
    
"""



def home(request):
    content= """
            <h1>Welcome to my Django Page</h1>
            <h2>Visit around</h2>
            <p>Enjoy the content of Page1</p>
    """
    
    return HttpResponse(nav + content + home_body)

def contact(request):
    
    email = "kavya@gmail.com"
    phone = 4377997765
    is_active = True

    my_list = ["call", 123, 4.5, False, "email", 99]

    my_dict = {
        "city": "Calgary",
        "code": "AB",
        "support": True,
        "rating": 4.3,
        "available": "24/7"
    }

    body = f"""
    <h1>Contact Us</h1>
    <h2>Get in Touch</h2>
    <p>You can contact us using below details</p>

    <ol>
        <li>Email: {email}</li>
        <li>Phone: {phone}</li>
        <li>Active: {is_active}</li>
    </ol>

   
    """

    return HttpResponse(nav + body)
    

def about(request):
    company = "MyApp"
    employees = 100
    is_global = False

    my_list = ["team", 5, 3.3, True, "growth", 80]

    my_dict = {
        "founded": 2020,
        "ceo": "John",
        "public": False,
        "revenue": 5.5,
        "country": "Canada"
    }

    body = f"""
    <h1>About Us</h1>
    <h2>Company Info</h2>
    <p>Learn more about our company</p>

    <ol>
        <li>Company: {company}</li>
        <li>Employees: {employees}</li>
        <li>Global: {is_global}</li>
    </ol>
 
    <h2>Highlights</h2>
    <ul>
        {''.join(f"<li>{i}</li>" for i in my_list)}
    </ul>

    <h2>Company Data</h2>
    <ul>
        {''.join(f"<li>{k}: {v}</li>" for k,v in my_dict.items())}
    </ul>
   
    """

    return HttpResponse(nav + body)

def signin(request):
    username = "Kavya"
    attempts = 3
    logged_in = False

    my_list = ["login", 2, 4.4, False, "user", 60]

    my_dict = {
        "page": "signin",
        "secure": True,
        "users": 500,
        "version": 1.0,
        "status": "active"
    }

    body = f"""
    <h1>Sign In</h1>
    <h2>User Login</h2>
    <p>Please enter your details</p>

    <ol>
        <li>Username: {username}</li>
        <li>Attempts: {attempts}</li>
        <li>Logged In: {logged_in}</li>
    </ol>


    """

    return HttpResponse(nav + body)