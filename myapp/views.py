from django.shortcuts import render, get_object_or_404, redirect
from .models import Student

# Read - Display all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Create
def student_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        year_level = request.POST['year_level']
        program_course = request.POST['program_course']
        email = request.POST['email']
        Student.objects.create(
            name=name,
            address=address,
            year_level=year_level,
            program_course=program_course,
            email=email,
        )
        return redirect('student_list')
    return render(request, 'student_form.html')

# Update
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.address = request.POST['address']
        student.year_level = request.POST['year_level']
        student.program_course = request.POST['program_course']
        student.email = request.POST['email']
        student.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'student': student})

# Delete
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})
