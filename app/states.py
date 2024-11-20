from . import templates, views

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
    ), "field": "name"},
    ]
    redirect_to = views.MovieListView

    def success(self, data): 
        def items():
            return [{"text": "Привет", "callback_data": "privet"}]

        def message():
            return "Выбери"

        return {"items": items(), "message": message()}