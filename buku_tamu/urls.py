from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render




# def buku(request):
#     return HttpResponse('Teknik Informatika Unsulbar')

# def buku(request):
#     return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def landing_page(request):
    return render(request, 'landingpage.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', buku, name='index'), 
    path('about/', about_page, name='about'),
    path('landingpage/', landing_page, name='landingpage'),

    # dari models base
    path('', include('base.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


