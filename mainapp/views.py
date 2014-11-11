from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
class HomeView(TemplateView):
    template_name = "home.html"