-- SQLite example requires script

-- Два запроса на выборку для связанных таблиц с условиями и сортировкой

-- Выбор туров с 4-х звезд и выше
SELECT dc.name, ac.name, h.name, date, h.stars
FROM tour
         join departure_city dc on tour.city_id = dc.id
         join hotel h on tour.hotel_id = h.id
         join resort r on h.resort_id = r.id
         join arrival_country ac on r.arrival_country_id = ac.id
WHERE h.stars >= 4;

-- Выбор отелей с 3-х звезд и меньше, сортировка по количеству звезд
SELECT name, stars
FROM hotel
WHERE stars <= 3
ORDER BY stars;


-- Два запроса с группировкой и групповыми функциями

-- Выбор количества туров в 5-и звездочные отели по странам вылета
SELECT dc.name, count(*) as count
FROM departure_city dc
         join tour t on dc.id = t.city_id
         join hotel h on t.hotel_id = h.id
WHERE h.stars = 5
GROUP BY dc.name;


-- Выбор количества типов питания
SELECT meal_type, count(*)
FROM tour
GROUP BY meal_type;


-- Два запроса со вложенными запросами или табличными выражениями

-- Выбор туров с 5-и звездочными отелями
SELECT *
from tour
where hotel_id in (select id from hotel where stars = 5);

-- Выбор туров из городов из которых более 2-х туров в 5-и звездочные отели
SELECT *
from tour
where city_id in (SELECT id
                  from (SELECT dc.id as id, count(*) as count
                        FROM departure_city dc
                                 join tour t on dc.id = t.city_id
                                 join hotel h on t.hotel_id = h.id
                        WHERE h.stars = 5
                        GROUP BY dc.name)
                  where count > 2);

-- Два запроса корректировки данных (обновление, добавление, удаление и пр)
-- Смотреть в файле fixtures.sql


-- Вывести среднюю цену тура на каждый курорт
-- без учета туров с самой большой и самой маленькой ценой