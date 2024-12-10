from . import templates, views, actions, models

class MovieSearchStateView(templates.StateView):
    transitions = [
        {
            "text": (
                "🔍 *Movie Search*\n\n"
                "Enter the movie title or choose a genre to search. 🎬\n\n"
                "*CinemaBot* will help you find information about any movie, including:\n"
                "📅 Release Date\n"
                "⭐ Rating and Reviews\n"
                "🎥 Trailers\n"
                "🎭 Cast\n"
                "📰 News and Updates\n\n"
                "You can either enter just the movie title or use genre filters for more accurate results.\n\n"
                "Enter the movie title or select a genre below!"
            ),
            "field": "text"
        },
    ]
    redirect_to = views.MovieListView

    async def success(self, data):
        typed_text = data["text"]

        async def items():
            model = models.Movie
            found_movies = await actions.db.search(model, field="title", text=typed_text)
            inline_buttons = []
            for found_movie in found_movies:
                inline_buttons.append({
                    "text": found_movie.title, 
                    "callback_data": f"{model.__tablename__}_{found_movie.uuid.lower()}"
                })
            return inline_buttons

        async def message():
            found_movies_count = len(await items())
            if found_movies_count > 0:
                text = (
                    f"🎬 **Search results for** \"\u200B**{typed_text}**\u200B\" **found** {found_movies_count} {'movie' if found_movies_count == 1 else 'movies'}!\n"
                    f"🔍 Here's what we found for you:\n"
                    f"✅ Everything you need to enjoy this great genre!\n\n"
                    f"✨ Each one is a masterpiece worth your attention! 🌟"
                )
            else:
                text = (
                    f"😔 **No results found** for \"\u200B**{typed_text}**\u200B\"!\n\n"
                    f"🔍 We tried to find something interesting for you, but couldn't find anything.\n"
                    f"✨ Try changing your search or check the spelling!\n\n"
                    f"💡 Maybe you'd like to try something else? We're always ready to help!"
                )
            return text

        return {
            "items": await items(),
            "message": await message()
        }