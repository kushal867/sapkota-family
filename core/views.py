from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Invitation, Birthday, Gallery
from .forms import InvitationForm, BirthdayForm, GalleryForm


# Home
def home(request):
    return render(request, 'home.html', {
        'invitations_count': Invitation.objects.count(),
        'birthdays_count': Birthday.objects.count(),
        'gallery_count': Gallery.objects.count(),
    })


# ---------- GENERIC HANDLER ----------
def handle_form(request, form_class, template, instance=None, success_msg="", redirect_url=""):
    form = form_class(request.POST or None, request.FILES or None, instance=instance)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, success_msg)
        return redirect(redirect_url)

    return render(request, template, {"form": form})


# ---------- INVITATION ----------
def invitation_list(request):
    return render(request, 'invitation_list.html', {
        'invitations': Invitation.objects.order_by('-created_at')
    })


def invitation_detail(request, pk):
    return render(request, 'invitation_detail.html', {
        'invitation': get_object_or_404(Invitation, pk=pk)
    })


@login_required
def invitation_create(request):
    return handle_form(
        request,
        InvitationForm,
        'invitation_form.html',
        success_msg="Invitation created successfully!",
        redirect_url='invitation_list'
    )


@login_required
def invitation_update(request, pk):
    invitation = get_object_or_404(Invitation, pk=pk)
    return handle_form(
        request,
        InvitationForm,
        'invitation_form.html',
        instance=invitation,
        success_msg="Invitation updated successfully!",
        redirect_url='invitation_list'
    )


@login_required
@require_POST
def invitation_delete(request, pk):
    invitation = get_object_or_404(Invitation, pk=pk)
    invitation.delete()
    messages.success(request, "Invitation deleted successfully!")
    return redirect('invitation_list')


# ---------- BIRTHDAY ----------
def birthday_list(request):
    return render(request, 'birthday_list.html', {
        'birthdays': Birthday.objects.order_by('name')
    })


def birthday_detail(request, pk):
    return render(request, 'birthday_detail.html', {
        'birthday': get_object_or_404(Birthday, pk=pk)
    })


@login_required
def birthday_create(request):
    return handle_form(
        request,
        BirthdayForm,
        'birthday_form.html',
        success_msg="Birthday added successfully!",
        redirect_url='birthday_list'
    )


@login_required
def birthday_update(request, pk):
    birthday = get_object_or_404(Birthday, pk=pk)
    return handle_form(
        request,
        BirthdayForm,
        'birthday_form.html',
        instance=birthday,
        success_msg="Birthday updated successfully!",
        redirect_url='birthday_list'
    )


@login_required
@require_POST
def birthday_delete(request, pk):
    birthday = get_object_or_404(Birthday, pk=pk)
    birthday.delete()
    messages.success(request, "Birthday deleted successfully!")
    return redirect('birthday_list')


# ---------- GALLERY ----------
def gallery_list(request):
    return render(request, 'gallery_list.html', {
        'gallery': Gallery.objects.order_by('-uploaded_at')
    })


def gallery_detail(request, pk):
    return render(request, 'gallery_detail.html', {
        'image': get_object_or_404(Gallery, pk=pk)
    })


@login_required
def gallery_create(request):
    return handle_form(
        request,
        GalleryForm,
        'gallery_form.html',
        success_msg="Image uploaded successfully!",
        redirect_url='gallery_list'
    )


@login_required
def gallery_update(request, pk):
    image = get_object_or_404(Gallery, pk=pk)
    return handle_form(
        request,
        GalleryForm,
        'gallery_form.html',
        instance=image,
        success_msg="Image updated successfully!",
        redirect_url='gallery_list'
    )


@login_required
@require_POST
def gallery_delete(request, pk):
    image = get_object_or_404(Gallery, pk=pk)
    image.delete()
    messages.success(request, "Image deleted successfully!")
    return redirect('gallery_list')
