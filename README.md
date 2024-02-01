# E-Commerce

Setup to run the E-Commerce Project

Step 1:

    Take the clone from the GitHub

    command: git clone https://github.com/sahil-verma-818/E-Commerce.git

Step 2:

    Move to the base directory folder

    command: cd E-Commerce/E_Commerce/

Step 3:

    Take a pull from docker hub 

    command: docker pull sahilverma818/e_commerce_web

Step 4:

    Run the Project in detach mode

    command: docker compose up -d

Step 5:

    Open the bash:

    command: docker compose exec web bash

Step 6:

    Inside the bash:

    command to migrate:
    command: python3 manage.py migrate

    command to create super user
    command: python3 manage.py createsuperuser

    Fill all the required details

    After successful user creation
    Exit from bash

    command: Exit

Step 7:

    In order to view running terminal and response, run again the following command

    command: docker compose up

For exiting the running terminal:

    press ctrl + c

for clearing or closing the running container 

    command: docker compose down
