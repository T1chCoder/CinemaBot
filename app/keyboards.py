import config
from . import views
from . import templates

class HelpInlineButtonView(templates.ReplyKeyboardButtonView):
    text = "Помощь"
    callback_data = "help"
    pages = [views.HomeView, views.SearchView]
    redirect_to = views.HelpView