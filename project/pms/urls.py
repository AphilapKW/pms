from django.urls import path
from . import views

app_name = 'pms'

urlpatterns = [
    path('work_order/list', views.WorkOrderList.as_view(), name='work_order_list'),
    path('work_order/<int:pk>/', views.WorkOrderDetail.as_view(), name='work_order_detail'),

    path('maid_request/list', views.MaidRequestList.as_view(), name='maid_request_list'),
    path('maid_request/<int:pk>/', views.MaidRequestDetail.as_view(), name='maid_request_detail'),

    path('technician_request/list', views.TechnicianRequestList.as_view()),
    path('technician_request/<int:pk>/', views.TechnicianRequestDetail.as_view()),

    path('amenity_request/list', views.AmenityRequestList.as_view()),
    path('amenity_request/<int:pk>/', views.AmenityRequestDetail.as_view()),

]
