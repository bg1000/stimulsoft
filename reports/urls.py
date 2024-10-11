from django.urls import path

from reports import views

urlpatterns = [
    path("report/", views.report_view),
     path("report-data/<int:record_id>/", views.report_data),
]
