from django.views.generic import TemplateView
class Calender(TemplateView):
    template_name = "calender/index.html"
    def get_context_data(self, **kwargs):
        context = super(Calender,self).get_context_data(**kwargs)
        return context