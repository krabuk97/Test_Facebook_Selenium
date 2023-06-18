# Automated Facebook Web Application Tests

This project contains automated tests for the Facebook web application's functionality using the Selenium library.

## Description

The tests verify various features of the Facebook web application, such as login, creating a new post, adding friends, and sending messages. Each test executes a sequence of steps to test the respective functionality.

### Test 1: Facebook Login

This test verifies the correctness of the login functionality on Facebook. It performs the following steps:

1. Opens the Facebook homepage.
2. Enters the email address.
3. Enters the password.
4. Submits the login form by pressing the Enter key.

### Test 2: Creating a New Post

This test verifies the ability to create a new post on the user's profile. It performs the following steps:

1. Opens the user's profile page.
2. Clicks on the "New Post" button.
3. Enters the post content in the "What's on your mind?" field.
4. Clicks the "Publish" button.

### Test 3: Adding a Friend

This test verifies the functionality of adding a new friend on Facebook. It performs the following steps:

1. Clicks on the "Friends" button.
2. Clicks on the "Confirm" button to add the friend.

### Test 4: Sending a Message

This test verifies the ability to send a message to another user on Facebook. It performs the following steps:

1. Searches for a specific person.
2. Clicks on the profile of the found person.
3. Clicks on the "Send Message" button.
4. Enters the message content.
5. Sends the message by pressing the Enter key.

### Test 5: Log Out

This test verifies the functionality of logging out from Facebook. It performs the following steps:

1. Clicks on the profile menu button.
2. Clicks on the "Log Out" button.

## Requirements

To run these tests, you need:

- Programming language: Python 3.x
- Web browser: Chrome (or another browser supported by WebDriver)
- WebDriver for the chosen browser
- Python libraries:
  - Selenium
  - WebDriver for Chrome (or another browser)

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/your-username/repository-name.git
   ```

2. Navigate to the project directory:

   ```shell
   cd repository-name
   ```

3. Install the required libraries:

   ```shell
   pip install -r requirements.txt
   ```

4. Configure the WebDriver for your chosen browser. Ensure that the WebDriver is available in the system's PATH or provide the WebDriver's path in the configuration file.

5. Run the tests:

   ```shell
   python test_file.py
   ```

Remember to replace `test_file.py` with the actual filename of the test file you want to execute.

Feel free to modify and expand the tests to suit your specific Facebook application's functionality and requirements.
