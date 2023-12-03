from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    path('accounts/',include('allauth.urls')),
    # path('accounts/', include('allauth.socialaccount.urls'), name='social'),
]

handler404 = 'main.views.handling_404'
handler500 = 'main.views.handling_500'


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

