<h4>Реализованная функциональность</h4>
<ul>
    <li>Отображение безбилетников на внутреннем экране транспорта;</li>
    <li>Распознавание лиц;</li>
    <li>Распознавание фигур;</li>
</ul>

<h4>Особенность проекта в следующем:</h4>
<ul>
    <li>Отслеживание передвижения фигур по транспорту;</li>
    <li>Социальный харассмент безбилетников;</li>
</ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Python 3+.</li>
	<li>HTML, CSS, JavaScript, TypeScript.</li>
	<li>SCSS.</li>
	<li>Gulp, Webpack, Babel.</li>
	<li>Vue.</li>
	<li>Git.</li>
	<li>Heroku.</li>

 </ul>

<h4>Демо</h4>
<p>Демо сервиса доступно по адресу: TODO </p>

 
Среда запуска
------------
1) развертывание сервиса производится на debian-like linux (debian 9+);

Установка и запуск
------------
 Сервер
------
Выполните:

```bash
sudo apt-get update
sudo apt-get install -y software-properties-common python3.9 python3-pip

git clone https://github.com/Nikita-Sherstnev/moscow-no-ticket.git
cd moscow-no-ticket/server
pip install venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m app
```

/detect (GET) - endpoint на распознавание изображения

***

 Клиент
------

### Среда запуска

- NodeJS, NPM 14.17.0+ 
- Yarn 1.22.5+

### Установка
```
git clone https://github.com/Nikita-Sherstnev/moscow-no-ticket.git
cd moscow-no-ticket/client
yarn install
```

### Компиляция
```
yarn serve
```

### Сборка
```
yarn build
```

РАЗРАБОТЧИКИ

<h4>Шерстнев Никита Data Science, Backend https://t.me/iewkw </h4>
<h4>Давидович Артем FullStack https://t.me/artyom_d </h4>
<h4>Сандуляк Степан Backend https://t.me/developmc </h4>