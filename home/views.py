from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from home.models import Admin, customer, booking, Event
# Create your views here.
def home(request):
    return render(request,'homepage.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()  # Get and strip whitespace
        password = request.POST.get('password')
        role = request.POST.get('role')
        print(email, password, role)
        if role=='Patron':
            try:
                # Fetch the admin user by email
                user = customer.objects.get(email=email)

                # Check the password using check_password
                if check_password(password, user.password):
                    print('Customer login successful')
                    # You might want to create a session or perform some actions here
                    return redirect('eventlist')  # Redirect to admin dashboard
                else:
                    print('Password incorrect for customer!')
                    return redirect('login')  # Redirect back to admin login

            except customer.DoesNotExist:
                print('Customer does not exist!')
                return redirect('login')  # Redirect back to admin login
        if role=='Admin':
            try:
                # Fetch the admin user by email
                user = Admin.objects.get(email=email)

                # Check the password using check_password
                if password==user.password:
                    print('Admin login successful')
                    # You might want to create a session or perform some actions here
                    return redirect('eventlistAdmin')  # Redirect to admin dashboard
                else:
                    print('Password incorrect for admin!')
                    return redirect('login')  # Redirect back to admin login

            except customer.DoesNotExist:
                print('Admin does not exist!')
                return redirect('login')  # Redirect back to admin login

    return render(request, 'login.html')  # Render the login page if GET request

                

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the customer already exists
        isthere = customer.objects.filter(email=email)
        if isthere.exists():
            print('Customer already exists!')
            return redirect('login')  # Make sure to return the redirect
        else:
            # Hash the password before saving
            hashed_password = make_password(password)
            c = customer(name=f"{firstname} {lastname}", email=email, password=hashed_password)
            c.save()
            return redirect('home')  # Make sure to return the redirect

    return render(request, 'register.html')

def eventlist(request):
    events = Event.objects.all().values()
    event_list=list(events)
    context={'events':event_list}
    return render(request,'eventlist.html', context=context)

def eventcreate(request):
    if request.method=='POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        chef = request.POST.get('chef')
        details = request.POST.get('details')
        theme = request.POST.get('theme')
        gprice = request.POST.get('gprice')
        VIPrice = request.POST.get('VIPrice')
        seats = request.POST.get('seats')
        venue = request.POST.get('venue')
        try:
            new_event = Event(name=name, date=date, time=time, chef=chef, details=details, theme=theme, gprice=gprice, VIPrice=VIPrice, seats=seats, venue=venue )
            new_event.save()
            return redirect('home')
        except Exception as e:
            print("Try Again" + str(e))
    return render(request, 'eventcreate.html')
        

def dashindex(request):
    return render(request, 'dashindex.html')


def editevent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        chef = request.POST.get('chef')
        details = request.POST.get('details')
        theme = request.POST.get('theme')
        gprice = request.POST.get('gprice')
        VIPrice = request.POST.get('VIPrice')
        seats = request.POST.get('seats')
        venue = request.POST.get('venue')

        if not name or not date or not time or not venue:
            return render(request, 'editevent.html', {
                'error': 'All fields are required, especially name, date, time, and venue.'
            })

        # Check if the event with the given name exists
        exists = Event.objects.filter(name=name).first()  # Get the first matching event or None
        
        if exists is None:
            # If no event exists, create a new event
            new_event = Event(
                name=name,
                date=date,
                time=time,
                chef=chef,
                details=details,
                theme=theme,
                gprice=gprice,
                VIPrice=VIPrice,
                seats=seats,
                venue=venue
            )
            new_event.save()
            print('New event added')
        else:
            # If the event exists, update its fields
            exists.date = date
            exists.time = time
            exists.chef = chef
            exists.details = details
            exists.theme = theme
            exists.gprice = gprice
            exists.VIPrice = VIPrice
            exists.seats = seats
            exists.venue = venue
            exists.save()
            print('Event has been edited')

        return redirect('home')  # Redirect to the home page

    return render(request, 'editevent.html')

def eventlistAdmin(request):
    return render(request, 'eventlistAdmin.html')

def Bookindex(request):
    return render(request, 'Bookindex.html')

def eventdelete(request):
    return render(request, 'eventdelete.html')

def faqindex(request):
    return render(request, 'faqindex.html')

def feedback(request):
    return render(request, 'feedback.html')

def QR1index(request):
    return render(request, 'QR1index.html')

def QR2index(request):
    return render(request, 'QR2index.html')

def QR3index(request):
    return render(request, 'QR3index.html')