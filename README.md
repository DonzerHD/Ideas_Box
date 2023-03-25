# Ideas_Box

Ideas_Box is a web application that allows users to create, share, and vote on boxes that contain ideas.

## Features

- Create a box with a title and description
- Vote for or against a box
- Sort boxes by date or popularity
- Pagination for long lists of boxes

## Technologies Used

- Python
- Django
- SQLite
- HTML/CSS/JavaScript
- Bootstrap
- Docker
- Azure

## Installation

1. Clone the repository
2. Create a virtual environment with Python 3.9
3. Install the dependencies with `pip install -r requirements.txt`
4. Create a PostgreSQL database and add the credentials to the `settings.py` file
5. Run the database migrations with `python manage.py migrate`
6. Start the server with `python manage.py runserver`

## Usage

1. Navigate to the homepage to view a list of all boxes
2. Click on the "Create a Box" button to create a new box
3. Vote for or against boxes by clicking the corresponding buttons
4. Use the dropdown menu to sort the boxes by date or popularity
5. Use the pagination links to navigate through long lists of boxes

## Docker
This application can also be run using Docker:
- Build the Docker image: `docker build -t ideas-box` .
- Run the Docker container: `docker run -p 8000:8000 ideas-box` .

Don't forget to update the database settings in settings.py and the IP address in settings.py to match your environment.

## Deployment
This application can be deployed to Azure. A PostgreSQL database can be set up on Azure, and the `DATABASES` setting in `settings.py` should be updated accordingly.

## License
This project is licensed under the terms of the MIT license.

## Creator
* **Thomas.l59**[@DonzerHD](https://github.com/DonzerHD)