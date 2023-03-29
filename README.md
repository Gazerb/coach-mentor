# Clitheroe Wolves Coach Mentor System

## Code institute / City of Bristol College Milestone Project 3

<img src="documentation/readme-images/am-i-responsive-coach-mentor.png" height="auto" width="100%" alt="Image of index.html on mulitple devices to show responsiveness"/>

<sub>*Created using* [Am I Responsive](http://ami.responsivedesign.is/)</sub>

Clitheroe Wolves Coach Mentoring system is something that Clitheore Wolves FC will use with their new coaches in order for them to get the help and support they need from experienced coaches within the club. This is my third milestone project for the full stack development course at Code Institute / City of Bristol College. For this project I had to create a full-stack site that allows your users to manage a common dataset about a particular domain. This was to include the use of Flask framework.

Click <a href="https://clitheroe-coach-mentor.herokuapp.com/">here</a> to view the live website.

## User Experince 
In this section, I will be providing information on the UX process. Focusing on who the PeakMotion website is for, the main aims of this project and how the website helps to meet the users needs

The Project Goals:
<ul>
    <li>Allow users to register an account</li>
    <li>Enable users to make a booking </li>
    <li>Alow users the ability to change a booking created</li>
    <li>Provide information and the current club mentors</li>
</ul>

## User stories

A new user:
<ul>
    <li>Easy to sign up</li>
    <li>Easy to make a booking</li>
    <li>Easy to change a booking made</li>
</ul>

#### Returning users

Current user:
<ul>
    <li>Easy to make a booking</li>
    <li>Easy to change a booking made</li>
</ul>

Buisness Owner:
<ul>
    <li>Give users the ability to make bookings with the coach mentors</li>
    <li>Show users contact details for the club and coach mentors</li>
    <li>Provide other learning resources</li>
</ul>


## User Centered Design
### 1. Strategy Plane
The User Centered Design process started with the creation of the user stories and these influenced the design and layout of the product.


### 2. Scope Plane
A system so the club can allow its new coaches to book time with one of the experienced coach metors to help them with any issues or just to improve them as coaches.


### 3. Structure Plane
After idenifying the needs of the business owner and users that will use the new system the below was identified as required:
<ul>
    <li>Blue and White colour scheme to match the clubs current colours</li>
    <li>Club contact details/li>
    <li>Current club mentors</li>
    <li>Booking form</li>
    <li>User bookings page</li>
    <li>Clear layout</li>
    <li>easy navigation for the user</li>
</ul>


### 4. Skeleton Page
To create the wireframes for the product I used <a href="https://www.figma.com/>">Figma</a>. They were created to appear as they would on a desktop, table and mobile.

We have a header containing the logo and nav bar.

To help the website with responsiveness of devices it was decided that when viewed on a mobile that the nav bar would be in a drop down hamberger menu.

A footer is also included which contains the contact details of the club and links to other resources.

#### Wireframes
Desktop:
<ul>
    <li><a href="documentation/wireframe/Desktop-Home-page.png">Index Page</a></li>
    <li><a href="documentation/wireframe/Desktop-Log-In.png">Log In Page</a></li>
    <li><a href="documentation/wireframe/Desktop-Make-a-Booking.png">Make a Booking Page</a></li>
    <li><a href="documentation/wireframe/Desktop-Mentors.png">Mentors Page</a></li>
    <li><a href="documentation/wireframe/Desktop-User-bookings.png">User Bookings page</a></li>
    <li><a href="documentation/wireframe/Desktop-User-Profile.png">User Profile Page</a></li>
</ul>


Tablet:
<ul>
    <li><a href="documentation/wireframe/Tablet-Home-Page.png">Index Page</a></li>
    <li><a href="documentation/wireframe/Tablet-Log-In-page.png">Log In Page</a></li>
    <li><a href="documentation/wireframe/Tablet-Make-a-Booking.png">Make a Booking Page</a></li>
    <li><a href="documentation/wireframe/Tablet-Mentors.png">Mentors Page</a></li>
    <li><a href="documentation/wireframe/Tablet-Profile.png">User Profile Page</a></li>
    <li><a href="documentation/wireframe/Tablet-user-bookings-page.png">User Bookings Page</a></li>
</ul>


Mobile:
<ul>
    <li><a href="documentation/wireframe/Phone-home.png">Index Page</a></li>
    <li><a href="documentation/wireframe/Phone-log-In.png">Log In Page</a></li>
    <li><a href="documentation/wireframe/Phone-Make-a-Booking.png">Make a Booking Page</a></li>
    <li><a href="documentation/wireframe/Phone-mentors.png">Mentors Page</a></li>
    <li><a href="documentation/wireframe/Phone-User-bookings-Page.png">User Bookings Page</a></li>
    <li><a href="documentation/wireframe/Phone-User-Profile-Page.png">User Profile Page</a></li>
</ul>


### 5. Surface Plane
#### Design
Due to the modern society of users now looking for information on mobile phones and tablet this was created with a mobile-first approach.

#### Colour Scheme
The colour scheme was chosen to be simple, clean, bright and visually appealing. Blue is the chosen as this is the primary colour of the club. There will be slight variations of the blue throught the system. Some ares will also contain white as this is the second colour of the clubs main two colours.
<img src="documentation/readme-images/colour.png" height="auto" width="100%" alt="Image of colour palette showing colours used in website" />

<sub>*Colour palette created at* [coolors.co](https://coolors.co/7ae9f0-04c6d3-fafafa-0420d4-000000).</sub>

<ul>
    <li>#1565C0. Chosen for the navigation bar and footer</li>
    <li>#0D47A1. A darker shade of blue chosen for the copyright area of the footer.</li>
    <li>#E3F2FD. Chosen as the background for the form areas</li>
    <li>#2196F3. Chosen as the background for list of bookings</li>
    <li>Green was chosen for the edit buttons</li>
    <li>Red was chosen for the delete/ cancel buttons</li>
</ul>

#### Icons
Icons were used alongside to help the user understand sections of the website at a glance. I have taken the icons used in this project from Font Awesome (https://fontawesome.com/).

## Development
I was advised by my mentor to change the buttons to have one on each side of the page cards rather then right next to each other to improve UX. I was also advised to add icons to the buttons to improve the clearness of the website and buttons.


## Features
### Consistent features on all pages
<ul>
    <li>Header, contains the same company logo and navigation bar</li>
    <li>Footer, Contains company contact number, email and social links</li>
</ul>

### Other features
<ul>
    <li>Ability for the user to create an account</li>
    <li>User can log in and out of their account</li>
    <li>User can make, edit and cancel bookings</li>
    <li>User can also delete their account</li>
</ul>

## Future Features
<ul>
    <li>Allow the mentors to set availabilty that can be booked</li>
    <li>Add an area where managers can share sessions and other resources</li>
    <li>Add feature so once booking is made then the mentors get an email of this booking with contact details</li>
    <li>Reviews area for the coaches to review their mentors</li>
    <li>User to receive email confirming booking</li>
</ul>

## Technologies used
The below languages were used in this project:
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript - Imported from Materialize script</li>
    <li>Python</li>
    <li>JQuery - imported from Materialize script</li>
    <li>MongoDB</li>
    <li>Flask</li>
    <li>Jinja</li>
</ul>

## websites used
<ul>
    <li>Am I Responsive (http://ami.responsivedesign.is/). This was used to create the mock up image at the top of this readme document</li>
    <li>Code Institute (https://codeinstitute.net/). Modules and walk-through projects have been used and copied in this project</li>
    <li>Coolors (https://coolors.co/7ae9f0-04c6d3-fafafa-0420d4-000000). Used to create website colour scheme and palette</li>
    <li>Font Awesome (https://fontawesome.com/). Used for icons within website</li>
    <li>Chrome Developer tools. Used to test website for buys and responsiveness</li>
    <li>Google Fonts. Used to incorporate fonts in website</li>
    <li>Github. Used for site respository</li>
    <li>Gitpod. Online developer tool used to build and develop this project</li>
    <li>Heroku. To deploy finished website</li>
    <li>W3C CSS Validation. Used to validate projects CSS code</li>
    <li>W3C HTML Validation. Used ti validate projects html pages / code</li>
    <li>Figma. Used to create websites wireframes</li>
</ul>

## Performance Testing
### Lighthouse testing
I used the chrome extension 'Lighthouse' to test the performance of the website. Below is the capture of my report.

<img src="documentation/readme-images/lighthouse.png" height="auto" width="100%" alt="First Lighthouse Report." />

### W3C HTML Validator
All pages checked and no errors found within the HTML.


### W3C CSS Validator
No error where found in the CSS code when that went through the validator.


## Manual Testing
The website was tested on the following browsers:
<ul>
    <li>Google Chrome - Version 106.0.5249.91</li>
    <li>Safari on iPhone</li>
    <li>Opera - Version 90.0.4480.80</li>
    <li>Microsoft Edge - Version 105.0.1343.53</li>
    <li>Firefox - Version 105.01</li>
</ul>

All browsers where tested fully and the website behaved as expected on them. I tested:

<ul>
    <li>That the user can log in and out</li>
    <li>That if the wrong password is entered the user is told and can try again</li>
    <li>That the user can register</li>
    <li>That the user can added, edit and cancel bookings</li>
    <li>That the user can delete their account</li>
    <li>That the user can edit their profile</li>
</ul>

## Device & responsiveness testing
The below devices where tested to see how the website behaved on them and their responsiveness using Google Developer Chrome tools.

<ul>
    <li>iPhone SE</li>
    <li>iPhone Xr</li>
    <li>iPhone12 Pro</li>
    <li>Pixel 5</li>
    <li>Samsung S20 Ultra</li>
    <li>iPad Air</li>
    <li>iPad Mini</li>
    <li>Surface Pro 7</li>
</ul>

It was also tested on the below laptop and desktop sizes:

<ul>
    <li>15" Laptop (1024 x 800)</li>
    <li>22" Desktop (1680 x 1050)</li>
    <li>24" Desktop (1920 x 1200)</li>
</ul>

### Tested User Stories
Below I will discuss how the project met the requirements of the user stories from earlier.

#### New User
So for a new user of this booking system they needed to be able to complete below:
<ul>
    <li>sign up</li>
    <li>make a booking</li>
    <li>change a booking made</li>
</ul>

After testing this is proven to work for the new user.

<img src="documentation/readme-images/new-user-1.png" height="auto" width="100%" alt="image showing nav bar pages where the new user requirements can be met" />
<img src="documentation/readme-images/new-user-2.png" height="auto" width="100%" alt="image showing nav bar pages where the new user requirements can be met" />


The above also met the requirements of a current/ returning user:
<ul>
    <li>Make a booking</li>
    <li>Change a booking made</li>
    <li>Cancel a booking</li>
</ul>


We have also met the buisness owners requirement of:
Buisness Owner:
<ul>
    <li>Give users the ability to make bookings with the coach mentors</li>
    <li>Show users contact details for the club and coach mentors</li>
    <li>Provide other learning resources</li>
</ul>

We already know from testing that users can make bookings with mentors. To meet the other requirement each booking the user makes they have to enter their contact details and the reason for their booking to assist them mentors. We have also provided other learning resouces on the links in the footer on every page.

<img src="documentation/readme-images/buisness-1.png" height="auto" width="100%" alt="image showing booking form" />
<img src="documentation/readme-images/buisness-2.png" height="auto" width="100%" alt="image showing other resouce links" />

## Bugs
I had a few bugs with this project throughout. The first was that my website would not connect to my Mongdb, this was due to an incorrect path to the mongodb.

Second was issues with showing users current bookings. This was resolved by inputting the correct code on all pages it was required and calling the booking ID when the show bookings page loaded.


Third, I was having issues where when the account was deleted the user still had a session. This was resolved by added in session pop in the app.py.


### Deployment to Heroku

1. Log in to your Heroku account and create a new App.
2. Set the environment variables in Settings > Reveal Config Variables
3. The following Variables must be set 
```
MONGO_URI = mongodb+srv://<INSERT USERNAME>:<INSERT PASSWORD>@<INSERT CLUSTERNAME>.zbpbq.mongodb.net/<INSERT COLLECTION NAME>?retryWrites=true&w=majority
MONGO_DBNAME = <INSERT YOUR COLLECTION NAME>
SECRET_KEY = <INSERT YOUR SECRET KEY>
IP = 0.0.0.0
PORT = 5000
```
4. Create requirements.txt from your project with the help of ```pip3 freeze --local > requirements.txt ```
5. Create a Procfile ```echo web: python app.py > Procfile``` 
6. Commit changes to Git ```git add . ``` followed by ```git commit -m ""```
7. Log in to heroku from your terminal ```heroku login```
8. Add exisitng repository to Heroku ```heroku git:remote -a <your repository>```
9. Push changes to Heroku ```git push heroku master```


## Credits
In this project of lot of my early code was used with the help of the Code institute Flask taskmanager app walkthrough. I then added code to suite this project.

I have also used materialize throught the project for the nav bar and mobile nav bar, layout, colours, forms and buttons.


