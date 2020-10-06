<h1 align="center">Marco Store</h1>
<div> 
<p>
Marco Store is an e-commerce site created as the 4th and last Milestone Project inside Code Institute fullstack developer course. The main purpose of this site is to sell cloths.
The bulk of the functionality was made possible with the use of the Django3 framework. Django3 is a Python run application and helps to put a lot of the structure and functionality in place, which in turns allows you to focus on the more important things about your website, such as the content and making it as user friendly as possible.
There are many benefits to using the Djnago3 framework, but the biggest one in my opinion is having instant access to an admin panel. The admin panel allows you to create, view, update and/or delete and record, whether it's a post, user or even just a specific category for one of your products.
Profile Page Functionality: The profile page will display a page that contains your email address and username and an option to edit your details. 
The deployed link for the site is:  https://marco-moreschi-milestone.herokuapp.com/
When testing this app, to make a payment, the following details should be used:

*	Card number: 4242 4242 4242 4242
*	CVC: any three numbers
*   Date: any future date
*	ZIP Code: any five numbers
</p>
</div>

## Table of Contents
1. [**User Experience (UX)**](#UserExperience(UX))

2. [**Wireframes**](#wireframes)

2. [**Features**](#features)

3. [**Technologies**](#technologies)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)




## User Experience (UX)
The site has a smooth and clear functionality. Customer users can see a list with all the products, search for products by name, see a product details, see other customers reviews and average of reviews. They can adjust their bag by updating quantity or remove items. Additionally, for customers that registered an account, they have access to their profile which includes the option to save their delivery details for future use and see their order history. Also, they can leave reviews and ratings. Business owner has access to the admin panel that allows them to update products details, price, and image, to delete products or add new ones.
All these features were created following these users’ goals:

### User goals

##### Guest customer:
*	As a customer, I want to view a list of all the products.
*	As a customer, I want to search a product by name or description.
*	As a customer, I want to be able to sort products by name or price.
*	As a customer, I want to see a product detail.
*	As a customer, I want to see reviews and ratings left by other customers.
*	As a customer, I want to have the ability to adjust the quantity of the items or remove them.
*	As a customer, I want to make online payments.
*	As a registered customer, I want to be able to save my delivery details for future use.

##### Business owner:

*	As a business owner, I want to be able to add, remove products and update product details.

### Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project.

[View the wireframes here](https://github.com/marcomoreschi/Milestone-4/tree/master/Wireframes) 

## Features

### Existing features

##### Header and navigation bar
*	logo on the top left with link to home page. 
*	search bar for looking after products by name. On smaller than large screens, it transforms into a search icon, which when selected opens into a search bar.
*	My account icon with dropdown list of options for register and login. When registered, the dropdown list contains profile and logout links.
*	Bag icon with link to your bag list items and the total price of the selected order.

##### Home page

* consists in a background picture and a call to action button that redirects to all products page.

##### All Products

* contains a list of all products available displayed using pagination. at the bottom you find the pagination navigation links.
* at the top, there are 5 badges that act as filters for each collection available on the site. 
* sorting option for prices and name in ascending or descending way.

##### Product detail

* when choosing one specific product you will redirect to the product that contains the chosen product, its details, input quantity option and a button to add it to bag
* reviews and average ratings left by users

##### Reviews

* on product detail page, you have the option to leave a review and to rate the product. This is made via a form that has an input field for ratings with options from 1 to 5. The average of ratings is displayed on each product details list. If the product has not rating it will show ‘No Rating”.

##### Bag 

* on the bag page, the user can see its selected products displayed on top of each other. Each product from the bag contains its image, name, price, quantity selected and the subtotal which is price multiplied by quantity.
* the user has the option to update each products quantity or remove it.
* on bottom right of the page, the grand total with delivery included is displayed and two buttons. One to proceed to checkout and one to go back and shop more. If the bag as no item it will show your bag is empty with a button for keep shopping.

##### checkout

* contains a form for the delivery details of the user.
* contains the payment form from Stripe that takes card number, CVC, expiry date and ZIP code.
* contains an order summary, as a table with products name, quantity selected, subtotal. Also, the delivery costs, grand total and a button that redirects to bag for adjusting it if needed. The delivery will be free over £30. In case you don’t spend £30 it will tell you how much you should spend for have free delivery.

##### Emails

* user receives an email on the email address provided with details of his order.

##### Register and login

* form for register with: email address, username, password fields.
* confirmation email for registering.

##### Profile

* this is available only for registered users. It contains a form with delivery details of the user that can be updated and saved for future purchase. 

##### Admin 

* for business owners the ability to add, edit, delete a product, this can be done from the admin panel.
* Update or remove a review.

## Technologies

### Tools

* GitPod - as code editor.
* GIT - to manage version control.
* GitHub - to share and store code remotely.
* Heroku - for hosting the application and deployment.
* AWS S3 - cloud service for media and static files.
* Stripe - for managing payments.
* Sqlite3 - database for development.
* PostgreSQL - database provided by Heroku for production.

### Libraries and frameworks

* Django3 - a high-level Python Web framework that encourages rapid development.
* Bootsrap4 - for layout and responsive design.
* FontAwesome - icons implementation.
* Crispy forms - a template language for python used to bring logic into templates.
* boto3 - a library that enables python code to modify AWS service.

### Languages

* HTML
* CSS
* Javascript
* Python 

# Testing

For this app, testing was made manually and with validator services. 
During development I constantly used Chrome Developer Tools to ensure responsiveness on all devices. During development, in settings.py, Django's debugger was set to:
```console
debug = False
```
This was so to ensure that when the app encounters an error, Django gives a detailed report of what happened and why the error occurred.
### Validators
*	W3C HTML Validator - this tool checks the .html files validity
*	W3C CSS Validator - this tool checks the .css files validity
*	Pep8 online - this ensures that the python code is legit and does not contain formatting errors.

### Manual testing
Manual testing was done on a series of different screen devices and browsers as Chrome, Firefox, Edge, Safari , Opera and Mi Browser. I used different scenarios for each feature on every device. The deployed app was sent to friends and family to ensure I have covered enough devices and to get feedback from real life users about design, UX and functionality.
#### Navbar
*	click on each navbar link to see if they open the designated pages. Notice if hover effects work and if the active state of the link is highlighted when on page
*	on smaller than medium devices, check if the toggle button and links work
#### Search bar
*	type in different existent keywords from name or description of the product. See if the results for the search are correct
*	type an inexistent keyword from name or description of the product. See if it gives no results
*	make a search without an input. See if your receive an error and you get redirected to the products page
#### Home
*	check responsiveness for products and collections cards display on different devices
*	click on each collection card to see if you are redirected to the designated collection page
#### All products
*	check if all products are displayed and the number of them is correct
*	check if pagination links work properly
*	click on each collection filter bag to see if they work properly. Check if the pagination links work.
*	select each sorting option and see if the sorting works as intended
#### Product details
*	check responsiveness of product details displays on different screens
*	choose a quantity and click add to cart. See if a success message appears that contains the product selected, total price, delivery, and button to go for checkout
*	try to type a bigger than 99 or smaller than 1 quantity. See if you get an error message
*	remove 1 as default quantity. Click add to bag. See if you get an error message
*	try to add letters as quantity. See if it was possible. 
*	see if the reviews are displayed correctly: username, date, star rating, subject and body
*	introduce different star ratings. Check if the star rating selected is displayed correct. Check if the average star rating is calculated correct and displayed properly
#### Bag page
*	click on the bag icon from the header to see if you get to the bag page
*	check if the selected products and the correct quantity are inside the bag
*	try to type a bigger than 99 or smaller than 1 quantity and click update. See if you get an error message
*	remove 1 as default quantity. Click update. See if you get an error message
*	try to add letters as quantity. See if it was possible. 
*	use increment and decrement buttons and click update. See if the updated quantity is the one selected.
*	click remove and see if the product is removed from the bag
*	remove all products and see if the back is empty
*	check if the total price, delivery, and grand total are calculated correct.
#### Checkout page
*	as a user not logged in click on secure checkout button. Check if a modal opens that gives option but as a guest. 
*	as logged in user, click on secure checkout button, and see if you are redirected to checkout page.
*	on checkout page, see if the order summary is displayed with the selected products, and if you didn’t spend £30 it will tell you how much you have to spend more for free delivery. 
*	as a user not logged in see if the delivery information form fields are empty
*	as a logged in user see if the delivery information fields are prepopulated with your details provided in your profile
#### Payment
For payments testing the following details should be use:
*	Card number: 4242 4242 4242 4242
*	CVC: any 3 digits
*	Date: any future date
*	ZIP Code: any 5 digits
#### Try the following scenarios:
*	type a wrong card number
*	type the correct payment details but do not provide your delivery details, see if you get error messages from the form
#### Checkout success
*	on checkout success page you should have a message that contains your order number and the email address where you'll get details with your order
*	as a logged in user or as a guest you have a button that redirects to the home page.
*	profile page is available only for logged in users
*	type your details in the delivery information form. Click update then go to the checkout page. Check if the delivery information form from checkout page is prepopulated with the correct information
*	try to update your delivery information without completing all the fields required. See if you get error messages.

## Deployment
This application can run locally or deployed to a live environment
## Local
The example provided uses GitPod as a code editor and Windows as an operating system.
1.	Save a copy of the github repository located at https://github.com/marcomoreschi/Milestone-4  by clicking the 'download.zip' button at the top of the page and extracting the zip file to your chosen folder. 
2.	In your IDE terminal, navigate to this folder
3.	Install the required packages and start your virtual environment with these commands
```console
pipenv install
pipenv shell
```
4.	Install all required modules with the command:
```console
pip install -r requirements.txt
```
5.	Create a env.py file and add it to your .gitignore
6.	Copy the following into the env.py file:
```console
7.	import os
8.	
9.	os.environ['SECRET_KEY'] = 'your value'
10.	os.environ['DATABASE_URL'] = 'your value'
11.	os.environ['STRIPE_PUBLIC_KEY'] = 'your value'
12.	os.environ['STRIPE_SECRET_KEY'] = 'your value'
13.	os.environ['AWS_ACCESS_KEY_ID'] = 'your value'
14.	os.environ['AWS_SECRET_ACCESS_KEY'] = 'your value'
os.environ['DEVELOPMENT'] = '1'
```
15.	Set up the databases by running the following management command in your terminal:
```console
python manage.py migrate
```
16.	Create the superuser so you can have access to the django admin:
```console
python manage.py createsuperuser
```
17.	Start your server by running the following command in your terminal:
```console
python manage.py runserver
```
### Deploy to Heroku
The deployed site can be found here: https://marco-moreschi-milestone.herokuapp.com/
Login to Heroku and create a new app
1.	On the Resources tab, in the Add-ons field look for Heroku Postgres, select the default Hobby Dev - Free tier, then click the Provision button. This will provision a Postgres Database for you.
2.	In Heroku, go on settings tab and click Reveal Config Vars.
3.	Add the values from your env.py file to heroku:
```console
* AWS_ACCESS_KEY_ID - your value
* AWS_SECRET_ACCESS_KEY - your value
* DATABASE_URL - your value
* EMAIL_HOST_PASS - your value
* EMAIL_HOST_USER - your value
* SECRET_KEY - your value
* STRIPE_PUBLIC_KEY - your value
* STRIPE_SECRET_KEY - your value
USE_AWS - True*
```
4.	Set up the databases with the following command:
```console
python manage.py migrate
```
5.	Create the superuser for the postgres database so you can have access to the django admin:
```console
python manage.py createsuperuser
```
6.	Preload products and collections using following commands (the order is important):
7.	
```console
python manage.py loaddata collections.json
python manage.py loaddata products.json
```
8.	Save all the requirements:
```console
pip freeze > requirements.txt
```
9.	Create Procfile:
```console
echo web: gunicorn dream_woollies.wsgi:application > Procfile
```
10.	Add the files and push them to Github:
```console
11.	git add .
12.	git commit
    git push
```
13.	Deploy branch in Heroku
14.	In settings.py add https://marco-moreschi-milestone.herokuapp.com/  to Allowed Hosts

## Credits

### Media 

All the images and texts were provided in Google which is the rightful owner of their copyright.

### Code

*	A big part of the code was developed by following the Code Institute video lessons. Where needed, I provided credits in the comments of the code.
*	StackOverflow where I found answers for different topics.
