# Wiki
 
A lightweight Wikipedia-style encyclopedia built with **Django**. Articles are written in Markdown, stored as plain `.md` files on disk, and rendered to HTML on request.
 
This is my implementation of **Project 1: Wiki** from [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/).
 
---
 
## Features
 
| Feature | What it does |
| --- | --- |
| **View entries** | `/wiki/<TITLE>` converts the entry's Markdown to HTML with `markdown2`. Missing entries show a custom 404 page. |
| **Index page** | Lists every available entry as a link. |
| **Search** | An exact match redirects straight to the entry. A partial match shows a results page listing every entry whose title contains the query. |
| **Create page** | Write a new entry in Markdown. Titles are compared case-insensitively, so you can't create a duplicate; if one exists, an error message is shown instead. |
| **Edit page** | Opens the entry's raw Markdown in a textarea. Saving overwrites the file and returns you to the rendered page. |
| **Random page** | Takes you to a randomly chosen entry. |
 
---
 
## Getting Started
 
**Requirements:** Python 3.8+
 
```bash
# 1. Clone the repository
git clone <your-repository-url>
cd wiki
 
# 2. Install dependencies
pip3 install django markdown2
 
# 3. Run the development server
python manage.py runserver
```
 
Then open <http://127.0.0.1:8000/> in your browser.
 
---
 
## Project Structure
 
```text
wiki/
├── manage.py
├── wiki/                          # Project configuration
│   ├── settings.py
│   └── urls.py                    # Includes the encyclopedia app's URLs
│
├── encyclopedia/                  # Main app
│   ├── views.py                   # Request handling for all pages
│   ├── urls.py                    # App routes
│   ├── util.py                    # list_entries, get_entry, save_entry
│   ├── static/encyclopedia/
│   │   ├── styles.css             # Layout and sidebar styling
│   │   └── images/                # Image used on the 404 page
│   └── templates/encyclopedia/
│       ├── layout.html            # Base template: sidebar, search bar, nav links
│       ├── index.html             # List of all entries
│       ├── entry.html             # Rendered entry
│       ├── edit.html              # Edit form
│       ├── newpage.html           # New-entry form
│       ├── search_results.html    # Partial-match results
│       └── notfound.html          # Custom 404 page
│
└── entries/                       # Markdown source files (one per article)
```
 
---
 
## How It Works
 
- **Storage:** Each article is a Markdown file in `entries/`. The helpers in `util.py` read, list, and write these files, so no database is needed.
- **Rendering:** `views.py` loads an entry with `util.get_entry()` and converts it to HTML with `markdown2` before passing it to `entry.html`.
- **Search:** The search bar submits a `GET` request. The view first checks for an exact (case-insensitive) title match, then falls back to a substring search.
- **Create and edit:** Both use `POST` forms. New entries are saved with `util.save_entry()`; edits overwrite the existing file and redirect to the updated page.
- **Random:** `random.choice()` picks a title from `util.list_entries()`.
---
 
## Adding Entries Manually
 
Drop a Markdown file named after the article title into `entries/` (for example, `entries/Flask.md`) and it will appear on the index page automatically.
 
---
 
## Built With
 
- [Django](https://www.djangoproject.com/): web framework
- [markdown2](https://github.com/trentm/python-markdown2): Markdown-to-HTML conversion
