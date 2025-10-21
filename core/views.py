from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Invitation, Birthday, Gallery

# Home View
def home(request):
    """Home page view"""
    context = {
        'invitations_count': Invitation.objects.count(),
        'birthdays_count': Birthday.objects.count(),
        'gallery_count': Gallery.objects.count(),
    }
    return render(request, 'home.html', context)

# Invitation Views
def invitation_list(request):
    """Invitation list view"""
    invitations = Invitation.objects.all().order_by('-created_at')
    return render(request, 'invitation_list.html', {'invitations': invitations})

def invitation_detail(request, pk):
    """Invitation detail view"""
    invitation = get_object_or_404(Invitation, pk=pk)
    return render(request, 'invitation_detail.html', {'invitation': invitation})

def invitation_create(request):
    """Create new invitation"""
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        location = request.POST.get('location')
        description = request.POST.get('description')
        
        invitation = Invitation(
            title=title,
            date=date,
            location=location,
            description=description
        )
        invitation.save()
        messages.success(request, 'Invitation created successfully!')
        return redirect('invitation_list')
    
    return render(request, 'invitation_form.html')

def invitation_update(request, pk):
    """Update existing invitation"""
    invitation = get_object_or_404(Invitation, pk=pk)
    
    if request.method == 'POST':
        invitation.title = request.POST.get('title')
        invitation.date = request.POST.get('date')
        invitation.location = request.POST.get('location')
        invitation.description = request.POST.get('description')
        invitation.save()
        
        messages.success(request, 'Invitation updated successfully!')
        return redirect('invitation_list')
    
    return render(request, 'invitation_form.html', {'invitation': invitation})

def invitation_delete(request, pk):
    """Delete invitation"""
    invitation = get_object_or_404(Invitation, pk=pk)
    
    if request.method == 'POST':
        invitation.delete()
        messages.success(request, 'Invitation deleted successfully!')
        return redirect('invitation_list')
    
    return render(request, 'invitation_confirm_delete.html', {'invitation': invitation})

# Birthday Views
def birthday_list(request):
    """Birthday list view"""
    birthdays = Birthday.objects.all().order_by('name')
    return render(request, 'birthday_list.html', {'birthdays': birthdays})

def birthday_detail(request, pk):
    """Birthday detail view"""
    birthday = get_object_or_404(Birthday, pk=pk)
    return render(request, 'birthday_detail.html', {'birthday': birthday})

def birthday_create(request):
    """Create new birthday"""
    if request.method == 'POST':
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        message = request.POST.get('message')
        photo = request.FILES.get('photo')
        
        birthday = Birthday(
            name=name,
            date_of_birth=date_of_birth,
            message=message,
            photo=photo
        )
        birthday.save()
        messages.success(request, 'Birthday added successfully!')
        return redirect('birthday_list')
    
    return render(request, 'birthday_form.html')

def birthday_update(request, pk):
    """Update existing birthday"""
    birthday = get_object_or_404(Birthday, pk=pk)
    
    if request.method == 'POST':
        birthday.name = request.POST.get('name')
        birthday.date_of_birth = request.POST.get('date_of_birth')
        birthday.message = request.POST.get('message')
        
        if 'photo' in request.FILES:
            birthday.photo = request.FILES['photo']
        
        birthday.save()
        messages.success(request, 'Birthday updated successfully!')
        return redirect('birthday_list')
    
    return render(request, 'birthday_form.html', {'birthday': birthday})

def birthday_delete(request, pk):
    """Delete birthday"""
    birthday = get_object_or_404(Birthday, pk=pk)
    
    if request.method == 'POST':
        birthday.delete()
        messages.success(request, 'Birthday deleted successfully!')
        return redirect('birthday_list')
    
    return render(request, 'birthday_confirm_delete.html', {'birthday': birthday})

# Gallery Views
def gallery_list(request):
    """Gallery list view"""
    gallery = Gallery.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery_list.html', {'gallery': gallery})

def gallery_detail(request, pk):
    """Gallery detail view"""
    image = get_object_or_404(Gallery, pk=pk)
    return render(request, 'gallery_detail.html', {'image': image})

def gallery_create(request):
    """Create new gallery image"""
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        caption = request.POST.get('caption')
        
        gallery = Gallery(
            title=title,
            image=image,
            caption=caption
        )
        gallery.save()
        messages.success(request, 'Image uploaded successfully!')
        return redirect('gallery_list')
    
    return render(request, 'gallery_form.html')

def gallery_update(request, pk):
    """Update existing gallery image"""
    image = get_object_or_404(Gallery, pk=pk)
    
    if request.method == 'POST':
        image.title = request.POST.get('title')
        image.caption = request.POST.get('caption')
        
        if 'image' in request.FILES:
            image.image = request.FILES['image']
        
        image.save()
        messages.success(request, 'Image updated successfully!')
        return redirect('gallery_list')
    
    return render(request, 'gallery_form.html', {'image': image})

def gallery_delete(request, pk):
    """Delete gallery image"""
    image = get_object_or_404(Gallery, pk=pk)
    
    if request.method == 'POST':
        image.delete()
        messages.success(request, 'Image deleted successfully!')
        return redirect('gallery_list')
    
    return render(request, 'gallery_confirm_delete.html', {'image': image})