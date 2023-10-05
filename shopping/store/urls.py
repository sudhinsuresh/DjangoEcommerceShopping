from store import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('store/',views.store,name="store"),
    path('store/category/<slug:category_slug>/',views.store,name="products_by_category"),
    path('store/category/<slug:category_slug>/<slug:product_slug>/',views.product_detail,name="product_detail"),
    path('store/search/',views.search,name="search"),
    path('store/submit_review/<int:product_id>/',views.submit_review,name="submit_review"),
    
    
    
]