
# Overview

A friend has a YouTube channel, and wants to understand which themes get more attention, so he can make more videos on them.

# Task

    * Create a simple Pyramid app using Mongo as the back-end.
    * On the home page I can list and create videos. Each video has a name and a theme (like "Music").
    * On each video I can click buttons to add thumbs up or thumbs down. I can thumbs up and thumbs down each video multiple times. It should show total  thumbs up & thumbs down next to each video.
    * On another page, it lists themes, sorted by highest score. The score for a theme is the sum of thumbs_up - (thumbs_down/2) for each video in the theme. The scores for each theme should be visible.

# Deliverable

A working Pyramid project that uses Mongo for the database. I should be able to start mongo, start the project, and test the functionality above.

** Observation:** This project was made with Django and Sqlite3.

## How to run


* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/Herbetypaulo/NewProject.git
cd NewProject
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate

```