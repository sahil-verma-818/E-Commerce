# E-Commerce

## Setup to run the E-Commerce Project

### Step 1:
**Take the clone from the GitHub**

    git clone https://github.com/sahil-verma-818/E-Commerce.git

### Step 2:
**Move to the base directory folder**

    cd E-Commerce/E_Commerce/

#
> **_NOTE:_**  Docker Setup is mandatory for further process.
### Step 3:
**Take a pull from docker hub** 

    docker pull sahilverma818/e_commerce_web

### Step 4:
**Run the Project in detach mode**

    docker compose up -d

### Step 5:
**Open the bash:**

    docker compose exec web bash

### Step 6:
- **Inside the bash:**
    - **command to migrate:**

          python3 manage.py migrate

    - **command to create super user**

          python3 manage.py createsuperuser

      > **_NOTE:_** Fill all the required details to create super user
    
    - **Exit from bash**

            Exit

### Step 7:
- **In order to view running terminal and response, run again the following command**

      docker compose up

- **For exiting the running terminal:**

      ctrl + c

- **For clearing or closing the running container** 

      docker compose down

