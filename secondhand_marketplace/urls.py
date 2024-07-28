from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import register, login_view, logout_view, profile_view, home, activity_feed, CustomPasswordResetView, CustomPasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),        
    path('', home, name='home'),
    path('activity/', activity_feed, name='activity_feed'),
    #path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    #path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('users/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('listings/', include('listings.urls')),
    path('messaging/', include('messaging.urls')),
    path('', include('django.contrib.auth.urls')),  
     path('login/', login_view, name='login'),  
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

