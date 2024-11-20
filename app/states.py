from . import templates, views, actions, models

class MovieSearchStateView(templates.StateView):
    transitions = [
        {"text": (
        "🔍 *Поиск фильма*\n\n"
        "Введите название фильма или выберите жанр для поиска. 🎬\n\n"
        "*CinemaBot* поможет вам найти информацию о любых фильмах, включая:\n"
        "📅 Дату выхода\n"
        "⭐ Рейтинг и рецензии\n"
        "🎥 Трейлеры\n"
        "🎭 Состав актеров\n"
        "📰 Новости и обновления\n\n"
        "Вы можете ввести только название фильма или использовать фильтры по жанрам для более точных результатов.\n\n"
        "Введите название фильма или выберите жанр ниже!"
    ), "field": "text"},
    ]
    redirect_to = views.MovieListView

    async def success(self, data): 
        typed_text = data["text"]
        
        async def items():
            found_movies = await actions.db.search(models.Movie, field="title", text=typed_text)
            inline_buttons = []
            for found_movie in found_movies:
                inline_buttons.append({"text": found_movie.title, "callback_data": f"movie_{found_movie.uuid.lower()}"})
            return inline_buttons

        async def message():
            found_movies_count = len(await items())
            if found_movies_count > 0:
                text = (
                    f"🎬 **По запросу** \"\u200B**{typed_text}**\u200B\" **найдено** {found_movies_count} {'кинофильм' if found_movies_count == 1 else 'кинофильмов'}!\n"
                    f"🔍 Вот что мы нашли для вас:\n"
                    f"✅ Всё, что нужно, чтобы провести время с этим великолепным жанром!\n\n"
                    f"✨ Каждое из них — шедевр, который стоит вашего внимания! 🌟"
                    )
            else:
                text = (
                    f"😔 **По запросу** \"\u200B**{typed_text}**\u200B\" **ничего не найдено!**\n\n"
                    f"🔍 Мы постарались найти для вас что-то поинтереснее, но ничего не нашли.\n"
                    f"✨ Попробуйте изменить запрос или проверьте орфографию!\n"
                    f"💡 Может быть, хотите попробовать что-то другое? Мы всегда готовы помочь!"
                    )
            return text

        return {"items": await items(), "message": await message()}