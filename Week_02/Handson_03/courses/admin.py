from django.contrib import admin
from .models import Department, Course, Student, Enrollment

# Step 22: Register basic models directly so they show up in the admin list -- revsion
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Enrollment)

# Steps 23 & 24: Create a highly customized dashboard panel for Courses
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Step 23: Display these fields as clean, organized columns instead of just one name string
    list_display = ['name', 'code', 'credits', 'department']
    
    # Step 23: Add a search bar at the top that looks through names and course codes instantly
    search_fields = ['name', 'code']
    
    # Step 24: Add a sidebar module on the right to filter rows by their department group
    list_filter = ['department']