"""munager_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import sys

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

sys.path.append("..")  # TODO: be less janky

from schema import schema  # noqa: E402

print(schema)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gateway/', csrf_exempt(GraphQLView.as_view(schema=schema)))
]

if settings.DEBUG:
    urlpatterns.append(path('gui/',
                            GraphQLView.as_view(graphiql=True, schema=schema)))
