# Task
Реализовать расширяемое приложение.

Требования к коду: минимум 3 класса, минимум 1 раз использовать lambda-функции и декораторы.

Расширение функционала приложения не должно требовать от пользователя вмешательства в код (aka система плагинов).

Срок выполнения: 1 неделя.

# Completed task

Application composed of 3 base files:
- main.py - Main file of application, entry point
- imodule.py - Contains abstract interface of module
- class_name_decorator.py - Contains class decorator, that adds name of class as attrubute **name** to class itself


And 3 module files in **modules** folder:
- cat.py
- echo.py
- ps.py

That duplicate functions of bash with same names

New modules have to be inherited of IModule class and added to **modules** dir
