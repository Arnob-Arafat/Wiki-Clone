# Wiki
 
A lightweight Wikipedia-style encyclopedia built with **Django**. Articles are written in Markdown, stored as plain `.md` files on disk, and rendered to HTML on request.
 
This is my implementation of **Project 1: Wiki** from [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/).
 
---
 
## Features
 
| Feature | Behavior |
| --- | --- |
| **Entry page** | `/wiki/TITLE` loads the entry with `util.get_entry()`, converts its Markdown to HTML with `markdown2`, and displays it under the entry's name. If the entry doesn't exist, a custom "not found" page is shown. |
| **Index page** | Lists every entry; each name links directly to its entry page. |
| **Search** | The sidebar search box submits a `GET` request. A case-insensitive exact match redirects to that entry. Otherwise a results page lists every entry whose title contains the query as a substring (searching `ytho` finds `Python`), and each result links to its entry. |
| **New page** | "Create New Page" in the sidebar opens a form with a title field and a `textarea` for Markdown content. The title is checked against existing entries case-insensitively. If one exists, an error message is shown and nothing is saved. Otherwise the entry is written to disk and you are redirected to its page. |
| **Edit page** | Each entry page links to an edit form whose `textarea` is pre-filled with the entry's current Markdown. Saving overwrites the file and redirects back to the entry. |
| **Random page** | "Random Page" in the sidebar redirects to a randomly chosen entry using `random.choice()`. |
 
---
 
## Getting Started
 
**Requirements:** Python 3.8+
 
```bash
# 1. Clone the repository
git clone <your-repository-url>
cd wiki
 
# 2. Install dependencies
pip install django markdown2
 
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
│   ├── views.py                   # index, entry, search, newpage, randompage, edit
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
 
Each view in `encyclopedia/views.py` maps to one feature:
 
| View | Description |
| --- | --- |
| `index` | Renders all titles from `util.list_entries()` as links. |
| `entry` | Fetches the Markdown with `util.get_entry()`. Returns the not-found page if it is `None`; otherwise converts to HTML with `markdown2` and renders `entry.html`. |
| `search` | Validates the query with a Django form, redirects on an exact case-insensitive title match, and otherwise renders `search_results.html` with every title containing the query. |
| `newpage` | On `GET`, shows the form. On `POST`, rejects duplicate titles (case-insensitive) or saves the entry with `util.save_entry()` and redirects to it. |
| `randompage` | Redirects to a random title from `util.list_entries()`. |
| `edit` | On `GET`, pre-fills the form with the current Markdown. On `POST`, saves the new content and redirects to the entry. |
 
Entries are plain files, so no database is needed. To add one manually, drop a Markdown file named after the title into `entries/` (for example `entries/Flask.md`) and it will appear on the index page.
 
---
 
## Acknowledgements
 
This project was built as part of [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/), taught by **Brian Yu** and **David J. Malan** at Harvard University. The project specification and starter code (including `util.py`, the base layout, and the initial project setup) are provided by CS50.
 
---
 
## Built With
 
- [Django](https://www.djangoproject.com/): web framework
- [markdown2](https://github.com/trentm/python-markdown2): Markdown-to-HTML conversion
