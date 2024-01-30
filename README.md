# Label-Hub-Selenium-Automation
Use cases covered with the test cases:

Login Functionality:
● Verify invalid login prevention and error messages.
● Test login with missing credentials.
● Validate successful login.

User Management:
● Confirm user creation with valid data.
● Test duplicate username prevention.
● Verify proper user deletion handling.

Project Management:
● Ensure creation and prevent duplicate project names.
● Validate project deletion functionality.

File Management and Annotation:
● Test file upload and format validation.
● Validate annotator interactions and data integrity.

System Configuration and Data Viewing:
● Verify system configuration adjustments.
● Test secure data viewing for authorized users.

Test Case Design Strategy:

Comprehensive Coverage: The test cases cover a broad spectrum of functionalities including
authentication, user and project management, file handling, and system configuration.

Negative Testing: Many test cases focus on negative testing (e.g., trying to create users with
invalid data) to ensure robust error handling.

Role-Based Testing: Different roles like Admin, Annotator, and Validator are tested to ensure
role-based access control and functionalities.

Edge Cases: Testing with edge cases like overly long names, invalid email formats, and
incorrect password requirements.

Test Case Implementation Details:

Selenium Automation: Selenium, a browser automation tool, is used to implement these test
cases.

Modular Design: Each test case is designed as a separate function (like Login, UserCreate,
projectCreate) to promote reusability and readability.

Test Case Running Details :

Here is the test cases list:
Case 1: Wrong ID
Attempt to login with an incorrect email ID.
Case 2: Without Password
Attempt to login with an email but without providing a password.
Case 3: Without ID and Password
Attempt to login with both email and password fields left empty.
Case 4: Without ID
Attempt to login without providing an email but with a password.
Case 5: Only Part of the Email
Attempt to login with an incomplete email.
Case 6: Correct ID and Password
Successfully login with the correct email and password.
Case 7: Create User without Role
Attempt to create a user without specifying a role.
Case 8: Create User without Email
Attempt to create a user without providing an email.
Case 9: Create User without Password Requirement
Attempt to create a user with an inadequate password.
Case 10: Create User without Name
Attempt to create a user without providing a name.
Case 11: Create User with All Valid Info
Successfully create a user with all required and valid information.
Case 12: Create User with Password Size >14
Create a user with an excessively long password.
Case 13: Create User with Big Name
Create a user with an overly long name.
Case 14: Create User without Gender
Attempt to create a user without specifying a gender.
Case 15: Create User without Valid Email
Attempt to create a user with an invalid email format.
Case 16: Create User with Non-Integer Mobile Number
Attempt to create a user with an invalid mobile number format.
Case 17: Delete a User
Successfully delete a user.
Case 18: Logout
Successfully log out.
Case 19: Create User with Mobile Number <11 Digits
Attempt to create a user with a short mobile number.
Case 20: Create User with Mobile Number >11 Digits
Attempt to create a user with a long mobile number.
Case 21: Create New Project
Successfully create a new project.
Case 22: Create Duplicate Project
Attempt to create a project with a name that already exists.
Case 23: Delete Project
Successfully delete a project.
Case 24: File Upload in Project
Successfully upload a file to a project.
Case 25: Annotator
Annotator logs in, searches for a project, annotates, and logs out.
Case 26: Validator (No Edit)
Validator logs in, searches for a project, performs validation without edits, and logs out.
Case 27: Validator (Edit)
Validator logs in, searches for a project, performs validation with edits, and logs out.
Case 28: Rejected Annotator
Annotator logs in, searches for a rejected project, reviews rejection, and logs out.
Case 29: Configuration
Admin logs in and configures settings.
Case 30: Data View
Admin logs in and views project data.

Test report:

Total Tests Conducted: 30

Results:

Passed Tests: 27 tests passed successfully, demonstrating expected outcomes in functionalities
like login, user creation, project management, and file uploads.
Failed Tests: 3

Bug Details:

Default User Role Assignment: When creating a user without specifying a role, the system
defaulted to the "guest" role. This needs clarification or a mandatory role selection.

Phone Number Validation: Entering an incorrect phone number format caused the website to
crash, indicating a need for better input validation and error handling.

Performance Issues: The website occasionally experienced slow loading times and displayed
404 errors, suggesting server-side issues or inefficient configurations.

Recommendations:

Role Selection Enforcement: Modify the system to make role selection mandatory during user
creation or clearly indicate default roles.

Input Validation and Error Handling: Implement frontend validation for phone numbers and
improve backend error handling to prevent crashes.

Server and Performance Review: Investigate and address the causes of slow loading and 404
errors to enhance website stability and performance.

Conclusion: While the majority of the tests confirmed the system’s functionalities are working
as intended, addressing the identified issues is essential for a smoother and more reliable user
experience.
