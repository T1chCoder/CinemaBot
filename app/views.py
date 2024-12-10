from . import templates, models

#Views
class HomeView(templates.TemplateView):
    text = (
        "🎥 *Welcome to CinemaBot!* 🍿\n\n"
        "CinemaBot is your personal guide to the world of cinema, right in Telegram! 🚀\n\n"
        "🌟 *What can CinemaBot do?*\n\n"
        "🔍 *Movie Search*: Discover everything about any movie — plot, cast, genre, and more.\n"
        "⭐️ *Reviews and Ratings*: Read reviews and check ratings from popular services.\n"
        "🎞 *Trailers and Stills*: Watch trailers and browse galleries of the movies you love.\n"
        "🤖 *Recommendations*: Get personalized movie picks based on your preferences.\n"
        "🕒 *Cinema Showtimes*: Find nearby screenings and buy tickets.\n"
        "📰 *Movie News*: Stay updated with hot news and premieres!\n\n"
        "👉 [Add CinemaBot to your Telegram](https://t.me/CinemaBot)\n"
    )

class RecommendedMoviesView(templates.TemplateView):
    text = (
        "🤖 *CinemaBot Recommendations* 🎬\n\n"
        "Can't decide what to watch? Don't worry, CinemaBot has got you covered! 🎉\n\n"
        "Based on your preferences, tastes, and favorite genres, the bot will suggest movies you'll love.\n\n"
        "🌟 *How does it work?*\n\n"
        "1. Answer a few questions to customize your recommendations.\n"
        "2. CinemaBot will suggest movies that match your interests.\n"
        "3. You can view details for each movie: trailers, ratings, reviews, and more.\n\n"
        "🎥 Start receiving personalized recommendations right now!"
    )
    
class MovieSearchResultView(templates.TemplateView):
    text = (
        "Found"
        )

class NewMoviesView(templates.TemplateView):
    text = (
        "✨ *New Movie Releases* 🎬\n\n"
        "Looking for the freshest films? CinemaBot will help you discover what’s just hit the theaters! 🍿\n\n"
        "🔥 *What to expect?*\n\n"
        "📅 A list of the latest movies that have just premiered in cinemas.\n"
        "⭐ Ratings and reviews from viewers and critics.\n"
        "🎥 Trailers of new releases — stay updated on the most anticipated movies!\n"
        "📰 News and details about premieres.\n\n"
        "Click below to see the latest releases and pick a movie to watch!"
    )

class MovieTrailersView(templates.TemplateView):
    text = (
        "🎥 *Movie Trailers* 🍿\n\n"
        "Want a sneak peek at what’s coming to the screen? CinemaBot will help you watch the latest trailers! 🎬\n\n"
        "🌟 *What to expect?*\n\n"
        "📹 Watch trailers of the most anticipated movies.\n"
        "🎞 Exclusive clips and scenes from upcoming releases.\n"
        "🔥 Immerse yourself in the atmosphere of future blockbusters through trailers.\n\n"
        "Select a movie to watch its trailer, or simply enjoy the collection!"
    )

class MovieRatingsView(templates.TemplateView):
    text = (
        "🌟 *Movie Ratings* 🎬\n\n"
        "Want to know how movies are rated by audiences and critics? CinemaBot will guide you to the films worth your attention! 🍿\n\n"
        "⭐ *What to expect?*\n\n"
        "📊 Detailed movie ratings from popular platforms like IMDb, Rotten Tomatoes, and more.\n"
        "🎥 Reviews and critiques from professionals.\n"
        "👥 Viewer ratings — see how regular audiences rate the movie.\n\n"
        "Select a movie to view its rating, or explore the top-rated films!"
    )

class TheatreSessionsView(templates.TemplateView):
    text = (
        "🎬 *Cinema Showtimes* 🍿\n\n"
        "Want to know when you can watch your favorite movie? CinemaBot will help you find the nearest showtimes! 🕒\n\n"
        "🌟 *What to expect?*\n\n"
        "📅 Showtimes at nearby cinemas.\n"
        "🎥 Information about movies currently playing in theaters.\n"
        "📍 Search for showtimes based on your location.\n"
        "🎫 Option to book tickets for your selected showtime.\n\n"
        "Enter the movie title or select a cinema to see available showtimes."
    )

class MovieNewsView(templates.TemplateView):
    text = (
        "📰 *Movie News* 🎬\n\n"
        "Want to stay updated on all the latest releases, premieres, and rumors from the world of cinema? CinemaBot has gathered the hottest news just for you! 🌟\n\n"
        "🔥 *What to expect?*\n\n"
        "📅 The latest updates on movies and TV series.\n"
        "🎞 Announcements of upcoming premieres and events.\n"
        "🎬 Interviews with actors and directors.\n"
        "📝 Reviews and news from the film industry.\n\n"
        "Select a news story to learn more, or simply keep an eye on the latest updates!"
    )

class HelpView(templates.TemplateView):
    text = (
        "❓ *Help* 📝\n\n"
        "Don't know how to use CinemaBot? Don't worry, we're here to help! 🚀\n\n"
        "🎬 *What can CinemaBot do?*\n\n"
        "1. 🔍 *Movie Search* — get detailed information about any movie.\n"
        "2. ⭐️ *Ratings and Reviews* — read audience and critic reviews.\n"
        "3. 🎞 *Trailers* — watch trailers for the most anticipated movies.\n"
        "4. 🕒 *Cinema Showtimes* — find nearby showtimes and buy tickets.\n"
        "5. 📰 *Movie News* — stay updated with the latest releases and announcements.\n"
        "6. 🤖 *Recommendations* — get personalized movie suggestions.\n\n"
        "🛠 *How to get started?*\n\n"
        "1. Use commands or menu buttons to navigate the bot.\n"
        "2. Enter a movie title or select a category to search.\n"
        "3. Keep track of new releases, ratings, and news in the movie world.\n\n"
        "If you have any questions or suggestions, feel free to reach out to us! 📩"
    )

# List-Views
class MovieListView(templates.ListView):
    pass

# Detail-Views
class MovieDetailView(templates.DetailView):
    model = models.Movie
    context_name = model.__tablename__

    async def info(self, item):
        async def message():
            text = (
                f"""🎬 **Movie Title:** {item.title}\n"""
                f"""🌍 **Country:** {item.country_uuid}\n"""
                f"""⏱️ **Duration:** {item.duration} minutes\n"""
                f"""📅 **Release Date:** {item.released_at}\n"""
                f"""⭐ **Rating:** {item.rating}\n"""
                f"""This is a true masterpiece worth seeing! 🌟"""
            )
            self.text = text
            return text
            
        return {"message": await message()}