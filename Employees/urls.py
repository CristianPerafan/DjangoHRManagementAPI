from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'genders',views.GenderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]