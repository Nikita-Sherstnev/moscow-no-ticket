<h4>Реализованная функциональность</h4>
<ul>
    <li>Отображение безбилетников на внутреннем экране транспорта;</li>
    <li>Распознавание лиц;</li>
    <li>Распознавание фигур;</li>
    <li>Распознавание терминалов оплаты;</li>
</ul>

<h4>Особенность проекта в следующем:</h4>
<ul>
    <li>Отпределение безбилетников согласно пересечению фигуры человека и терминала оплаты. Проверка прохождения оплаты;</li>
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
conda env create -f environment.yml
conda activate no-ticket
python -m app
```

/detect (GET) - endpoint на распознавание лиц на изображении.

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

## Разработчики

<h4>Шерстнев Никита - Data Science, Backend https://t.me/iewkw</h4>
<h4>Давидович Артем - FullStack https://t.me/artyom_d </h4>
<h4>Сандуляк Степан - Backend https://t.me/developmc </h4>