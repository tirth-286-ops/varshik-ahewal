from django import forms
from .models import (
    NonTeachingStaff, TeachingStaff, PhDStudent, Course, ExamResult,
    TeacherInformation, TeacherPublicationInformation, ResearchProjectInformation,
    SpecialNote, Specialpro, Special ,Year, Department
)
# staff/forms.py

from django import forms
from django.contrib.auth.models import User

class UserCreationCustomForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff', 'is_superuser']


class UserEditCustomForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser']

class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = ['year']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['sr_no', 'name']
class NonTeachingStaffForm(forms.ModelForm):
    class Meta:
        model = NonTeachingStaff
        fields = '__all__'

class TeachingStaffForm(forms.ModelForm):
    class Meta:
        model = TeachingStaff
        fields = '__all__'

class PhDStudentForm(forms.ModelForm):
    class Meta:
        model = PhDStudent
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class ExamResultForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = '__all__'

class TeacherInformationForm(forms.ModelForm):
    class Meta:
        model = TeacherInformation
        fields = '__all__'

class TeacherPublicationInformationForm(forms.ModelForm):
    class Meta:
        model = TeacherPublicationInformation
        fields = '__all__'

class ResearchProjectInformationForm(forms.ModelForm):
    class Meta:
        model = ResearchProjectInformation
        fields = '__all__'

class SpecialNoteForm(forms.ModelForm):
    class Meta:
        model = SpecialNote
        fields = '__all__'

class SpecialproForm(forms.ModelForm):
    class Meta:
        model = Specialpro
        fields = '__all__'

class SpecialForm(forms.ModelForm):
    class Meta:
        model = Special
        fields = '__all__'
