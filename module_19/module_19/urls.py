from django.contrib import admin
from django.urls import path
from task1.views import platform, shop, bag, news
from task1.views import sign_up_by_html, sign_up_by_django


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', platform), path('shop', shop), path('bag', bag),
    path('reg', sign_up_by_html),
    path('reg_c', sign_up_by_django),
    path('news', news),
]