# the-midnight-times

This is a Django-based web application that allows users to search for news articles from around the world based on keywords. Users can also view the results of their previous searches.

## Prerequisites

- Python 3.x
- pip
- virtualenv (optional, but recommended)

  # Install virtualenv if not already installed

  pip install virtualenv

  # Create a virtual environment (replace 'venv' with your preferred name)

  virtualenv venv

  # Activate the virtual environment

  # On Windows:

  venv\Scripts\activate

  # On macOS and Linux:

  source venv/bin/activate

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/akshay-toshniwal/news-search-app.git
   cd news-search-app
   ```

2. Install Django and project dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Migrate the database:

   ```
   python manage.py migrate
   ```

4. Run the development server:

   ```
   python manage.py runserver
   ```

5. Access the application in your web browser at http://localhost:8000/
