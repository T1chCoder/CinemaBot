from . import templates, views

class StartCommandView(templates.CommandView):
    text = "start"
    redirect_to = views.HomeView