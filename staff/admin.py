from django.contrib import admin
from .models import NonTeachingStaff,TeachingStaff,PhDStudent, Department, Course,ExamResult,TeacherInformation,TeacherPublicationInformation,ResearchProjectInformation,SpecialNote,Specialpro,Special,Year

@admin.register(NonTeachingStaff)
class NonTeachingStaffAdmin(admin.ModelAdmin):
    list_display = ('sr_no','department', 'year', 'class1_female', 'class1_male', 
                    'class2_female', 'class2_male', 'class3_female', 'class3_male', 'total')
    ordering = ('department',)


@admin.register(TeachingStaff)
class TeachingStaffAdmin(admin.ModelAdmin):
    list_display = ('sr_no','department', 'year', 
                    'professor_female', 'professor_male', 
                    'associate_professor_female', 'associate_professor_male', 
                    'assistant_professor_female', 'assistant_professor_male', 'total')
    search_fields = ('department__name',)
    list_filter = ('department', 'year')




@admin.register(PhDStudent)
class PhDStudentAdmin(admin.ModelAdmin):
    list_display = ('sr_no',
        'department', 'year',
        'boys_general', 'boys_st', 'boys_sc', 'boys_sebc', 'boys_ews',
        'girls_general', 'girls_st', 'girls_sc', 'girls_sebc', 'girls_ews',
        'total_boys', 'total_girls'
    )
    search_fields = ('department__name',)
    list_filter = ['year', 'department']

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)  



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'name')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('department', 'name', 'total_boys', 'total_girls')
    list_filter = ('department',)



class ExamResultInline(admin.TabularInline):
    model = ExamResult
    extra = 1  # Allow adding multiple courses under a department


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('department', 'course_name', 'first_class', 'second_class', 'pass_class', 'total_students')
    list_filter = ('department',)
    search_fields = ('course_name',)



class TeacherInformationAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'conference', 'location_date', 'paper_title']  # Use English field names

admin.site.register(TeacherInformation, TeacherInformationAdmin)

@admin.register(TeacherPublicationInformation)
class TeacherPublicationInformationAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'teacher_name', 'publication_title', 'publisher_details')
    search_fields = ('teacher_name', 'publication_title')


@admin.register(ResearchProjectInformation)
class ResearchProjectInformationAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'teacher_name', 'research_project_title', 'funding_agency', 'approved_amount')
    search_fields = ('teacher_name', 'research_project_title', 'funding_agency')
    list_filter = ('funding_agency',)

class SpecialNoteAdmin(admin.ModelAdmin):
    list_display = ['note', 'is_displayed']
    list_filter = ['is_displayed']
    search_fields = ['note']

admin.site.register(SpecialNote, SpecialNoteAdmin)

class SpecialNoteAdmin(admin.ModelAdmin):
    list_display = ['note', 'is_displayed']
    list_filter = ['is_displayed']
    search_fields = ['note']

admin.site.register(Specialpro, SpecialNoteAdmin)

class SpecialNoteAdmin(admin.ModelAdmin):
    list_display = ['note', 'is_displayed']
    list_filter = ['is_displayed']
    search_fields = ['note']

admin.site.register(Special, SpecialNoteAdmin)

