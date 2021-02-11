from django.conf import global_settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import SignupView, landing_page
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', landing_page, name='landing-page'),
    path('leads/', include('leads.urls', namespace="leads")),
    path('agents/', include('agents.urls', namespace="agents")),
    path('signup/', SignupView.as_view(), name="signup"),
    path('reset-password/', PasswordResetView.as_view(), name="reset-password"),
    path('password-reset-done', PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset-complete', PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
]

if global_settings.DEBUG:
    urlpatterns += static(global_settings.STATIC_URL,
                          document_root=global_settings.STATIC_ROOT)
