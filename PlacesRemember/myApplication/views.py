from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from PlacesRemember.forms import MemoryForm



def welcome(request):
    memories = []  # Replace with your actual memory data
    context = {'memories': memories}
    return render(request, 'welcome.html', context)


@login_required
def home(request):
    user = request.user
    profile_picture = None

    # Retrieve the profile picture URL based on the authentication provider
    if user.is_authenticated:
        if user.socialaccount_set.filter(provider='google').exists():
            google_provider = user.socialaccount_set.get(provider='google')
            profile_picture = google_provider.extra_data.get('picture', None)
        elif user.socialaccount_set.filter(provider='vk').exists():
            vk_provider = user.socialaccount_set.get(provider='vk')
            profile_picture = vk_provider.extra_data.get('photo_max_orig', None)


    context = {
        'user': user,
        'profile_picture': profile_picture,
    }
    return render(request, 'home.html', context)

@login_required
def add_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            # Save the form data without committing to the database
            memory = form.save(commit=False)

            # Retrieve the latitude and longitude from the form's cleaned data
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            # Set the latitude and longitude values for the memory object
            memory.latitude = latitude
            memory.longitude = longitude

            # Save the memory object to the database
            memory.save()

            # Redirect to the home page or a success page
            return redirect('home')
    else:
        form = MemoryForm()
    return render(request, 'add_memory.html', {'form': form})

# Create your views here.
