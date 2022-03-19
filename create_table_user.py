from dao.model.user import User
from setup_db import db
import base64
import datetime, calendar, jwt, hashlib
from helpers.constants import SECRET_HERE as secret, PWD_HASH_ITERATIONS, algo
from dao.model.director import Director
from dao.model.movie import Movie
from dao.model.genre import Genre

def make_user_password_hash(password):
    return base64.b64encode(hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        secret,
        PWD_HASH_ITERATIONS
    )).decode('utf-8')

def create_tokens(data):
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, secret, algorithm=algo)
    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    data["exp"] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(data, secret, algorithm=algo)
    tokens = {"access_token": access_token, "refresh_token": refresh_token}
    return tokens

def create_table_user():
    db.drop_all()
    db.create_all()
    data_users = {
        "user": [{'username': 'vasya', 'password': 'my_little_pony', 'role': 'user'},
                  {'username': 'oleg1', 'password': 'qwerty', 'role': 'user'},
                  {'username': 'oleg', 'password': 'qwerty', 'role': 'admin'}]
    }

    users = []
    for k, item in enumerate(data_users["user"], 1):
        data = {
            "username": item['username'],
            "role": item['role'],
            "id": k
        }
        tokens = create_tokens(data)
        user = User(username=item['username'],
                    password=make_user_password_hash(item['password']),
                    role=item['role'],
                    access_token=tokens["access_token"],
                    refresh_token=tokens["refresh_token"])
        users.append(user)

    with db.session.begin():
        db.session.add_all(users)
        db.session.commit()

    data = {
        "movies": [{
            "title": "Йеллоустоун",
            "description": "Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
            "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
            "year": 2018,
            "rating": 8.6,
            "genre_id": 17,
            "director_id": 1,
            "pk": 1
        }, {
            "title": "Омерзительная восьмерка",
            "description": "США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.",
            "trailer": "https://www.youtube.com/watch?v=lmB9VWm0okU",
            "year": 2015,
            "rating": 7.8,
            "genre_id": 4,
            "director_id": 2,
            "pk": 2
        }, {
            "title": "Вооружен и очень опасен",
            "description": "События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...",
            "trailer": "https://www.youtube.com/watch?v=hLA5631F-jo",
            "year": 1978,
            "rating": 6,
            "genre_id": 17,
            "director_id": 3,
            "pk": 3
        }, {
            "title": "Джанго освобожденный",
            "description": "Эксцентричный охотник за головами, также известный как Дантист, промышляет отстрелом самых опасных преступников. Работенка пыльная, и без надежного помощника ему не обойтись. Но как найти такого и желательно не очень дорогого? Освобождённый им раб по имени Джанго – прекрасная кандидатура. Правда, у нового помощника свои мотивы – кое с чем надо сперва разобраться.",
            "trailer": "https://www.youtube.com/watch?v=2Dty-zwcPv4",
            "year": 2012,
            "rating": 8.4,
            "genre_id": 17,
            "director_id": 2,
            "pk": 4
        }, {
            "title": "Рокетмен",
            "description": "История превращения застенчивого парня Реджинальда Дуайта, талантливого музыканта из маленького городка, в суперзвезду и культовую фигуру мировой поп-музыки Элтона Джона.",
            "trailer": "https://youtu.be/VISiqVeKTq8",
            "year": 2019,
            "rating": 7.3,
            "genre_id": 18,
            "director_id": 4,
            "pk": 5
        }, {
            "title": "Бурлеск",
            "description": "Али - молодая амбициозная девушка из маленького городка с чудесным голосом, совсем недавно потеряла своих родителей. Теперь никому не нужная, она отправляется в большой город Лос-Анджелес, где устраивается на работу у Тесс, хозяйки ночного клуба «Бурлеск». За короткое время она находит друзей, поклонников и любовь всей своей жизни. Но может ли сказка длиться вечно? Ведь немало людей завидует этой прекрасной танцовщице...",
            "trailer": "https://www.youtube.com/watch?v=sgOhxneHkiE",
            "year": 2010,
            "rating": 6.4,
            "genre_id": 18,
            "director_id": 5,
            "pk": 6
        }, {
            "title": "Чикаго",
            "description": "Рокси Харт мечтает о песнях и танцах и о том, как сравняться с самой Велмой Келли, примадонной водевиля. И Рокси действительно оказывается с Велмой в одном положении, когда несколько очень неправильных шагов приводят обеих на скамью подсудимых.",
            "trailer": "https://www.youtube.com/watch?v=YxzS_LzWdG8",
            "year": 2002,
            "rating": 7.2,
            "genre_id": 18,
            "director_id": 6,
            "pk": 7
        }, {
            "title": "Мулен Руж",
            "description": "Париж, 1899 год. Знаменитый ночной клуб «Мулен Руж» — это не только дискотека и шикарный бордель, но и место, где, повинуясь неудержимому желанию прочувствовать атмосферу праздника, собираются страждущие приобщиться к красоте, свободе, любви и готовые платить за это наличными.",
            "trailer": "https://www.youtube.com/watch?v=lpiMCTd87gE",
            "year": 2001,
            "rating": 7.6,
            "genre_id": 18,
            "director_id": 7,
            "pk": 8
        }, {
            "title": "Одержимость",
            "description": "Эндрю мечтает стать великим. Казалось бы, вот-вот его мечта осуществится. Юношу замечает настоящий гений, дирижер лучшего в стране оркестра. Желание Эндрю добиться успеха быстро становится одержимостью, а безжалостный наставник продолжает подталкивать его все дальше и дальше – за пределы человеческих возможностей. Кто выйдет победителем из этой схватки?",
            "trailer": "https://www.youtube.com/watch?v=Q9PxDPOo1jw",
            "year": 2013,
            "rating": 8.5,
            "genre_id": 4,
            "director_id": 8,
            "pk": 9
        }, {
            "title": "Наследие итало-диско",
            "description": "Авторитетный взгляд на историю культового электронного стиля глазами самых известных его представителей и последователей. Увлекательный рассказ о феномене итало-диско и возможность увидеть своими глазами, что творилось на главных танцполах 80-х.",
            "trailer": "https://www.youtube.com/watch?v=LVdRR6m5OdQ",
            "year": 2017,
            "rating": 0,
            "genre_id": 9,
            "director_id": 9,
            "pk": 10
        }, {
            "title": "Переступить черту",
            "description": "Юность певца Джонни Кэша была омрачена гибелью его брата и пренебрежительным отношением отца. Военную службу будущий певец проходил в Германии. После свадьбы и рождения дочери он выпустил свой первый хит и вскоре отправился в турне по США вместе с Джерри Ли Льюисом, Элвисом Пресли и Джун Картер, о которой он безнадёжно мечтал целых десять лет.",
            "trailer": "https://www.youtube.com/watch?v=RnFrrzg1OEQ",
            "year": 2005,
            "rating": 7.8,
            "genre_id": 4,
            "director_id": 10,
            "pk": 11
        }, {
            "title": "Дюна",
            "description": "Наследник знаменитого дома Атрейдесов Пол отправляется вместе с семьей на одну из самых опасных планет во Вселенной — Арракис. Здесь нет ничего, кроме песка, палящего солнца, гигантских чудовищ и основной причины межгалактических конфликтов — невероятно ценного ресурса, который называется меланж. В результате захвата власти Пол вынужден бежать и скрываться, и это становится началом его эпического путешествия. Враждебный мир Арракиса приготовил для него множество тяжелых испытаний, но только тот, кто готов взглянуть в глаза своему страху, достоин стать избранным.",
            "trailer": "https://www.youtube.com/watch?v=DOlTmIhEsg0",
            "year": 2021,
            "rating": 8.4,
            "genre_id": 7,
            "director_id": 11,
            "pk": 12
        }, {
            "title": "Ла-Ла Ленд",
            "description": "Это история любви старлетки, которая между прослушиваниями подает кофе состоявшимся кинозвездам, и фанатичного джазового музыканта, вынужденного подрабатывать в заштатных барах. Но пришедший к влюбленным успех начинает подтачивать их отношения.",
            "trailer": "https://www.youtube.com/watch?v=lneNCBIXD4I",
            "year": 2016,
            "rating": 8,
            "genre_id": 18,
            "director_id": 8,
            "pk": 13
        }, {
            "title": "Лето",
            "description": "Рассказ о начале творческого пути Виктора Цоя и группы «Кино», о его взаимоотношениях с Майком Науменко, его женой Натальей и многими, кто был в авангарде рок-движения Ленинграда 1981 года.",
            "trailer": "https://www.youtube.com/watch?v=TvAbtsQKrHA",
            "year": 2018,
            "rating": 7.3,
            "genre_id": 4,
            "director_id": 12,
            "pk": 14
        }, {
            "title": "Сияние ",
            "description": "Джек Торренс с женой и сыном приезжает в элегантный отдалённый отель, чтобы работать смотрителем во время мертвого сезона. Торренс здесь раньше никогда не бывал. Или это не совсем так? Ответ лежит во мраке, сотканном из преступного кошмара.",
            "trailer": "https://www.youtube.com/watch?v=NMSUEhDWXH0",
            "year": 1980,
            "rating": 8.4,
            "genre_id": 6,
            "director_id": 14,
            "pk": 15
        }, {
            "title": "Веном",
            "description": "Что если в один прекрасный день в тебя вселяется существо-симбиот, которое наделяет тебя сверхчеловеческими способностями? Вот только Веном – симбиот совсем недобрый, и договориться с ним невозможно. Хотя нужно ли договариваться?.. Ведь в какой-то момент ты понимаешь, что быть плохим вовсе не так уж и плохо. Так даже веселее. В мире и так слишком много супергероев! Мы – Веном!",
            "trailer": "https://www.youtube.com/watch?v=n7GlLxV_Igk",
            "year": 2018,
            "rating": 6.7,
            "genre_id": 7,
            "director_id": 13,
            "pk": 16
        }, {
            "title": "Донни Дарко",
            "description": "К своим 16 годам старшеклассник Донни уже знает, что такое смерть. После несчастного случая, едва не стоившего ему жизни, Донни открывает в себе способности изменять время и судьбу. Произошедшие с ним перемены пугают его окружение — родителей, сестер, учителей, друзей и любимую девушку.",
            "trailer": "https://www.youtube.com/watch?v=9H_t5cdszFU",
            "year": 2001,
            "rating": 8,
            "genre_id": 7,
            "director_id": 15,
            "pk": 17
        }, {
            "title": "Душа",
            "description": "Уже немолодой школьный учитель музыки Джо Гарднер всю жизнь мечтал выступать на сцене в составе джазового ансамбля. Однажды он успешно проходит прослушивание у легендарной саксофонистки и, возвращаясь домой вне себя от счастья, падает в люк и умирает. Теперь у Джо одна дорога — в Великое После, но он сбегает с идущего в вечность эскалатора и случайно попадает в Великое До. Тут новенькие души обретают себя, и у будущих людей зарождаются увлечения, мечты и интересы. Джо становится наставником упрямой души 22, которая уже много веков не может найти свою искру и отправиться на Землю.",
            "trailer": "https://www.youtube.com/watch?v=vsb8762mE6Q",
            "year": 2020,
            "rating": 8.1,
            "genre_id": 16,
            "director_id": 16,
            "pk": 18
        }, {
            "title": "Монстр в Париже",
            "description": "Париж. 1910 год. Ужасный монстр, напоминающий гигантское насекомое, нагоняет страх на всю Францию. Застенчивый киномеханик и неутомимый изобретатель начинают охоту на него. В этой погоне они знакомятся со звездой кабаре, сумасшедшим ученым и его умной обезьянкой и, наконец, самим монстром, который оказывается совсем не страшным. Теперь безобидное, как блоха, чудовище ищет у своих новых друзей защиты от вредного начальника городской полиции.",
            "trailer": "https://www.youtube.com/watch?v=rKsdTuvrF5w",
            "year": 2010,
            "rating": 6.1,
            "genre_id": 16,
            "director_id": 18,
            "pk": 19
        }, {
            "title": "Упс... Приплыли!",
            "description": "От Великого потопа зверей спас ковчег. Но спустя полгода скитаний они готовы сбежать с него куда угодно. Нервы на пределе. Хищники готовы забыть про запреты и заглядываются на травоядных. Единственное спасение — найти райский остров. Там простор и полно еды. Но даже если он совсем близко, будут ли рады местные такому количеству гостей?",
            "trailer": "https://www.youtube.com/watch?v=Qjpmysz4x-4",
            "year": 2020,
            "rating": 5.9,
            "genre_id": 16,
            "director_id": 19,
            "pk": 20
        }],
        "directors": [
            {"name": "Тейлор Шеридан", "pk": 1}, {"name": "Квентин Тарантино", "pk": 2},
            {"name": "Владимир Вайншток", "pk": 3}, {"name": "Декстер Флетчер", "pk": 4},
            {"name": "Стив Энтин", "pk": 5}, {"name": "Роб Маршалл", "pk": 6}, {"name": "Баз Лурман", "pk": 7},
            {"name": "Дэмьен Шазелл", "pk": 8}, {"name": "Пьетро Антон", "pk": 9},
            {"name": "Джеймс Мэнголд", "pk": 10}, {"name": "Дени Вильнёв", "pk": 11},
            {"name": "Кирилл Серебренников", "pk": 12}, {"name": "Рубен Фляйшер", "pk": 13},
            {"name": "Стэнли Кубрик", "pk": 14}, {"name": "Ричард Келли", "pk": 15},
            {"name": "Пит Доктер", "pk": 16}, {"name": "Кемп Пауэрс", "pk": 17},
            {"name": "Бибо Бержерон", "pk": 18}, {"name": "Тоби Генкель", "pk": 19},
            {"name": "Шон Маккормак", "pk": 20}],
        "genres": [
            {"name": "Комедия", "pk": 1}, {"name": "Семейный", "pk": 2}, {"name": "Фэнтези", "pk": 3},
            {"name": "Драма", "pk": 4}, {"name": "Приключения", "pk": 5}, {"name": "Триллер", "pk": 6},
            {"name": "Фантастика", "pk": 7}, {"name": "Аниме", "pk": 8}, {"name": "Документальное", "pk": 9},
            {"name": "Короткометражка", "pk": 10}, {"name": "Ужасы", "pk": 11}, {"name": "Боевик", "pk": 12},
            {"name": "Мелодрама", "pk": 13}, {"name": "Детектив", "pk": 14}, {"name": "Авторское кино", "pk": 15},
            {"name": "Мультфильм", "pk": 16}, {"name": "Вестерн", "pk": 17}, {"name": "Мюзикл", "pk": 18}],
    }
    # -------------------------------------------------------

    for movie in data["movies"]:
        m = Movie(
            id=movie["pk"],
            title=movie["title"],
            description=movie["description"],
            trailer=movie["trailer"],
            year=movie["year"],
            rating=movie["rating"],
            genre_id=movie["genre_id"],
            director_id=movie["director_id"],
        )
        with db.session.begin():
            db.session.add(m)

    for director in data["directors"]:
        d = Director(
            id=director["pk"],
            name=director["name"],
        )
        with db.session.begin():
            db.session.add(d)

    for genre in data["genres"]:
        d = Genre(
            id=genre["pk"],
            name=genre["name"],
        )
        with db.session.begin():
            db.session.add(d)
            db.session.commit()

