# Testing During Development

During development I continually testing the project in a number of ways.

- I manually tested the responsiveness of each page and element within the development environment by running the application and checking the output within the browser.

- Once happy with any new additions the code was pushed to Heroku. I then ran the same tests using other devices, and had family and friends do the same on their own devices, before passing on any feedback or suggestions.

## Manual Testing

* During testing I used numerous web browsers to ensure the site performed well on a range of browsers. On desktop I used the following:

1. Safari
2. Chrome
3. Firefox
4. Brave

* I used Google devtools to simulate different screen sizes and devices to check useability and responsiveness on a range of screen sizes.

* I also tested the site on an iPhone 11 and an ipad pro and air, using both Safari and Chrome.


# Testing User Stories from the User Experience Section

## User Stories:
---
- As a first time user I want to:

1. Quickly understand the purpose and layout of the site.
2. Understand how to create a profile and navigate the sites functionality.
3. Be able to customise my profile.
4. Be able to view products.
5. Use the integrated interactive score player.

- As a returning visitor I want to:

1. Be able to search for high quality scores by search terms.
2. Be able to filter scores based on a number of parameters.
3. Be able to purchase and view a library of my scores as both a PDF and interactive file.
4. View top performing scores through a review system.
5. Be able to request scores in a reddit style forum where the most popular posts rise to the top.

- As a Vendor I want to:

1. Be able to upload and sell my own scores.
2. Be able to view important sales data regarding income, growth, top performing products etc.
3. Customise my sales profile.
4. View trending score requests to help produce popular products.

## Responses to User Stories

- As a first time user I want to:

1. Q.  Quickly understand the purpose and layout of the site.
      * The site is layed out in an organised manner with quick access to any area from the navbar. The process of adding, editing and purchasing musical scores is intuitive and streamlined.

2. Q. Understand how to create a profile and navigate the sites functionality.
      * The website features a very streamlined and simple navigation bar that quickly allows users access to any area of the site within 2-3 mouse clicks. All areas of the site are neatly organised to make navigation as streamlined as possible.
      The Registeration process is quick and clear and can easily be completed in just a minute.

3. Q. Be able to customise my profile.
      * The user is easilly able to update and change details about their profile. They are also able to upload their own custom profile picture and cover photo.

4. Q. Be able to view products.
    * Products are easily accessible either via the products page, the search bar or many of the other links on the site. Products can be searched for and filitered in a myriad of different ways, and the products detail page is very informative and clearly layed out.

5. Q.  Use the integrated interactive score player.
      * The score player is easilly accesible either via the navbar or through the 'purchased scores section. The user is able to use this feature regardless of whether they have an account or not.


- As a returning visitor I want to:

1. Q. Be able to search for high quality scores by search terms.
      * Comprehensive search features allow the user to sort and filter products in many ways including by rating, name, price, description, and genre.

2. Q. Be able to filter scores based on a number of parameters.
      * Products can be filtered in many ways to be ranked either by price or rating, or filtered by genre and difficulty.

3. Q. Be able to purchase and view a library of my scores as both a PDF and interactive file.
      * Scores are neatly collected in a library of purchased scores. From this menu the relevant files can be easilly accessed. 

4. Q. View top performing scores through a review system.
      * All products can receieve user reviews which then generate an average score for the item and vendor. Scores can then be filtered by this review score.

5. Q. Be able to request scores in a reddit style forum where the most popular posts rise to the top.
      * Users are able to post advertisements for scores they would like to see. These posts can then be upvoted and commented on by other users. The number of likes a score has determine it's ranking on the page.

            
- As a Vendor I want to:

1. Q. Be able to upload and sell my own scores.
    * The process of uploading a score is simple. If an image is not provided a watermarked sample of the score will be automatically generated for the user. Once the score is uploaded it can be easilly purchased by other users. 

2. Q. Be able to view important sales data regarding income, growth, top performing products etc.
    * A large amount of useful sales data is available to the user though the sales dashboard. Metrics include; number of customers, income, growth, most popular genre sold, top performing products, sales data from today vs last week and month etc.

3. Q. Customise my sales profile.
    * The users sales profile can easily be customised to incldue a profile and cover photo, bio and other information.

4. Q. View trending score requests to help produce popular products.
    * Vendors are easilly able to see popular score requests and to respond to them.
    
## Further Testing
---
### Validator Results
* All Html pages passed through the official [W3C Validator](https://validator.w3.org) validator with no errors.

* The CSS stylesheet passed through the official [W3C Validator](https://validator.w3.org) with no issues.

HTML results can be found [here](README_images/testing_images/html)
CSS results can be found [here](README_images/testing_images/css)


## Accessibility and Performance
---
The project was tested using both [lighthouse](https://developers.google.com/web/tools/lighthouse) and [Wave](https://wave.webaim.org/) to check the overall performance and accessibility of the project.

The [Wave](https://wave.webaim.org/) report revealed some errors however I believe these were irrelevant. For example the link for the side nav is a burger icon. Due to its' lack of text Wave reported this as an empty link error. Some of the labels for the search bars are also not recognised despite being present.
Wave results can be viewed [here](README_images/testing_images/wave)

The [lighthouse](https://developers.google.com/web/tools/lighthouse) report was very positive for almost all areas, particularly for accessibility, SEO and best practises. Some marks were lost again due to an 'Empty link' and form label in the nav being present in the 'base.html' file, and thus occuring on every page.
Performance was generally rated positively, and the site seems to run very well on all tested devices.
Light house results can be viewed [here](README_images/testing_images/lighthouse)

The python file was run through the PEP8 validator to ensure no syntax errors, and the Javascript files were validated using JsHint.
I used both autopep8 and an online tool to try to adhere to PEP8 guidlines with the python code. In some cases the code is longer than the suggested 79 characters. I chose to leave these as they were as any alterations I made resulted in much less readable code.

JS results can be found [here](README_images/testing_images/js)

[Return to README](/README.md)