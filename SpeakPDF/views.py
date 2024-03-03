'''views.py'''
import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from run import text_to_speech, extract_content, translate_to_hindi
from SpeakPDF.models import AudioConvert, LanguageConvert, Feedback

def homeView(request):
    return render(request, 'home.html', {'user': checkUser(request)})

def audioConvertView(request):
    if request.method == 'POST':
        file = request.FILES["file"]

        if file.name.split('.')[-1] == 'pdf':
            audio = text_to_speech(extract_content(file), file.name, 1)
            audio_path = os.path.join('/static','converted_files',os.path.basename(audio))

            audioObj = AudioConvert.objects.create(
                user = request.user,
                file = file,
                audio_file = audio
            )
            audioObj.save()

            return render(request, 'home.html', {'audio': audio_path, 'file':os.path.basename(audio), 'Asuccess': True, 'user': checkUser(request)})
        else:
            messages.error(request, 'The file must be of type .pdf')
            return render(request, 'home.html', {'Asuccess': False, 'user': checkUser(request)})
    
    return redirect('home')

def languageConvertView(request):
    if request.method == 'POST':
        file = request.FILES["file"]

        if file.name.split('.')[-1] == 'pdf':
            audio = text_to_speech(translate_to_hindi(extract_content(file)), file.name, 2)
            audio_path = os.path.join('/static','hindi_files',os.path.basename(audio))

            langObj = LanguageConvert.objects.create(
                user = request.user,
                file = file,
                audio_file = audio
            )
            langObj.save()

            return render(request, 'home.html', {'langAudio': audio_path, 'langFile':os.path.basename(audio), 'Lsuccess': True, 'user': checkUser(request)})
        else:
            messages.error(request, 'The file must be of type .pdf')
            return render(request, 'home.html', {'Lsuccess': False, 'user': checkUser(request)})
    
    return redirect('home')

def feedbackView(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        try:
            feedback = Feedback.objects.create(
                user = request.user,
                title = title,
                description = desc
            )
            feedback.save()
            messages.success(request, 'Feedback given successfully.')

        except Exception:
            messages.error(request, 'There was an error while giving feedback. Kindly fill the feedback form again.')

    return render(request, 'feedback.html', {'user':checkUser(request)})

def contactView(request):
    return render(request, 'contact.html', {'user':checkUser(request)})

def loginView(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username=email).exists():
            messages.error(request, "No such user exists.")
            return redirect("login")
        
        user = authenticate(username=email,password=password)

        if user is None:
            messages.error(request, "Wrong credentials.")
            return redirect("login")
        else:
            login(request,user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')

    return render(request, 'login.html')

@login_required
def logoutView(request):
    logout(request)
    return redirect('home')


def registerView(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=email)

        if user.exists():
            messages.error(request, 'User exists.')
            return redirect("register")

        user = User.objects.create(first_name=fname, last_name=lname, username=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'Registration successful.')

    return render(request, 'register.html')


def checkUser(request):
    try:
        user = request.user.first_name
    except Exception:
        user = ''
    return user
