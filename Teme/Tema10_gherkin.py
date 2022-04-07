'''
Background: (la fiecare scenariu de test se fac acesti 2pasi)
Given: I am on the https://the-internet.herokuapp.com/ home page
And: I click on the Form Authentication link
'''

# se verifica ca noul url e corect
'''1
Given: I am on the  Home page url: https://the-internet.herokuapp.com/
When: I click on the Form Autehntication Link
Then: I should land on Login page with url: https://the-internet.herokuapp.com/login
'''

# verificam page title
'''2
Given: I am on the  https://the-internet.herokuapp.com/ home page
When: I click on the Form Autehntication Link
Then: I should see that the page title is: "The Internet" 
'''

# verificam textul de pe label-ul Login Page e corect
'''3
Given: I am on the  https://the-internet.herokuapp.com/ home page
When: I click on the Form Autehntication Link
Then: I see that the text for the sub-heading/label is: "Login Page"
'''

# verificam ca butonul de login este displayed
'''4
Given: I am on the  https://the-internet.herokuapp.com/ home page
When: I click on the Form Autehntication Link
Then: I see that on this page there is a button with "Login" text on it
'''

# verificam exista un element care contine un href attribute
'''5
Given: I am on the  https://the-internet.herokuapp.com/ home page
When: I click on the Form Autehntication Link
Then: I see that on this page there is a link with "Elemntal Selenium" text
And: I see that it lids me on: http://elementalselenium.com/
'''

# verificam ca se afiseaza mesajul de eroare daca nu completam campurile Username&Password
'''6
Given: I am on the  https://the-internet.herokuapp.com/ home page
And: I click on the Form Autehntication Link
When: I don't fill anything in Username field
And: I don't fill anything in Password field 
And: I click on the Login button
Then: I see an error message displayed with text: "Your username is invalid"
'''

''' 9
Scenario: I see one "Username" label and one "Password" Label
Given: I am on the  https://the-internet.herokuapp.com/ home page
When: I click on the Form Autehntication Link
Then: I see an input field with "Username" label
And: I see an input field with "Password" label
'''

'''
Background:
Given: I am on the https://the-internet.herokuapp.com/ home page
And: I click on the Form Authentication link'''

'''7
Scenario: The message error is displayed when we fill with username and password invalid
When: I fill "Name" in Username field
And: I  fill "Pass" in Password field 
And: I click on the Login button
Then: I see the error banner with the correct message: "Your username is invalid!"
'''

'''8
Scenario: The message error it's not displayed anymore when we close it
When: I don't fill anything in Username field
And: I don't fill anything in Password field 
And: I click on the Login button
And: I see the error banner
And: I click on X sign 
Then: I don't see the error message displayed anymore
'''

'''10
Scenario: The login flow 
When: I fill "tomsmith" in Username field
And: I fill "SuperSecretPassword!" in Password field
And: I click on Login button
Then: I land on a page with an url that contains word "/secure"
And: I see a green banner 
And: I see that on the green banner is displayed a message that contains the text "secure area!"
'''

'''11
Scenario: After the login flow, at Logout we are on the correct url
When: I fill "tomsmith" in Username field
And: I fill "SuperSecretPassword!" in Password field
And: I click on Login button
And: I click on Logout button
Then: I land on a page with the url: 'https://the-internet.herokuapp.com/login'
'''

