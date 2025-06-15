from django.db import models
from django.contrib.auth.models import User

class Year(models.Model):
    year = models.CharField(max_length=255,null=True)

    def __str__(self):
        return str(self.year)

class Department(models.Model):
    sr_no = models.PositiveIntegerField(unique=True)  # Serial Number
    name = models.CharField(max_length=255, unique=True)  # Department Name

    def __str__(self):
        return self.name
    
class NonTeachingStaff(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    sr_no = models.CharField(max_length=255,null=True)  # Serial Number

    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)  # ForeignKey to Department
    class1_female = models.IntegerField(default=0)
    class1_male = models.IntegerField(default=0)
    class2_female = models.IntegerField(default=0)
    class2_male = models.IntegerField(default=0)
    class3_female = models.IntegerField(default=0)
    class3_male = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Automatically calculate the total before saving
        self.total = (
            self.class1_female + self.class1_male +
            self.class2_female + self.class2_male +
            self.class3_female + self.class3_male
        )
        super().save(*args, **kwargs)

        def __str__(self):
            department_name = self.department.name if self.department else "No Department"
            year_name = self.year if self.year else "No Year"
            return f"{department_name} - {year_name}"


class TeachingStaff(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)  # ForeignKey to Department
    sr_no = models.CharField(max_length=255,null=True)  # Serial Number


    # Professor category
    professor_female = models.IntegerField(default=0)
    professor_male = models.IntegerField(default=0)

    # Associate Professor category
    associate_professor_female = models.IntegerField(default=0)
    associate_professor_male = models.IntegerField(default=0)

    # Assistant Professor category
    assistant_professor_female = models.IntegerField(default=0)
    assistant_professor_male = models.IntegerField(default=0)

    total = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Automatically calculate the total before saving
        self.total = (
            self.professor_female + self.professor_male +
            self.associate_professor_female + self.associate_professor_male +
            self.assistant_professor_female + self.assistant_professor_male
        )
        super().save(*args, **kwargs)

    def __str__(self):
        department_name = self.department.name if self.department else "No Department"
        year_name = self.year if self.year else "No Year"
        return f"{department_name} - {year_name}"
    
class PhDStudent(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)  # ForeignKey to Department
    sr_no = models.CharField(max_length=255,null=True)  # Serial Number
    # Boys Categories
    boys_general = models.IntegerField(default=0)
    boys_st = models.IntegerField(default=0)
    boys_sc = models.IntegerField(default=0)
    boys_sebc = models.IntegerField(default=0)
    boys_ews = models.IntegerField(default=0)

    # Girls Categories
    girls_general = models.IntegerField(default=0)
    girls_st = models.IntegerField(default=0)
    girls_sc = models.IntegerField(default=0)
    girls_sebc = models.IntegerField(default=0)
    girls_ews = models.IntegerField(default=0)

    # Total
    total_boys = models.IntegerField(default=0)
    total_girls = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Auto-calculate total boys and girls before saving
        self.total_boys = (
            self.boys_general + self.boys_st + self.boys_sc +
            self.boys_sebc + self.boys_ews
        )
        self.total_girls = (
            self.girls_general + self.girls_st + self.girls_sc +
            self.girls_sebc + self.girls_ews
        )
        super().save(*args, **kwargs)

        def __str__(self):
            department_name = self.department.name if self.department else "No Department"
            year_name = self.year if self.year else "No Year"
            return f"{department_name} - {year_name}"




class Course(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="courses")
    name = models.CharField(max_length=255)  # Course Name
    boys_general = models.PositiveIntegerField(default=0)
    boys_st = models.PositiveIntegerField(default=0)
    boys_sc = models.PositiveIntegerField(default=0)
    boys_sebc = models.PositiveIntegerField(default=0)
    boys_ews = models.PositiveIntegerField(default=0)
    girls_general = models.PositiveIntegerField(default=0)
    girls_st = models.PositiveIntegerField(default=0)
    girls_sc = models.PositiveIntegerField(default=0)
    girls_sebc = models.PositiveIntegerField(default=0)
    girls_ews = models.PositiveIntegerField(default=0)

    @property
    def total_boys(self):
        return self.boys_general + self.boys_st + self.boys_sc + self.boys_sebc + self.boys_ews

    @property
    def total_girls(self):
        return self.girls_general + self.girls_st + self.girls_sc + self.girls_sebc + self.girls_ews

    def __str__(self):
        return f"{self.department.name} - {self.name}"



class ExamResult(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="exam_results")
    course_name = models.CharField(max_length=255)  # Course Name
    first_class = models.PositiveIntegerField(default=0)  # First Class Count
    second_class = models.PositiveIntegerField(default=0)  # Second Class Count
    pass_class = models.PositiveIntegerField(default=0)  # Pass Class Count
    total_students = models.PositiveIntegerField(default=0)  # Total Students (Auto-calculated)

    def save(self, *args, **kwargs):
        # Automatically calculate total before saving
        self.total_students = self.first_class + self.second_class + self.pass_class
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.department.name} - {self.course_name}"
    

class TeacherInformation(models.Model):

    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    teacher_name = models.CharField(max_length=255)
    conference = models.CharField(max_length=255)
    location_date = models.CharField(max_length=255)  # Ensure this exists
    paper_title = models.CharField(max_length=255)  # Ensure this exists

    def __str__(self):
        return self.teacher_name
    
class TeacherPublicationInformation(models.Model):
 
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    serial_number = models.IntegerField()
    teacher_name = models.CharField(max_length=255)  # English field name
    publication_title = models.CharField(max_length=500)  # English field name
    publisher_details = models.CharField(max_length=500)  # English field name

    def __str__(self):
        return f'{self.teacher_name} - {self.publication_title}' 
    
class ResearchProjectInformation(models.Model):
   
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    serial_number = models.IntegerField()  # Serial Number
    teacher_name = models.CharField(max_length=255)  # Teacher's Name
    research_project_title = models.CharField(max_length=255)  # Research Project Title
    funding_agency = models.CharField(max_length=255)  # Research Grant Providing Institution
    approved_amount = models.CharField(max_length=255)  # Total Amount Approved for Research

    def __str__(self):
        return f"{self.serial_number} - {self.teacher_name} - {self.research_project_title}"

class SpecialNote(models.Model):

    year = models.ForeignKey(Year, on_delete=models.CASCADE,null=True)
    note = models.TextField(help_text="Enter the special note text")
    is_displayed = models.BooleanField(default=False, help_text="Check to display the note in the document")

    def __str__(self):
        return self.note
    
    class Meta:
        verbose_name = 'વિશેષ નોંધ'
        verbose_name_plural = 'વિશેષ નોંધ'

class Specialpro(models.Model):
  
    year = models.ForeignKey(Year, on_delete=models.CASCADE,null=True)
    note = models.TextField(help_text="Enter the special note text")
    is_displayed = models.BooleanField(default=False, help_text="Check to display the note in the document")

    def __str__(self):
        return self.note
    
    class Meta:
        verbose_name = 'વર્ષ દરમ્યાન ભવનમાં કરેલા વિશિષ્ટ પ્રયોગો-પ્રોજેક્ટો વિષયક માહિતી સંક્ષેપમા'
        verbose_name_plural = 'વર્ષ દરમ્યાન ભવનમાં કરેલા વિશિષ્ટ પ્રયોગો-પ્રોજેક્ટો વિષયક માહિતી સંક્ષેપમા'
    

class Special(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE,null=True)
    note = models.TextField(help_text="Enter the special note text")
    is_displayed = models.BooleanField(default=False, help_text="Check to display the note in the document")

    def __str__(self):
        return self.note
    
    class Meta:
        verbose_name = 'વર્ષ દરમ્યાન ભવનમાં રમત-ગમત/યુવક મહોત્સવ /એન.એસ.એસ. રાજ્ય/રાષ્ટ્રીય કક્ષાએ નોંધપાત્ર વિશિષ્ટસન્માન/પારિતોષિક મેળવ્યું હોય તો તેની સંક્ષિપ્ત વિગતો'
        verbose_name_plural = 'વર્ષ દરમ્યાન ભવનમાં રમત-ગમત/યુવક મહોત્સવ /એન.એસ.એસ. રાજ્ય/રાષ્ટ્રીય કક્ષાએ નોંધપાત્ર વિશિષ્ટસન્માન/પારિતોષિક મેળવ્યું હોય તો તેની સંક્ષિપ્ત વિગતો'


