from django.urls import path
from. import views

urlpatterns=[
  path('chome',views.home),
  path('clogin',views.login),
  path('javascript',views.javascript),
  path('baabtra',views.baabtra),
  path('javascript1',views.javascript1),
  path('dom',views.dom),
  path('domexample',views.domexample),
  path('todoapp',views.todoapp),
  path('calculator',views.calculator),
  path('student',views.student),
  path('jquery',views.jquery),
  path('newpage',views.newpage),
  path('listNew',views.listNew),
  path('calculator1',views.calculator1),
  path('jquery1',views.jquery1),
  path('jqueryform',views.jqueryform), 
  path('jqueryformwork',views.jqueryformwork), 
  path('jqueryslider',views.jqueryslider),
  path('jqueryslider1',views.jqueryslider1),
  path('jqueryslider2',views.jqueryslider2),
  path('snakegame',views.snakegame),
]
