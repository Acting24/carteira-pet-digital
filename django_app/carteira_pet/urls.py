"""
URLs principais do projeto Carteira Digital Pet
PJI110 - UNIVESP 2026
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# URLs principais do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Página inicial temporária
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    
    # URLs dos apps (adicionar conforme desenvolvimento)
    # path('pets/', include('apps.pets.urls')),
    # path('vacinas/', include('apps.vacinas.urls')),
    # path('auth/', include('apps.core.urls')),
]

# Configuração para arquivos de media em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Personalização do admin
admin.site.site_header = "Carteira Digital Pet - Admin"
admin.site.site_title = "Carteira Pet"
admin.site.index_title = "Administração do Sistema"