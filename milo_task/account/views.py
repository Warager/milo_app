import csv
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from milo_task.account.forms import UserForm
from milo_task.account.models import User
from milo_task.account.utils import get_eligible, get_bizzfuzz


def listing(request):
    users = User.objects.all()
    data = {
        'users': users
    }
    return render(request, "account/listing.html", data)


def display(request, user_id):
    user = User.objects.get(id=user_id)
    data = {
        'user': user
    }
    return render(request, "account/display.html", data)


def edit(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse(display, args=(user.id, )))
    else:
        form = UserForm(instance=user)
    data = {
        'user': user,
        'form': form
    }
    return render(request, "account/edit.html", data)


def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse(display, args=(user.id, )))
    else:
        form = UserForm()
    data = {
        'form': form
    }
    return render(request, "account/create.html", data)


def delete(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect(reverse(listing))
    return render(request, "account/delete.html")


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=users.csv'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Eligible', 'Random',
                     'BizzFuzz'])
    for user in User.objects.all():
        writer.writerow([
            user.username,
            user.birthday.strftime('%Y-%m-%d'),
            get_eligible(user.birthday),
            user.random,
            get_bizzfuzz(user.random)
        ])
    return response