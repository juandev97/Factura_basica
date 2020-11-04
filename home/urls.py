from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^home/', views.get_facturas),
	url(r'form_item',views.new_item),
	url(r'form_factura',views.new_factura),
	url(r'form_persona',views.new_persona),
	url(r'^', views.inicio),

]

