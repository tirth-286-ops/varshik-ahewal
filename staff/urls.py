from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    

    path('add-user/', views.add_user, name='add_user'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('change-password/<int:user_id>/', views.change_user_password, name='change_user_password'),
       

    path('year/add/', views.add_year, name='add_year'),
    path('year/edit/<int:pk>/', views.edit_year, name='edit_year'),
    path('year/delete/<int:pk>/', views.delete_year, name='delete_year'),

    # Department URLs
    path('department/add/', views.add_department, name='add_department'),
    path('department/edit/<int:pk>/', views.edit_department, name='edit_department'),
    path('department/delete/<int:pk>/', views.delete_department, name='delete_department'),

    path('non-teaching-staff/add/', views.add_non_teaching_staff, name='add_non_teaching_staff'),
    path('edit/non-teaching-staff/<int:pk>/', views.edit_non_teaching_staff, name='edit_non_teaching_staff'),
    path('delete/non-teaching-staff/<int:pk>/', views.delete_non_teaching_staff, name='delete_non_teaching_staff'),


        # Teaching Staff
    path('teaching-staff/add/', views.add_teaching_staff, name='add_teaching_staff'),
    path('teaching-staff/edit/<int:pk>/', views.edit_teaching_staff, name='edit_teaching_staff'),
    path('teaching-staff/delete/<int:pk>/', views.delete_teaching_staff, name='delete_teaching_staff'),

      # PhDStudent
    path('phd/add/', views.add_phd_student, name='add_phd_student'),
    path('phd/edit/<int:pk>/', views.edit_phd_student, name='edit_phd_student'),
    path('phd/delete/<int:pk>/', views.delete_phd_student, name='delete_phd_student'),

    # Course
    path('course/add/', views.add_course, name='add_course'),
    path('course/edit/<int:pk>/', views.edit_course, name='edit_course'),
    path('course/delete/<int:pk>/', views.delete_course, name='delete_course'),

    # ExamResult
    path('examresult/add/', views.add_exam_result, name='add_exam_result'),
    path('examresult/edit/<int:pk>/', views.edit_exam_result, name='edit_exam_result'),
    path('examresult/delete/<int:pk>/', views.delete_exam_result, name='delete_exam_result'),

    # TeacherInformation
    path('teacherinfo/add/', views.add_teacher_information, name='add_teacher_information'),
    path('teacherinfo/edit/<int:pk>/', views.edit_teacher_information, name='edit_teacher_information'),
    path('teacherinfo/delete/<int:pk>/', views.delete_teacher_information, name='delete_teacher_information'),

    # TeacherPublicationInformation
    path('publication/add/', views.add_teacher_publication, name='add_teacher_publication'),
    path('publication/edit/<int:pk>/', views.edit_teacher_publication, name='edit_teacher_publication'),
    path('publication/delete/<int:pk>/', views.delete_teacher_publication, name='delete_teacher_publication'),

    # ResearchProjectInformation
    path('project/add/', views.add_research_project, name='add_research_project'),
    path('project/edit/<int:pk>/', views.edit_research_project, name='edit_research_project'),
    path('project/delete/<int:pk>/', views.delete_research_project, name='delete_research_project'),

    # SpecialNote
    path('specialnote/add/', views.add_special_note, name='add_special_note'),
    path('specialnote/edit/<int:pk>/', views.edit_special_note, name='edit_special_note'),
    path('specialnote/delete/<int:pk>/', views.delete_special_note, name='delete_special_note'),

    # Specialpro
    path('specialpro/add/', views.add_specialpro, name='add_specialpro'),
    path('specialpro/edit/<int:pk>/', views.edit_specialpro, name='edit_specialpro'),
    path('specialpro/delete/<int:pk>/', views.delete_specialpro, name='delete_specialpro'),

    # Special
    path('special/add/', views.add_special, name='add_special'),
    path('special/edit/<int:pk>/', views.edit_special, name='edit_special'),
    path('special/delete/<int:pk>/', views.delete_special, name='delete_special'),
    path('logout/', views.logout_view, name='logout'),

    
    path('index/', views.index, name='index'),
     path('year/', views.year_selection, name='year_selection'),
    path('export-excel/', views.export_to_excel, name='export_to_excel'),
    path('teching/', views.teching, name='teching'),
    path('PhD/', views.PhD, name='PhD'),
    path('export2/',views.export2, name='export2'),
    path('export/', views.export, name='export'),
    path('download/', views.download, name='download'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),





]
