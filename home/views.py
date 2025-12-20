from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import UserProfile
from .forms import ProfileForm

from .models import Internship, UserProfile
from .recommendation import recommend_internships
from .models import SavedInternship
from .models import AppliedInternship



@login_required
def recommendations_view(request):
    profile = UserProfile.objects.get(user=request.user)
    internships = Internship.objects.all()

    recommended = recommend_internships(profile.skills, internships)

    return render(
        request,
        'home/recommendations.html',
        {'internships': recommended}
    )


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()

    return render(request, 'home/signup.html', {'form': form})
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()

    return render(request, 'home/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'home/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return redirect('login')



@login_required
def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        skills_list = request.POST.getlist('skills')
        profile.skills = ", ".join(skills_list)
        profile.preferred_role = request.POST.get('preferred_role')
        profile.location = request.POST.get('location')
        profile.save()

        return redirect('recommendations')

    return render(request, 'home/profile.html')

@login_required
def save_internship_view(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)

    SavedInternship.objects.get_or_create(
        user=request.user,
        internship=internship
    )

    return redirect('recommendations')

@login_required
def saved_internships_view(request):
    saved = SavedInternship.objects.filter(user=request.user)

    return render(
        request,
        'home/saved.html',
        {'saved': saved}
    )


@login_required
def apply_internship_view(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)

    AppliedInternship.objects.get_or_create(
        user=request.user,
        internship=internship
    )

    return redirect('recommendations')

@login_required
def applied_internships_view(request):
    applied = AppliedInternship.objects.filter(user=request.user)

    return render(
        request,
        'home/applied.html',
        {'applied': applied}
    )
