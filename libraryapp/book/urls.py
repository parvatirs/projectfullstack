from django.urls import path,include
from .  import views
from libraryapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ,name='index'),
    path('accounts/',include('django.contrib.auth.urls') ),

    path('upload/', views.upload, name = 'upload-book'),
    path('delete/<int:book_id>', views.delete_book),
    path('update/<int:book_id>', views.update_book),
    path('library', views.library),
    path('adminsignup', views.adminsignup_view),
    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='book/adminlogin.html')),
    path('logout', LogoutView.as_view(template_name='book/home.html')),
    path('afterlogin', LoginView.as_view(template_name='book/library.html')),
    ]

#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)