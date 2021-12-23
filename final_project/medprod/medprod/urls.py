"""medprod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import app.views as view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/<int:id>/', view.product, name='product'),
    path('products/', view.products, name='products'),
    path('', view.products, name='products'),
    path('home/', view.home, name='home'),
    path('company/', view.company, name='company'),
    path('add_product/', view.add_product, name='add_product'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('application/', view.application, name='application'),
    path('partners/', view.partners, name='partners'),
    path('contacts/', view.contacts, name='contacts'),
    path('sales/', view.sales, name='sales'),
    path('employes/', view.employes, name='employes'),
    path('materials/', view.materials, name='materials'),
    path('recipe/', view.recipe, name='recipe'),
    path('add_consumer/', view.add_consumer, name='add_consumer'),
    #path('search/', view.SearchView.as_view(), name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
