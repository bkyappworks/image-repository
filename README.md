# Image Repository - Upload your favorite images!
<h2>Summer 2022 -  Shopify Developer Intern Challenge</h2>
<p>https://docs.google.com/document/d/1z9LZ_kZBUbg-O2MhZVVSqTmvDko5IJWHtuFmIu_Xg1A/edit</p>
<h3> An Image Repository which users can ADD images </h2>
<li> Private permissions mechanism: Users have to sign up or log in before they can upload image(s) </li>
<li> After users upload images, they will see the images they uploaded displayed on the screen and they can right click to access the images</li>
<li> With security mechanism uploading and stored images</li>

<h2>How to run the App</h2>
<p>1. Clone this repository</p>
<p>2. Run pip install -r requirements.txt</p>
<p>3. Run python manage.py runserver</p>
<p>4. Open your browser and go to 127.0.0.1:80</p>

<h2>How to run the Test</h2>
<p>1. pip install django-utils-six</p>
<p>2. Run python manage.py test image</p>

<h2>Technology</h2>

<li>Backend: Python
<li>Web Development: Django
<li>Front-End: HTML
<li>Version Control: Git, GitHub
<li>Test: Unittest

<h2>Security</h2>
<ul>
    <h3>1.  Cross site scripting (XSS) </h3>
        <li> Django templates escape specific characters which are particularly dangerous to HTML
    <h3>2. Cross site request forgery (CSRF) </h3>
        <li> In any template that uses a POST form, use the csrf_token tag inside the <form> element if the form is for an internal URL
    <h3>3. Clickjacking </h3>
        <li> Django contains clickjacking protection in the form of the X-Frame-Options middleware which in a supporting browser can prevent a site from being rendered inside a frame.
    <h3>4. User-uploaded content </h3>
        <li> Only logged in user can upload content
        <li> Limit these uploads in web server configuration to a reasonable size in order to prevent denial of service (DOS) attacks. 
        <li> Use .env to store secret_key
</ul>
<h2>Testing</h2>
    <li> Test Models
    <li> Test Urls
    <li> Test Views

<h2>Contact</h2>

beckyappworks@gmail.com