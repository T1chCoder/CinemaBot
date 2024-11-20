from app import views, states
from app import templates

class SearchReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🔍 Поиск фильма"
    pages = [views.HomeView]
    redirect_to = states.MovieSearchStateView

class RecommendedMoviesReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🎬 Рекомендации"
    pages = [views.HomeView]
    redirect_to = views.RecommendedMoviesView

class NewMoviesReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "✨ Новинки"
    pages = [views.HomeView]
    redirect_to = views.NewMoviesView

class MovieTrailersReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🎥 Трейлеры"
    pages = [views.HomeView]
    redirect_to = views.MovieTrailersView

class MovieRatingsReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🌟 Рейтинг фильмов"
    pages = [views.HomeView]
    redirect_to = views.MovieRatingsView

class MovieNewsReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "📰 Новости кино"
    pages = [views.HomeView]
    redirect_to = views.MovieNewsView

class TheatreSessionsReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🎫 Сеансы кинотеатров"
    pages = [views.HomeView]
    redirect_to = views.TheatreSessionsView