from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = Student.objects.filter(email=email, password=password).first()
        
        if user:
            request.session['user'] = user.id
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')


def dashboard(request):
    if not request.session.get('user'):
        return redirect('login')
    
    data = Student.objects.all()
    return render(request, 'dashboard.html', {'data': data})

def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form})


def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('dashboard')
def logout_view(request):
    request.session.flush()
    return redirect('login')