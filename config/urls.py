from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("web.urls", "web"), namespace="web")),
    path("receitas/", include(("receitas.urls", "receitas"), namespace="receitas")),
    path("contato/", include(("contato.urls", "contato"), namespace="contato")),
    path("usuarios/", include(("usuarios.urls", "usuarios"), namespace="usuarios")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
