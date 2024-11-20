from . import templates, views, states

class StartCommandView(templates.CommandView):
    text = "start"
    redirect_to = views.HomeView

class HelpCommandView(templates.CommandView):
    text = "help"
    redirect_to = views.HelpView

class MovieSearchCommandView(templates.CommandView):
    text = "search"
    redirect_to = states.MovieSearchStateView

class RecommendedMoviesCommandView(templates.CommandView):
    text = "recommendations"
    redirect_to = views.RecommendedMoviesView

class NewMoviesCommandView(templates.CommandView):
    text = "releases"
    redirect_to = views.NewMoviesView

class MovieTrailersCommandView(templates.CommandView):
    text = "trailers"
    redirect_to = views.MovieTrailersView

class MovieRatingsCommandView(templates.CommandView):
    text = "ratings"
    redirect_to = views.MovieRatingsView

class TheatreSessionsCommandView(templates.CommandView):
    text = "showtimes"
    redirect_to = views.TheatreSessionsView

class MovieNewsCommandView(templates.CommandView):
    text = "news"
    redirect_to = views.MovieNewsView