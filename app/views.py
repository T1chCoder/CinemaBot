from . import templates, models, actions
from datetime import date, timedelta
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

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
                "callback_data": f"{model.__tablename__}_uuid_{recommended_movie.uuid.lower()}_detail"
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
            thirty_days_ago = date.today() - timedelta(days=30)
            if new_movie.released_at >= thirty_days_ago:
                inline_buttons.append({
                    "text": new_movie.title, 
                    "callback_data": f"{model.__tablename__}_uuid_{new_movie.uuid.lower()}_detail"
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
                "callback_data": f"{model.__tablename__}_uuid_{selected_movie.uuid.lower()}_trailers"
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
                "text": f"{selected_movie.title} — {selected_movie.rating.value} ⭐", 
                "callback_data": f"{model.__tablename__}_uuid_{selected_movie.uuid.lower()}_reviews"
            })
        
        return inline_buttons

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
class MovieAllReviewsDetailView(templates.DetailView):
    model = models.Movie
    context_name = model.__tablename__
    type = "reviews"
    
    async def info(self, item):
        async def message():
            from db import AsyncSessionLocal
            
            async with AsyncSessionLocal() as session:
                movie = await session.execute(
                    select(models.Movie)
                    .options(joinedload(models.Movie.reviews))
                    .where(models.Movie.id == item.id)
                )
                movie = movie.scalars().first()

                if len(movie.reviews) > 0:
                    text = (
                        f"""✨ {movie.title}'s reviews ✨\n\n"""
                        f"""Curious about what others are saying? Dive into a world of opinions, insights, and reactions to discover how this movie has captured hearts and minds.\n\n"""
                        f"""👇 Choose a review to check:"""
                    )

                    inline_buttons = []

                    for review in movie.reviews:
                        sender = await actions.db.get(models.User, uuid=review.user_uuid)
                        callback_data = f"{models.Review.__tablename__}_uuid_{review.uuid}_detail"
                        inline_buttons.append([InlineKeyboardButton(text=f"⭐{review.rating.value} — @{sender.username}", callback_data=callback_data)])

                    self.markup = InlineKeyboardMarkup(inline_keyboard=inline_buttons)
                else:
                    text = (
                        f"""😕 No reviews found for {movie.title} 😕\n\n"""
                        f"""It seems like no one has shared their thoughts on this movie yet. Be the first to leave a review and let others know your opinion!\n\n"""
                        f"""🔍 Keep exploring or add your own review!"""
                    )
                
                self.text = text
                
                return text
            
        return {"message": await message()}

class MovieAllTrailersDetailView(templates.DetailView):
    model = models.Movie
    context_name = model.__tablename__
    type = "trailers"
    
    async def info(self, item):
        async def message():
            from db import AsyncSessionLocal
            
            async with AsyncSessionLocal() as session:
                movie = await session.execute(
                    select(models.Movie)
                    .options(joinedload(models.Movie.trailers))
                    .where(models.Movie.id == item.id)
                )
                movie = movie.scalars().first()
                
                if len(movie.trailers) > 0:
                    text = (
                        f"""✨ {movie.title}'s trailers ✨\n\n"""
                        f"""Step into a world of captivating stories, breathtaking visuals, and unforgettable emotions. This cinematic journey awaits, and it all begins with a sneak peek.\n\n"""
                        f"""👇 Choose a trailer to watch:"""
                    )
                    
                    inline_buttons = []

                    for trailer in movie.trailers:
                        callback_data = f"{models.Trailer.__tablename__}_uuid_{trailer.uuid}_detail"
                        inline_buttons.append([InlineKeyboardButton(text=f"{trailer.title}", callback_data=callback_data)])

                    self.markup = InlineKeyboardMarkup(inline_keyboard=inline_buttons)
                else:
                    text = (
                        f"""😕 No trailers found for {movie.title} 😕\n\n"""
                        f"""Looks like there are no previews available for this movie right now. Stay tuned for updates, or check out other films to explore more exciting content!\n\n"""
                        f"""🔍 Keep exploring or add a trailer if you have one!"""
                    )
                    
                self.text = text
                
                return text

        return {"message": await message()}

class MovieDetailView(templates.DetailView):
    model = models.Movie
    context_name = model.__tablename__
    type = "detail"

    async def info(self, item):
        async def message():
            country = await actions.db.get(models.Country, uuid=item.country_uuid)
            
            text = (
                f"""🎬 Movie *{item.title}*\n\n"""
                f"""{item.short_description}\n\n"""
                f"""💡 *What Awaits You?*\n\n"""
                f"""{item.description}\n\n"""
                f"""📜 *Details*\n\n"""
                f"""🌍 Country: {country.title}\n"""
                f"""⏱️ Duration: {actions.sec_to_hms(item.duration)}\n"""
                f"""📅 Release date: {item.released_at.strftime("%d %B %Y")}\n"""
                f"""⭐ Rating: {item.rating.value} / 5.0\n\n"""
                f"""🎟 Grab your popcorn and dive into this unforgettable journey! 🍿  """
            )
            
            inline_buttons = []

            inline_buttons.append([InlineKeyboardButton(text="Watch", url=item.url)])
            inline_buttons.append([InlineKeyboardButton(text="Trailers", callback_data=f"{self.model.__tablename__}_uuid_{item.uuid}_{models.Trailer}")])
            inline_buttons.append([InlineKeyboardButton(text="Reviews", callback_data=f"{self.model.__tablename__}_uuid_{item.uuid}_{models.Review.__tablename__}")])
                
            self.markup = InlineKeyboardMarkup(inline_keyboard=inline_buttons)
            self.text = text
            
            return text
            
        return {"message": await message()}
    
class ReviewDetailView(templates.DetailView):
    model = models.Review
    context_name = model.__tablename__
    type = "detail"

    async def info(self, item):
        async def message():
            sender = await actions.db.get(models.User, uuid=item.user_uuid)
            movie = await actions.db.get(models.Movie, uuid=item.movie_uuid)
            
            text = (
                f"""🌟 Review for the movie *{movie.title}* 🌟\n\n"""
                f"""🖋️ Reviewed by @{sender.username}\n"""
                f"""🔥 {item.rating.name.capitalize()} — {item.rating.value} / 5.0 ⭐\n\n"""
                f"""{item.comment}\n\n"""
                f"""⏰ Submitted on {item.created_at.strftime("%d %B %Y")}"""
            )
            
            inline_buttons = []

            inline_buttons.append([InlineKeyboardButton(text="Back", callback_data=f"{models.Movie.__tablename__}_uuid_{movie.uuid}_{models.Review.__tablename__}")])
                
            self.markup = InlineKeyboardMarkup(inline_keyboard=inline_buttons)
            self.text = text
            
            return text
            
        return {"message": await message()}
    
class TrailerDetailView(templates.DetailView):
    model = models.Trailer
    context_name = model.__tablename__
    type = "detail"

    async def info(self, item):
        async def message():
            movie = await actions.db.get(models.Movie, uuid=item.movie_uuid)
            
            text = (
                f"""Trailer for the movie *{movie.title}*\n\n"""
                f"""{item.title}\n\n"""
                f"""*What awaits you?*\n\n"""
                f"""{item.description}\n\n"""
                f"""*Details*\n\n"""
                f"""❤️ Likes: {item.likes}\n"""
                f"""💬 Comments: {item.comments}\n"""
                f"""📅 Release date: {item.created_at.strftime("%d %B %Y")}\n\n"""
                f"""🎬 Get ready for an epic ride — popcorn in hand! 🍿"""
            )
            
            inline_buttons = []

            inline_buttons.append([InlineKeyboardButton(text="Watch", url=item.url)])
            inline_buttons.append([InlineKeyboardButton(text="Back", callback_data=f"{models.Movie.__tablename__}_uuid_{movie.uuid}_{models.Trailer.__tablename__}")])
                
            self.markup = InlineKeyboardMarkup(inline_keyboard=inline_buttons)
            self.text = text
            
            return text
            
        return {"message": await message()}