from . import templates, models, actions
import asyncio

# List-Views
class MovieSearchListView(templates.ListView):
    pass 

class RecommendedMovieListView(templates.ListView):
    pass

class NewMovieListView(templates.ListView):
    pass

class MovieTrailerListView(templates.ListView):
    pass

class MovieRatingListView(templates.ListView):
    pass

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
        "✨ *Movie recommendations for You!* 🎬\n\n"
        "We’ve picked out some amazing movies that we think you'll love! Based on your interests, here are some top picks to explore 🔥\n\n"
        "👇 Click on a movie to discover more:"
    )
    text_no = (
        "😞 *No movie recommendations at the moment.* 🎥\n\n"
        "Unfortunately, we don’t have any recommendations for you at the moment. But don’t worry, our collection is constantly growing! 🌟\n\n"
        "🔄 Check back later for more personalized suggestions or explore other categories in the meantime!"
    )
    list = True
    redirect_to = RecommendedMovieListView
    
    async def items(self):
        model = models.Movie 
        recommended_movies = await actions.db.get(model)
        inline_buttons = []
        
        for recommended_movie in recommended_movies:
            inline_buttons.append({
                "text": recommended_movie.title, 
                "callback_data": f"{model.__tablename__}_{recommended_movie.uuid.lower()}"
            })
            
        return inline_buttons
    
class MovieSearchResultView(templates.TemplateView):
    text = (
        "Found"
        )

class NewMoviesView(templates.TemplateView):
    text = (
        "✨ *New movie releases* 🎬\n\n"
        "Get ready for the latest and greatest movies hitting the big screen! Check out these exciting releases and click below to learn more about each one. Don't miss out on the action, adventure, and drama coming your way! 🎥✨\n\n"
        "👇 Choose a movie to explore more:"
    )
    text_no = (
        "😞 *No new movie releases at the moment* 🎥\n\n"
        "It looks like there are no fresh movie releases right now, but don't worry — new films are coming soon! 🎬 Stay tuned for exciting updates and upcoming releases! 🌟\n\n"
        "🔄 Check back later for the latest movie updates and explore other categories in the meantime!"
    )
    list = True
    redirect_to = MovieSearchListView
    
    async def items(self):
        model = models.Movie 
        new_movies = await actions.db.get(model)
        inline_buttons = []
        
        for new_movie in new_movies:
            inline_buttons.append({
                "text": new_movie.title, 
                "callback_data": f"{model.__tablename__}_{new_movie.uuid.lower()}"
            })
        
        return inline_buttons

class MovieTrailersView(templates.TemplateView):
    text = (
        "🎥 *Movie Trailers* 🍿\n\n"
        "Get a sneak peek at the hottest upcoming movies! Watch the official trailers and get excited about the action, drama, and thrills coming soon to theaters. 🎥✨\n\n"
        "👇 Choose a movie to watch trailers:"
    )
    text_no = (
        "😞 *No movie trailers available right now* 🎬\n\n"
        "It seems like we don't have any trailers at the moment, but don't worry — more exciting content is coming soon! 🎥 Stay tuned for the latest trailers and updates on upcoming movies! 🌟\n\n"
        "🔄 Check back later for fresh trailers or explore other sections for more movie info!"
    )
    list = True
    redirect_to = MovieTrailerListView
    
    async def items(self):
        model = models.Movie 
        selected_movies = await actions.db.get(model)
        inline_buttons = []
        
        for selected_movie in selected_movies:
            inline_buttons.append({
                "text": selected_movie.title, 
                "callback_data": f"{model.__tablename__}_{selected_movie.uuid.lower()}"
            })
        
        return inline_buttons

class MovieRatingsView(templates.TemplateView):
    text = (
        "🌟 *Movie Ratings* 🎬\n\n"
        "Want to know what others think about the latest movies? Read reviews and check ratings from popular services to help you decide what to watch next! 📽️✨\n\n"
        "👇 Choose a movie to see reviews:"
    )
    text_no = (
        "😞 No movie options available at the moment 🎬\n\n"
        "It seems we don't have any movies to display right now. We're constantly updating our list, so check back soon for more options! 🌟\n\n"
        "🔄 Stay tuned for new movie releases and exciting content!"
    )
    list = True 
    redirect_to = MovieRatingListView
    
    async def items(self):
        model = models.Movie 
        selected_movies = await actions.db.get(model)
        inline_buttons = []
        
        for selected_movie in selected_movies:
            inline_buttons.append({
                "text": selected_movie.title, 
                "callback_data": f"{model.__tablename__}_{selected_movie.uuid.lower()}"
            })
        
        return inline_buttons

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
    
# Detail-Views
class MovieDetailView(templates.DetailView):
    model = models.Movie
    context_name = model.__tablename__

    async def info(self, item):
        async def message():
            text = (
                f"""🎬 *{item.title}*\n\n"""
                f"""{item.short_description}\n\n"""
                f"""💡 *What Awaits You?*\n\n"""
                f"""{item.description}\n\n"""
                f"""📜 *Details:*\n\n"""
                f"""🌍 *Country:* {item.country_uuid}\n"""
                f"""⏱️ *Duration:* {actions.sec_to_hms(item.duration)}\n"""
                f"""📅 *Release date:* {item.released_at.strftime("%d %B %Y")}\n"""
                f"""⭐ *Rating:* {item.rating.value} / 5.0\n\n"""
                f"""🎟 Grab your popcorn and dive into this unforgettable journey! 🍿  """
            )
            self.text = text
            return text
            
        return {"message": await message()}