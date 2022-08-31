from django.urls import path

from .views import SignUpView, AgentPageView, AgentDetailPageView, AgentDetailPageView, AgentUpdatePageView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('agents/', AgentPageView.as_view(), name="agents"), 
    path('accountinfo/<int:pk>', AgentDetailPageView.as_view(), name="agentview"), 
    path('accountinfo/<int:pk>/edit', AgentUpdatePageView.as_view(), name="agentupdate"),
]