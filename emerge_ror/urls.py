"""emerge_ror URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ror import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login_page, name='login'),
    url(r'^home/', views.home_page, name='home'),
    url(r'^refresh_database', views.refresh_database, name='refresh_database'),
    url(r'^patient/report', views.patient_report_page, name='patient_report'),
    url(r'^patient/notes', views.patient_notes_page, name='patient_notes'),
    url(r'^patient/summary', views.patient_summary_page, name='patient_summary'),
    url(r'^patient/research', views.patient_research_page, name='patient_research'),
    url(r'^patient/phenolyzer', views.patient_phenolyzer_page, name='patient_phenolyzer'),

]



