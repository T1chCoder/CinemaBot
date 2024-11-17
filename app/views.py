from . import templates

#Views
class HomeView(templates.TemplateView):
    text = (
        "🎥 *Добро пожаловать в CinemaBot!* 🍿\n\n"
        "CinemaBot — ваш персональный гид по миру кино прямо в Telegram! 🚀\n\n"
        "🌟 *Что может CinemaBot?*\n\n"
        "🔍 *Поиск фильмов*: Узнайте всё о любом фильме — сюжет, актеры, жанр и многое другое.\n"
        "⭐️ *Рецензии и рейтинги*: Читайте отзывы и смотрите рейтинги от популярных сервисов.\n"
        "🎞 *Трейлеры и кадры*: Просматривайте трейлеры и галереи фильмов, которые вы любите.\n"
        "🤖 *Рекомендации*: Получайте персональные подборки фильмов на основе ваших вкусов.\n"
        "🕒 *Расписание кинотеатров*: Находите ближайшие сеансы и покупайте билеты.\n"
        "📰 *Новости кино*: Следите за горячими новостями и премьерами!\n\n"
        "👉 [Добавьте CinemaBot в свой Telegram](https://t.me/CinemaBot)\n"
    )

class MovieSearchView(templates.TemplateView):
    text = (
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
    )

class RecommendedMoviesView(templates.TemplateView):
    text = (
    "🤖 *Рекомендации от CinemaBot* 🎬\n\n"
    "Не можете выбрать, что посмотреть? Не переживайте, CinemaBot поможет вам! 🎉\n\n"
    "На основе ваших предпочтений, вкусов и жанров, бот предложит вам фильмы, которые вы обязательно оцените.\n\n"
    "🌟 *Как это работает?*\n\n"
    "1. Ответьте на несколько вопросов, чтобы настроить рекомендации.\n"
    "2. CinemaBot предложит вам фильмы, которые могут вам понравиться.\n"
    "3. Вы можете просмотреть подробности о каждом фильме: трейлер, рейтинг, отзывы и многое другое.\n\n"
    "🎥 Начните получать персонализированные рекомендации прямо сейчас!"
)

class NewMoviesView(templates.TemplateView):
    text = (
    "✨ *Новинки кино* 🎬\n\n"
    "Ищете самые свежие фильмы? CinemaBot поможет вам узнать, что только что вышло в кино! 🍿\n\n"
    "🔥 *Что вас ждет?*\n\n"
    "📅 Список самых свежих фильмов, которые только что появились в кинотеатрах.\n"
    "⭐ Рейтинг и отзывы зрителей и критиков.\n"
    "🎥 Трейлеры новинок — будьте в курсе самых ожидаемых фильмов!\n"
    "📰 Новости и подробности о премьерах.\n\n"
    "Нажмите ниже, чтобы увидеть новинки и выбрать фильм для просмотра!"
)

class MovieTrailersView(templates.TemplateView):
    text = (
    "🎥 *Трейлеры фильмов* 🍿\n\n"
    "Хотите увидеть, что вас ждет на экране? CinemaBot поможет вам просмотреть самые актуальные трейлеры! 🎬\n\n"
    "🌟 *Что вас ждет?*\n\n"
    "📹 Просмотр трейлеров самых ожидаемых фильмов.\n"
    "🎞 Уникальные кадры и сцены из фильмов, которые скоро выйдут.\n"
    "🔥 Погружение в атмосферу будущих хитов с помощью трейлеров.\n\n"
    "Выберите фильм, чтобы увидеть его трейлер, или просто наслаждайтесь подборкой!"
)

class MovieRatingsView(templates.TemplateView):
    text = (
    "🌟 *Рейтинг фильмов* 🎬\n\n"
    "Хотите узнать, как оценивают фильмы зрители и критики? CinemaBot подскажет вам, какие фильмы заслуживают вашего внимания! 🍿\n\n"
    "⭐ *Что вас ждет?*\n\n"
    "📊 Подробные рейтинги фильмов на популярных платформах, таких как IMDb, Rotten Tomatoes и других.\n"
    "🎥 Рецензии и оценки критиков.\n"
    "👥 Рейтинг зрителей — как оценивают фильм обычные зрители.\n\n"
    "Выберите фильм, чтобы увидеть его рейтинг, или просто исследуйте лучшие фильмы по рейтингам!"
)

class TheatreSessionsView(templates.TemplateView):
    text = (
    "🎬 *Сеансы кинотеатров* 🍿\n\n"
    "Хотите узнать, когда можно посмотреть свой любимый фильм? CinemaBot поможет вам найти ближайшие сеансы! 🕒\n\n"
    "🌟 *Что вас ждет?*\n\n"
    "📅 Расписание сеансов в ближайших кинотеатрах.\n"
    "🎥 Информация о фильмах, которые идут в кинотеатре в данный момент.\n"
    "📍 Поиск сеансов по вашему местоположению.\n"
    "🎫 Возможность забронировать билеты на выбранный сеанс.\n\n"
    "Введите название фильма или выберите кинотеатр, чтобы увидеть доступные сеансы."
)

class MovieNewsView(templates.TemplateView):
    text = (
    "📰 *Новости кино* 🎬\n\n"
    "Хотите быть в курсе всех новинок, премьеров и слухов из мира кино? CinemaBot собрал для вас самые горячие новости! 🌟\n\n"
    "🔥 *Что вас ждет?*\n\n"
    "📅 Последние новости о фильмах и сериалах.\n"
    "🎞 Анонсы предстоящих премьер и событий.\n"
    "🎬 Интервью с актерами и режиссерами.\n"
    "📝 Обзоры и новости индустрии кино.\n\n"
    "Выберите новость, чтобы узнать подробности, или просто следите за свежими обновлениями!"
)

class HelpView(templates.TemplateView):
    text = (
    "❓ *Помощь* 📝\n\n"
    "Вы не знаете, как использовать CinemaBot? Не переживайте, мы вам поможем! 🚀\n\n"
    "🎬 *Что может CinemaBot?*\n\n"
    "1. 🔍 *Поиск фильмов* — узнайте подробную информацию о любых фильмах.\n"
    "2. ⭐️ *Рейтинги и рецензии* — читайте отзывы зрителей и критиков.\n"
    "3. 🎞 *Трейлеры* — смотрите трейлеры самых ожидаемых фильмов.\n"
    "4. 🕒 *Сеансы кинотеатров* — найдите ближайшие сеансы и купите билеты.\n"
    "5. 📰 *Новости кино* — следите за свежими новинками и анонсами.\n"
    "6. 🤖 *Рекомендации* — получайте персональные рекомендации по фильмам.\n\n"
    "🛠 *Как начать?*\n\n"
    "1. Используйте команды или кнопки в меню для навигации по боту.\n"
    "2. Введите название фильма или выберите одну из категорий для поиска.\n"
    "3. Следите за новинками, рейтингами и новостями в мире кино.\n\n"
    "Если у вас есть вопросы или предложения, не стесняйтесь обратиться к нам! 📩"
)

#ReplyButtons
class SearchReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🔍 Поиск фильма"
    pages = [HomeView]
    redirect_to = MovieSearchView

class RecommendedMoviesReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🎬 Рекомендации"
    pages = [HomeView]
    redirect_to = RecommendedMoviesView

class NewMoviesReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "✨ Новинки"
    pages = [HomeView]
    redirect_to = NewMoviesView

class MovieTrailersReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🎥 Трейлеры"
    pages = [HomeView]
    redirect_to = MovieTrailersView

class MovieRatingsReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🌟 Рейтинг фильмов"
    pages = [HomeView]
    redirect_to = MovieRatingsView

class MovieNewsReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "📰 Новости кино"
    pages = [HomeView]
    redirect_to = MovieNewsView

class TheatreSessionsReplyButtonView(templates.ReplyKeyboardButtonView):
    text = "🎫 Сеансы кинотеатров"
    pages = [HomeView]
    redirect_to = TheatreSessionsView

#Commands
class StartCommandView(templates.CommandView):
    text = "start"
    redirect_to = HomeView

class HelpCommandView(templates.CommandView):
    text = "help"
    redirect_to = HelpView

class MovieSearchCommandView(templates.CommandView):
    text = "search"
    redirect_to = MovieSearchView

class RecommendedMoviesCommandView(templates.CommandView):
    text = "recommendations"
    redirect_to = MovieSearchView

class NewMoviesCommandView(templates.CommandView):
    text = "releases"
    redirect_to = NewMoviesView

class MovieTrailersCommandView(templates.CommandView):
    text = "releases"
    redirect_to = MovieTrailersView

class MovieRatingsCommandView(templates.CommandView):
    text = "ratings"
    redirect_to = MovieRatingsView

class TheatreSessionsCommandView(templates.CommandView):
    text = "showtimes"
    redirect_to = TheatreSessionsView

class MovieNewsCommandView(templates.CommandView):
    text = "news"
    redirect_to = MovieNewsView