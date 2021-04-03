"""LearnML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Pages.views import home_view, learn_view, signIn_view, signUp_view, signOut_view, faq_view, user_data_view, choosing_view
from ML_models.views import polynomial_regression_view




urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home_view, name='home'),
    path('test/',user_data_view, name='test'),
    path('learn/',learn_view, name='learning page'),
    path('signin/',signIn_view, name='sign in page'),
    path('polynomialRegression/',polynomial_regression_view, name='polynomial regression'),
    path('signup/',signUp_view, name='sign up page'),
    path('signout/',signOut_view, name='sign out page'),
    path('faq/',faq_view, name='faq page'),
    path('choosing/',choosing_view, name='choosing page'),
]
