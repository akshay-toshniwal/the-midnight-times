# the-midnight-times

This is a Django-based web application that allows users to search for news articles from around the world based on keywords. Users can also view the results of their previous searches.

## Prerequisites

- Python 3.x
- pip
- virtualenv (optional, but recommended)

### Install virtualenv if not already installed
  ```
  pip install virtualenv
```
### Create a virtual environment (replace 'venv' with your preferred name)
```
  virtualenv venv
```
### Activate the virtual environment

  #### On Windows:
```
  venv\Scripts\activate
```
  #### On macOS and Linux:
```
  source venv/bin/activate
```
## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/akshay-toshniwal/the-midnight-times.git
   cd the-midnight-times
   ```

2. Install Django and project dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Rename `.env_sample` as `.env`

    - Set `NEWS_API_TOKEN` with valid value `IVXtTaziYiHqSgUizaYabO0DQxBcIz0n6im1uVOg`

4. To start with project
    ```
    cd news_search_project/
    ```

5. Migrate the database:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create superuser (admin):

   ```
   python manage.py createsuperuser
   ```
   Follow the prompts for admin `username`, `password`

8. Run the development server:

   ```
   python manage.py runserver
   ```

9. Access the application in your web browser at http://localhost:8000/

10. Access the Admin interface of application in your web browser at http://localhost:8000/admin
    - Login with same `username` which used while creating `superuser`
  

### Time Taken to Complete project
  - 7 Hours

### Overall experience of working on this project
  - Overall, the experience was positive. The project was simple, however managing it after work hours was difficult because of my job at the time.
