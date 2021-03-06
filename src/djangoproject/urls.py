from django.urls import path
from django.contrib import admin
from djangoapp import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home, name='home'),
    path('add/', views.add, name='add'),
    path('inventario/', views.inventario, name='inventario'),
    path('inventario/<id>/', views.edit, name="edit"),
    path('inventario/<id>/delete/', views.delete, name="delete"),
    path('panel/', views.panel, name='panel'),
    path('accounts/', include('registration.backends.default.urls'))
]
