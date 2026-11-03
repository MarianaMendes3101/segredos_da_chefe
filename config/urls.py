
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial e páginas institucionais
    path('', include('web.urls')),

    # Receitas
    path('', include(('receitas.urls', 'receitas'), namespace='receitas')),

    # Contato e usuários
    path('contato/', include('contato.urls')),
    path('usuarios/', include('usuarios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
