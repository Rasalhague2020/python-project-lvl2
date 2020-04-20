# Python course - project #2

[![Maintainability](https://api.codeclimate.com/v1/badges/9dcafdf98b720b29c532/maintainability)](https://codeclimate.com/github/Rasalhague2020/python-project-lvl2/maintainability)


This is my second Python project on the Hexlet platform.
See details on [Hexlet site (russian language only)][hex-py1].

The second python project is a simple CLI program that show you difference between two JSON files.

### Installation

First of all you should create virtual enviroment via `venv`
```sh
$ python3 -m venv gendiff_env
```
and than activate this enviroment by
```sh
$ source gendiff_env/bin/activate
```
This will allow you to install package in an isolated location and you can easily delete this package in the future. 
To install the full **gendiff** package, type
```sh
(gendiff_env)$ pip install -i https://test.pypi.org/simple/ Rasalhague2020_brain_games --extra-index-url https://pypi.org/simple/
```
When the package `Rasalhague2020_gendiff` is installed in your virtual enviroment you will be able to run this program using the built-in scripts.

### Running gendiff

To start the **gendiff** program, type
```sh
(gendiff_env)$ gendiff <file1.json> <file2.json>
```

### Video tutorial

The process of installation and using **gendiff**:
[![asciicast](https://asciinema.org/a/K0pZWZK6hOpZLIl3KjGSTWWbi.svg)](https://asciinema.org/a/K0pZWZK6hOpZLIl3KjGSTWWbi)

### Delete package

After using this program and getting all information about files differences that you need, you could easily delete this package just by deleting your virtual enviroment directory.
For instance in our case just type
```sh
(gendiff_env)$ deactivate
```
and than delete `gendiff_env` directory
```sh
$ rm -r gendiff_env/
```


[hex-py1]:<https://ru.hexlet.io/professions/python/projects/50>
