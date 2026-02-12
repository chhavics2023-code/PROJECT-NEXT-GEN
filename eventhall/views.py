
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django .contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'eventhall/home.html')
def hall_details(request):
    return render(request, 'eventhall/hall_details.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')   # login ke baad home page
        else:
            return render(request, 'eventhall/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'eventhall/login.html')
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'eventhall/signup.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'eventhall/signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()

        return redirect('login')

    return render(request, 'eventhall/signup.html')
def halls(request):
    halls = Hall.objects.all()
    return render(request, 'eventhall/halls.html', {'halls': halls})
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def book_hall(request, id):
    hall = Hall.objects.get(id=id)
    if request.method == "POST":
        Booking.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            event_date=request.POST.get('date'),
            event_type=request.POST.get('event_type'),
            guests=request.POST.get('guests'),
            message=request.POST.get('message'),
        )
        return render(request, 'eventhall/book_hall.html', {'hall': hall,
            'message': 'Booking submitted successfully! Status: Pending'
        })

    return render(request, 'eventhall/book_hall.html',{
'hall': hall,})
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-event_date')
    return render(request, 'eventhall/my_bookings.html', {
        'bookings': bookings
    })
from django.contrib.admin.views.decorators import staff_member_required
from .models import Booking, Hall

@staff_member_required
def admin_dashboard(request):
    total_halls = Hall.objects.count()
    total_bookings = Booking.objects.count()
    pending_count = Booking.objects.filter(status='Pending').count()
    approved_count = Booking.objects.filter(status='Approved').count()

    recent_bookings = Booking.objects.order_by('-id')[:5]

    return render(request, 'eventhall/admin_dashboard.html', {
        'total_halls': total_halls,
        'total_bookings': total_bookings,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'recent_bookings': recent_bookings,
    })
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Booking

@staff_member_required
def manage_bookings(request):
    bookings = Booking.objects.all().order_by('-id')
    return render(request, 'eventhall/manage_bookings.html', {
        'bookings': bookings
    })


@staff_member_required
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'Approved'
    booking.save()
    return redirect('manage_bookings')


@staff_member_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'Rejected'
    booking.save()
    return redirect('manage_bookings')
def about(request):
    return render(request, 'eventhall/about.html')
def contact(request):
    if request.method == "POST":
        # form data access (optional)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # for now just reload page
        return render(request, 'eventhall/contact.html', {'success': True})

    return render(request, 'eventhall/contact.html')
