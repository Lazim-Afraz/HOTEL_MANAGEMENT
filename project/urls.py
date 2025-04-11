from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotel_booking/', include('hotel_booking.urls')),

    # 👇 Redirect root URL to hotel_booking/
    path('', RedirectView.as_view(url='/hotel_booking/', permanent=False)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
