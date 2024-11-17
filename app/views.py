from . import templates

class HomeView(templates.TemplateView):
    text = "Добро пожаловать! Выберите одну из страниц."

class SearchView(templates.TemplateView):
    text = "Поиск"

class HelpView(templates.TemplateView):
    text = "Поиск"