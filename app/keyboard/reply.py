from app import views, states
from app import templates

class SearchReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🔍 Search"
    pages = [
        views.HomeView, 
        views.RecommendedMoviesView, 
        views.MovieSearchResultView, 
        views.NewMoviesView, 
        views.MovieTrailersView, 
        views.MovieRatingsView, 
        views.HelpView, 
        views.MovieDetailView
    ]
    redirect_to = states.MovieSearchStateView

class RecommendedMoviesReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🎬 Recommendations"
    pages = [
        views.HomeView, 
        views.RecommendedMoviesView, 
        views.MovieSearchResultView, 
        views.NewMoviesView, 
        views.MovieTrailersView, 
        views.MovieRatingsView, 
        views.HelpView, 
        views.MovieDetailView
    ]
    redirect_to = views.RecommendedMoviesView

class NewMoviesReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "✨ Releases"
    pages = [
        views.HomeView, 
        views.RecommendedMoviesView, 
        views.MovieSearchResultView, 
        views.NewMoviesView, 
        views.MovieTrailersView, 
        views.MovieRatingsView, 
        views.HelpView, 
        views.MovieDetailView
    ]
    redirect_to = views.NewMoviesView

class MovieTrailersReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🎥 Trailers"
    pages = [
        views.HomeView, 
        views.RecommendedMoviesView, 
        views.MovieSearchResultView, 
        views.NewMoviesView, 
        views.MovieTrailersView, 
        views.MovieRatingsView, 
        views.HelpView, 
        views.MovieDetailView
    ]
    redirect_to = views.MovieTrailersView

class MovieRatingsReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🌟 Ratings"
    pages = [
        views.HomeView, 
        views.RecommendedMoviesView, 
        views.MovieSearchResultView, 
        views.NewMoviesView, 
        views.MovieTrailersView, 
        views.MovieRatingsView, 
        views.HelpView, 
        views.MovieDetailView
    ]
    redirect_to = views.MovieRatingsView
    
class HelpReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "❓ Help"
    pages = [
        views.HomeView, 
        views.RecommendedMoviesView, 
        views.MovieSearchResultView, 
        views.NewMoviesView, 
        views.MovieTrailersView, 
        views.MovieRatingsView, 
        views.HelpView, 
        views.MovieDetailView
    ]
    redirect_to = views.HelpView