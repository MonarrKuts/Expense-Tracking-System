from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Mobile_expense_tracker.views import UserLoginView, ExpenseListView, ExpenseViewSet, CustomTokenObtainPairView, UserRegistrationView, UserLogoutView, PasswordResetView, ReportUpdateView, ReportDeleteView, ExpenseDetailView, set_budget, generate_pie_chart, create_report

from .views import test_api,get_csrf_token

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Token-related views
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', UserRegistrationView.as_view(), name='user_registration'),
    path('api/logout/', UserLogoutView.as_view(), name='user_logout'),
    path('api/password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/login/', UserLoginView.as_view(), name='user_login'),
#   http://localhost:8000/api/login/
#   http://127.0.0.1:8000/api/register

    # Report-related views
    path('create_report/', create_report, name='create_report'),
    path('update_report/<int:pk>/', ReportUpdateView.as_view(), name='update_report'),
    path('reports/<int:pk>/delete/', ReportDeleteView.as_view(), name='delete_report'),

    # Expense-related views
    path('api/expense/<expense_id>/', ExpenseDetailView.as_view(), name='expense_detail'),
    path('api/expense/', ExpenseListView.as_view(), name='expense-list'),
    #http://localhost:8000/api/expense

    # Other views
    path('set_budget/', set_budget, name='set_budget'),
    path('generate_pie_chart/', generate_pie_chart, name='generate_pie_chart'),

    # test api
    path('api/test/', test_api, name='test_api'),
    path('api/csrf-token/', get_csrf_token, name='csrf_api'),
]

