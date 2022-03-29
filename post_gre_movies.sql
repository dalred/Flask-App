--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2 (Ubuntu 14.2-1.pgdg20.04+1)
-- Dumped by pg_dump version 14.2 (Ubuntu 14.2-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: director; Type: TABLE; Schema: public; Owner: flaskappuserdb
--

CREATE TABLE public.director (
    id integer NOT NULL,
    name character varying(255)
);


ALTER TABLE public.director OWNER TO flaskappuserdb;

--
-- Name: genre; Type: TABLE; Schema: public; Owner: flaskappuserdb
--

CREATE TABLE public.genre (
    id integer NOT NULL,
    name character varying(255)
);


ALTER TABLE public.genre OWNER TO flaskappuserdb;

--
-- Name: movie; Type: TABLE; Schema: public; Owner: flaskappuserdb
--

CREATE TABLE public.movie (
    id integer NOT NULL,
    title character varying(255),
    description character varying,
    trailer character varying(255),
    year integer,
    rating double precision,
    genre_id integer,
    director_id integer
);


ALTER TABLE public.movie OWNER TO flaskappuserdb;

--
-- Name: users; Type: TABLE; Schema: public; Owner: flaskappuserdb
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying,
    password character varying(255),
    role character varying(5),
    access_token character varying,
    refresh_token character varying
);


ALTER TABLE public.users OWNER TO flaskappuserdb;

--
-- Data for Name: director; Type: TABLE DATA; Schema: public; Owner: flaskappuserdb
--

COPY public.director (id, name) FROM stdin;
1	Тейлор Шеридан
2	Квентин Тарантино
3	Владимир Вайншток
4	Декстер Флетчер
5	Стив Энтин
6	Роб Маршалл
7	Баз Лурман
8	Дэмьен Шазелл
9	Пьетро Антон
10	Джеймс Мэнголд
11	Дени Вильнёв
12	Кирилл Серебренников
13	Рубен Фляйшер
14	Стэнли Кубрик
15	Ричард Келли
16	Пит Доктер
17	Кемп Пауэрс
18	Бибо Бержерон
19	Тоби Генкель
20	Шон Маккормак
\.


--
-- Data for Name: genre; Type: TABLE DATA; Schema: public; Owner: flaskappuserdb
--

COPY public.genre (id, name) FROM stdin;
1	Комедия
2	Семейный
3	Фэнтези
4	Драма
5	Приключения
6	Триллер
7	Фантастика
8	Аниме
9	Документальное
10	Короткометражка
11	Ужасы
12	Боевик
13	Мелодрама
14	Детектив
15	Авторское кино
16	Мультфильм
17	Вестерн
18	Мюзикл
\.


--
-- Data for Name: movie; Type: TABLE DATA; Schema: public; Owner: flaskappuserdb
--

COPY public.movie (id, title, description, trailer, year, rating, genre_id, director_id) FROM stdin;
1	Йеллоустоун	Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»	https://www.youtube.com/watch?v=UKei_d0cbP4	2018	8.6	17	1
2	Омерзительная восьмерка	США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.	https://www.youtube.com/watch?v=lmB9VWm0okU	2015	7.8	4	2
3	Вооружен и очень опасен	События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...	https://www.youtube.com/watch?v=hLA5631F-jo	1978	6	17	3
4	Джанго освобожденный	Эксцентричный охотник за головами, также известный как Дантист, промышляет отстрелом самых опасных преступников. Работенка пыльная, и без надежного помощника ему не обойтись. Но как найти такого и желательно не очень дорогого? Освобождённый им раб по имени Джанго – прекрасная кандидатура. Правда, у нового помощника свои мотивы – кое с чем надо сперва разобраться.	https://www.youtube.com/watch?v=2Dty-zwcPv4	2012	8.4	17	2
5	Рокетмен	История превращения застенчивого парня Реджинальда Дуайта, талантливого музыканта из маленького городка, в суперзвезду и культовую фигуру мировой поп-музыки Элтона Джона.	https://youtu.be/VISiqVeKTq8	2019	7.3	18	4
6	Бурлеск	Али - молодая амбициозная девушка из маленького городка с чудесным голосом, совсем недавно потеряла своих родителей. Теперь никому не нужная, она отправляется в большой город Лос-Анджелес, где устраивается на работу у Тесс, хозяйки ночного клуба «Бурлеск». За короткое время она находит друзей, поклонников и любовь всей своей жизни. Но может ли сказка длиться вечно? Ведь немало людей завидует этой прекрасной танцовщице...	https://www.youtube.com/watch?v=sgOhxneHkiE	2010	6.4	18	5
7	Чикаго	Рокси Харт мечтает о песнях и танцах и о том, как сравняться с самой Велмой Келли, примадонной водевиля. И Рокси действительно оказывается с Велмой в одном положении, когда несколько очень неправильных шагов приводят обеих на скамью подсудимых.	https://www.youtube.com/watch?v=YxzS_LzWdG8	2002	7.2	18	6
8	Мулен Руж	Париж, 1899 год. Знаменитый ночной клуб «Мулен Руж» — это не только дискотека и шикарный бордель, но и место, где, повинуясь неудержимому желанию прочувствовать атмосферу праздника, собираются страждущие приобщиться к красоте, свободе, любви и готовые платить за это наличными.	https://www.youtube.com/watch?v=lpiMCTd87gE	2001	7.6	18	7
9	Одержимость	Эндрю мечтает стать великим. Казалось бы, вот-вот его мечта осуществится. Юношу замечает настоящий гений, дирижер лучшего в стране оркестра. Желание Эндрю добиться успеха быстро становится одержимостью, а безжалостный наставник продолжает подталкивать его все дальше и дальше – за пределы человеческих возможностей. Кто выйдет победителем из этой схватки?	https://www.youtube.com/watch?v=Q9PxDPOo1jw	2013	8.5	4	8
10	Наследие итало-диско	Авторитетный взгляд на историю культового электронного стиля глазами самых известных его представителей и последователей. Увлекательный рассказ о феномене итало-диско и возможность увидеть своими глазами, что творилось на главных танцполах 80-х.	https://www.youtube.com/watch?v=LVdRR6m5OdQ	2017	0	9	9
11	Переступить черту	Юность певца Джонни Кэша была омрачена гибелью его брата и пренебрежительным отношением отца. Военную службу будущий певец проходил в Германии. После свадьбы и рождения дочери он выпустил свой первый хит и вскоре отправился в турне по США вместе с Джерри Ли Льюисом, Элвисом Пресли и Джун Картер, о которой он безнадёжно мечтал целых десять лет.	https://www.youtube.com/watch?v=RnFrrzg1OEQ	2005	7.8	4	10
12	Дюна	Наследник знаменитого дома Атрейдесов Пол отправляется вместе с семьей на одну из самых опасных планет во Вселенной — Арракис. Здесь нет ничего, кроме песка, палящего солнца, гигантских чудовищ и основной причины межгалактических конфликтов — невероятно ценного ресурса, который называется меланж. В результате захвата власти Пол вынужден бежать и скрываться, и это становится началом его эпического путешествия. Враждебный мир Арракиса приготовил для него множество тяжелых испытаний, но только тот, кто готов взглянуть в глаза своему страху, достоин стать избранным.	https://www.youtube.com/watch?v=DOlTmIhEsg0	2021	8.4	7	11
13	Ла-Ла Ленд	Это история любви старлетки, которая между прослушиваниями подает кофе состоявшимся кинозвездам, и фанатичного джазового музыканта, вынужденного подрабатывать в заштатных барах. Но пришедший к влюбленным успех начинает подтачивать их отношения.	https://www.youtube.com/watch?v=lneNCBIXD4I	2016	8	18	8
14	Лето	Рассказ о начале творческого пути Виктора Цоя и группы «Кино», о его взаимоотношениях с Майком Науменко, его женой Натальей и многими, кто был в авангарде рок-движения Ленинграда 1981 года.	https://www.youtube.com/watch?v=TvAbtsQKrHA	2018	7.3	4	12
15	Сияние 	Джек Торренс с женой и сыном приезжает в элегантный отдалённый отель, чтобы работать смотрителем во время мертвого сезона. Торренс здесь раньше никогда не бывал. Или это не совсем так? Ответ лежит во мраке, сотканном из преступного кошмара.	https://www.youtube.com/watch?v=NMSUEhDWXH0	1980	8.4	6	14
16	Веном	Что если в один прекрасный день в тебя вселяется существо-симбиот, которое наделяет тебя сверхчеловеческими способностями? Вот только Веном – симбиот совсем недобрый, и договориться с ним невозможно. Хотя нужно ли договариваться?.. Ведь в какой-то момент ты понимаешь, что быть плохим вовсе не так уж и плохо. Так даже веселее. В мире и так слишком много супергероев! Мы – Веном!	https://www.youtube.com/watch?v=n7GlLxV_Igk	2018	6.7	7	13
17	Донни Дарко	К своим 16 годам старшеклассник Донни уже знает, что такое смерть. После несчастного случая, едва не стоившего ему жизни, Донни открывает в себе способности изменять время и судьбу. Произошедшие с ним перемены пугают его окружение — родителей, сестер, учителей, друзей и любимую девушку.	https://www.youtube.com/watch?v=9H_t5cdszFU	2001	8	7	15
18	Душа	Уже немолодой школьный учитель музыки Джо Гарднер всю жизнь мечтал выступать на сцене в составе джазового ансамбля. Однажды он успешно проходит прослушивание у легендарной саксофонистки и, возвращаясь домой вне себя от счастья, падает в люк и умирает. Теперь у Джо одна дорога — в Великое После, но он сбегает с идущего в вечность эскалатора и случайно попадает в Великое До. Тут новенькие души обретают себя, и у будущих людей зарождаются увлечения, мечты и интересы. Джо становится наставником упрямой души 22, которая уже много веков не может найти свою искру и отправиться на Землю.	https://www.youtube.com/watch?v=vsb8762mE6Q	2020	8.1	16	16
19	Монстр в Париже	Париж. 1910 год. Ужасный монстр, напоминающий гигантское насекомое, нагоняет страх на всю Францию. Застенчивый киномеханик и неутомимый изобретатель начинают охоту на него. В этой погоне они знакомятся со звездой кабаре, сумасшедшим ученым и его умной обезьянкой и, наконец, самим монстром, который оказывается совсем не страшным. Теперь безобидное, как блоха, чудовище ищет у своих новых друзей защиты от вредного начальника городской полиции.	https://www.youtube.com/watch?v=rKsdTuvrF5w	2010	6.1	16	18
20	Упс... Приплыли!	От Великого потопа зверей спас ковчег. Но спустя полгода скитаний они готовы сбежать с него куда угодно. Нервы на пределе. Хищники готовы забыть про запреты и заглядываются на травоядных. Единственное спасение — найти райский остров. Там простор и полно еды. Но даже если он совсем близко, будут ли рады местные такому количеству гостей?	https://www.youtube.com/watch?v=Qjpmysz4x-4	2020	5.9	16	19
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: flaskappuserdb
--

COPY public.users (id, username, password, role, access_token, refresh_token) FROM stdin;
1	vasya	OhW1ATiLz9pqoQR821fGow4bV0UyYZo53ETmuHESeRg=	user	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InZhc3lhIiwicm9sZSI6InVzZXIiLCJpZCI6MSwiZXhwIjoxNjQ4NTU1MDk1fQ.TOFPPnAYZawuc2oTptSDyYsSq1FpJsOTpLDPT593X9w	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InZhc3lhIiwicm9sZSI6InVzZXIiLCJpZCI6MSwiZXhwIjoxNjU5Nzg1Mjk1fQ.agN5x3wZY97yBNDsXEBG9G2ko1bQk2lTmLuKrjA1dTM
2	oleg1	1Bj+q0/dG9Vfq8fHMEsFZFgLgdf4jyDENuKOsVKCHD4=	user	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9sZWcxIiwicm9sZSI6InVzZXIiLCJpZCI6MiwiZXhwIjoxNjQ4NTU1MDk1fQ.uh48Oo3utQ5Mj1z-KyIXGbDlloZVIj7SiPIjpAioDEw	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9sZWcxIiwicm9sZSI6InVzZXIiLCJpZCI6MiwiZXhwIjoxNjU5Nzg1Mjk1fQ.u4PcMBbvVFI6MCvd9fDWlFXybh38TSA6KCSPTnr0b7E
3	oleg	1Bj+q0/dG9Vfq8fHMEsFZFgLgdf4jyDENuKOsVKCHD4=	admin	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9sZWciLCJyb2xlIjoiYWRtaW4iLCJpZCI6MywiZXhwIjoxNjQ4NTU1MDk1fQ.JaS8xObAnyallTrJh2bqIwtwRWeR4vVngwe9Ju6KHLc	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9sZWciLCJyb2xlIjoiYWRtaW4iLCJpZCI6MywiZXhwIjoxNjU5Nzg1Mjk1fQ.WElJ4msxQXDRBBnKHHkVGgyxpczy7l-TJkJKyJR8Rg4
\.


--
-- Name: director director_pkey; Type: CONSTRAINT; Schema: public; Owner: flaskappuserdb
--

ALTER TABLE ONLY public.director
    ADD CONSTRAINT director_pkey PRIMARY KEY (id);


--
-- Name: genre genre_pkey; Type: CONSTRAINT; Schema: public; Owner: flaskappuserdb
--

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_pkey PRIMARY KEY (id);


--
-- Name: movie movie_pkey; Type: CONSTRAINT; Schema: public; Owner: flaskappuserdb
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: flaskappuserdb
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: flaskappuserdb
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: movie movie_director_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: flaskappuserdb
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_director_id_fkey FOREIGN KEY (director_id) REFERENCES public.director(id);


--
-- Name: movie movie_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: flaskappuserdb
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public.genre(id);


--
-- PostgreSQL database dump complete
--

