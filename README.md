# ProductionManagement


Production Management API!

The Production Management API is a Django-based RESTful API for managing products and their associated materials. 
It provides endpoints to retrieve product information, including quantities and materials, 
as well as manage warehouses and raw materials.

Features!

-Retrieve a list of products with their quantities and materials
-Get detailed information about individual products
-Manage warehouses and their quantities of raw materials
-Add, update, and delete products, materials, and warehouse quantities

Requirements
Python 3.x
Django 3.x
Django REST framework 3.x

Installation!

1 - Clone the repository:
git clone https://github.com/your-username/production-management.git

2 -Create a virtual environment (optional but recommended):

python3 -m venv myenv
source myenv/bin/activate

3- Install the dependencies:

pip install -r requirements.txt

4 - Apply database migrations:

python manage.py migrate

5- Start the development server:

python manage.py runserver

6 - Access the API at http://localhost:8000/api/



API Documentation

-Swagger Documentation: Visit http://localhost:8000/swagger/ to explore the API using Swagger.

![image](https://github.com/mukhammadjamshed/ProductionManagement/assets/110180732/a101bad2-6972-4656-8680-c4ff19c8cd37)

-ReDoc Documentation: Visit http://localhost:8000/redoc/ for a user-friendly API documentation using ReDoc.

![image](https://github.com/mukhammadjamshed/ProductionManagement/assets/110180732/bfb675f1-7501-4a35-9cd0-91991233c522)


Contributing
Contributions are welcome! If you would like to contribute to the project, please follow these steps:

1 Fork the repository.
2 Create a new branch for your feature or bug fix.
3 Make the necessary changes and commit them.
4 Push your branch to your forked repository.
5 Submit a pull request with a detailed description of your changes.



This is the output from postman

![image](https://github.com/mukhammadjamshed/ProductionManagement/assets/110180732/8e68767f-b4f1-48cc-a017-3ad5e51b90c3)
![image](https://github.com/mukhammadjamshed/ProductionManagement/assets/110180732/c550a5f7-0ce2-45e3-9f98-942266de8813)




