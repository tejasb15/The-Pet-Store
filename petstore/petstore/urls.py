"""
URL configuration for petstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from petapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.Index,name='Index'),
    path('display/',views.Display,name='Display'),
    path('delete/<int:id>',views.Delete,name='delete'),
    path('update/<int:id>',views.Update,name='update'),
    path('base/',views.UserBase,name='base'),
    path('userindex/',views.UserIndex,name='userIndex'),
    path('cart/',views.AddToCart,name='cart'),
    path('removecart/<int:id>',views.RemoveCart,name='removecart'),
    path('search/',views.ComponentSearch,name='search'),
    path('details/<int:id>',views.Details,name='details'),
    path('signup/',views.Signup,name='signup'),
    path('',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('email/',views.Email),
    path('address/<int:id>',views.address,name='address'),
    path('preorder/<int:aid>/<int:pid>',views.Pre_order,name='preorder'),
    path('orderconfirm/<int:aid>/<int:pid>',views.Order_Confirm,name='orderconfirm'),
    path('pay/<int:aid>/<int:pid>',views.Payment,name='pay'),
    path('cartaddress/',views.Cart_Address,name='cartaddress'),
    path('cartpreorder/<int:aid>',views.Cart_Preorder,name='cartpreorder'),
    path('cartorderconfirm/<int:aid>',views.Cart_OrderConfirm,name='cartorderconfirm'),
    path('cartpay/<int:aid>',views.Cart_Payment,name='cartpay'),
    path('adminSignUp/',views.AdminSignup,name='adminSignUp'),
    path('adminlogin/',views.AdminLogin,name='adminlogin'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)