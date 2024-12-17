from . import templates, views, actions, models

class MovieSearchStateView(templates.StateView):
    transitions = [
        {
            "text": (
                "🔍 *Search for Your Favorite Movie!* 🎬\n\n"
                "Welcome to the ultimate movie database! Want to know everything about the latest blockbuster or an old classic? Simply type the *name* of the movie, and we’ll fetch all the juicy details just for you! 🍿🎥\n\n"
                "✨ *How it works?*\n\n"
                "1️⃣ Type the *name of the movie* in the search box below.\n"
                "2️⃣ Press *Search*, and let the magic unfold!\n"
                "3️⃣ Get ready for detailed information like genre, cast, release date, synopsis, and more!\n\n"
                "Start searching and find your next movie! 📲"
            ),
            "field": "text"
        },
    ]
    redirect_to = views.MovieSearchListView

    async def success(self, data):
        typed_text = data["text"]

        async def items():
            model = models.Movie
            found_movies = await actions.db.search(model, field="title", text=typed_text)
            inline_buttons = []
            
            for found_movie in found_movies:
                inline_buttons.append({
                    "text": found_movie.title, 
                    "callback_data": f"{model.__tablename__}_uuid_{found_movie.uuid.lower()}_detail"
                })
                
            return inline_buttons

        async def message():
            found_movies_count = len(await items())
            if found_movies_count > 0:
                text = (
                    f"🎬 Search results for \"\u200B*{typed_text}*\u200B\"\n\n"
                    f"We've found *{found_movies_count} {'movie' if found_movies_count == 1 else 'movies'}* based on your search!\n\n"
                    f"👇 Click on a movie below to get more details:"
                )
            else:
                text = (
                    f"😔 No results found for \"\u200B*{typed_text}*\u200B\"\n\n"
                    f"🔍 Looks like we couldn't find any hidden gems this time!\n\n"
                    f"🎥 *Tips for a Better Search Experience:*\n\n"
                    f"1️⃣ *Be Specific*: Use the full movie title to get accurate results. Avoid abbreviations or partial names.\n"
                    f"2️⃣ *Check Spelling*: Small typos can make a big difference. Double-check your movie name!\n"
                    f"3️⃣ *Try Alternative Titles*: Some movies are known by different names in different regions. Try searching with variations if needed.\n"
                    f"4️⃣ *Avoid Extra Symbols*: Keep your search simple—no need for extra punctuation or characters.\n" 
                    f"5️⃣ *Keep It Short*: Searching by just the main title works best. Adding too many details can confuse the search.\n\n"
                    f"💡 Maybe you'd like to try something else? We're always ready to help!"
                )
            return text

        return {
            "items": await items(),
            "message": await message()
        }