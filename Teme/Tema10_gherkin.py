'''
Background: (la fiecare scenariu de test se fac acesti 2pasi)
Given: I am on the https://the-internet.herokuapp.com/ home page
And: I click on the Form Authentication link
'''

# se verifica ca noul url e corect
'''
Given: I am on the  Home page url: https://the-internet.herokuapp.com/
When: I click on the Form Autehntication Link
Then: I should land on Login page with url: https://the-internet.herokuapp.com/login
'''

# verificam page title
'''
Given: I am on the  https://the-internet.herokuapp.com/ home page
When: I click on the Form Autehntication Link
Then: I should see that the page title is: "The Internet" 
'''

# verificam textul de pe label-ul Login Page e corect
'''
Given: I am on the  https://the-internet.herokuapp.com/ home page
When: I click on the Form Autehntication Link
Then: I see that the text for the sub-heading/label is: "Login Page"
'''

# verificam ca butonul de login este displayed
'''
Given: I am on the  https://the-internet.herokuapp.com/ home page
When: I click on the Form Autehntication Link
Then: I see that on this page there is a button with "Login" text on it
'''

# verificam exista un element care contine un href attribute
'''
Given: I am on the  https://the-internet.herokuapp.com/ home page
When: I click on the Form Autehntication Link
Then: I see that on this page there is a link with "Elemntal Selenium" text
And: I see that it lids me on: http://elementalselenium.com/
'''


# error message not displayed
'''
Given: I am on the  https://the-internet.herokuapp.com/ home page
And: I click on the Form Autehntication Link
When: I complete user name with correct credentials
And : I complete
And: I click Login button
Then: I verify that the correct error message it's displayed
And: I close the error message
Then: I should not see the error message anymore
'''