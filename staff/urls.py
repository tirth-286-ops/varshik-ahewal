from django.urls import path
from . import views


urlpatterns = [
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
