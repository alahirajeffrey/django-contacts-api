#from contacts_api.views import contact_list, add_contact, contact
from django.urls import path
from contacts_api.views import ContactList, ContactDetail, ContactCreate

urlpatterns = [
    path('list/', ContactList.as_view()),
    path('', ContactCreate.as_view()),
    path('<int:pk>', ContactDetail.as_view())
]
