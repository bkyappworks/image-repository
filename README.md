# Image Repository - A place you can upload your favorite images!
<h2> An Image Repository which users can ADD one / bulk / enormous amount of images </h2>
<li> Private permissions mechanism: Users have to sign up or log in before they can upload image(s) </li>
<li> After users upload images, they will see the images they uploaded displayed on the screen and they can right click to access the images</li>
<li> With security mechanism uploading and stored images</li>

<h2>Technology</h2>

<li>Backend: Python
<li>Web Development: Django
<li>Front-End: HTML
<li>Version Control: Git, GitHub
<li>Test: Unittest

<h2>Security</h2>
<ul>
    <li> Cross site scripting (XSS) 
        <li> Django templates escape specific characters which are particularly dangerous to HTML
    <li> Cross site request forgery (CSRF)
        <li> In any template that uses a POST form, use the csrf_token tag inside the <form> element if the form is for an internal URL
    <li> Clickjacking
        <li> Django contains clickjacking protection in the form of the X-Frame-Options middleware which in a supporting browser can prevent a site from being rendered inside a frame.
    <li> User-uploaded content
        <li> Only logged in user can upload content
        <li> Limit these uploads in web server configuration to a reasonable size in order to prevent denial of service (DOS) attacks. 
        <li> Use .env to store secret_key
</ul>


<h2>Contact</h2>

beckyappworks@gmail.com