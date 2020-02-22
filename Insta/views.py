from django.views.generic.base import TemplateView

class HelloWorld(TemplateView):
	template_name = "test.html"
