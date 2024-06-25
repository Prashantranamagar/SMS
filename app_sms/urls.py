from django.urls import path
from .views import (
    home,
    SignupView,
    CustomLogoutView,
    CustomLoginView,
    StudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    StudentDetailView,
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    EnrollmentListView,
    EnrollmentDetailView,
    EnrollmentCreateView,
    EnrollmentUpdateView,
    EnrollmentDeleteView,
    InstructorListView,
    InstructorDetailView,
    InstructorCreateView,
    InstructorUpdateView,
    InstructorDeleteView,
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),

    # Students URLs
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/new/', StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    # Courses URLs
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/new/', CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/edit/', CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),

    # Enrollments URLs
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollments/new/', EnrollmentCreateView.as_view(), name='enrollment-create'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment-detail'),
    path('enrollments/<int:pk>/edit/', EnrollmentUpdateView.as_view(), name='enrollment-update'),
    path('enrollments/<int:pk>/delete/', EnrollmentDeleteView.as_view(), name='enrollment-delete'),

    # Instructor URLs
    path('instructors/', InstructorListView.as_view(), name='instructor-list'),
    path('instructors/new/', InstructorCreateView.as_view(), name='instructor-create'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
    path('instructors/<int:pk>/edit/', InstructorUpdateView.as_view(), name='instructor-update'),
    path('instructors/<int:pk>/delete/', InstructorDeleteView.as_view(), name='instructor-delete'),
]