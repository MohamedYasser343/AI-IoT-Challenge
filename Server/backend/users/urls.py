from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'users'
router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, ),
    path('test_token/', views.test_token, name='test_token_page'),
    path('adminPage/', views.administrator_page, name='administrator_page'),
    path('profile/', include(router.urls)),
    
    path('managers/', views.ListCreateManagers.as_view(), name='list_create_managers'),
    path('managers/<int:pk>/', views.ManagersDetail.as_view(), name='managers_detail'),
    
    path('data_analysts/', views.ListCreateAnalysts.as_view(), name='list_create_analysts'),
    path('data_analysts/<int:pk>/', views.AnalystsDetail.as_view(), name='analysts_detail'),
    
    path('farmers/', views.ListCreateFarmers.as_view(), name='list_create_farmers'),
    path('farmers/<int:pk>/', views.FarmersDetail.as_view(), name='farmers_detail'),
]

urlpatterns += static(settings.MEDIA_URLS, document_root=settings.MEDIA_ROOT)
