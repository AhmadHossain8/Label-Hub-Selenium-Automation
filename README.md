# Label-Hub-Selenium-Automation

This repository focuses on automating test cases for the Label Hub system using Selenium.

---

## Use Cases Covered with the Test Cases

### Login Functionality:
- **Invalid Login**: Verify prevention of invalid login attempts and display of appropriate error messages.
- **Missing Credentials**: Test login behavior when credentials (email or password) are missing.
- **Successful Login**: Validate the ability to login with valid credentials.

### User Management:
- **User Creation**: Confirm user creation with valid input data.
- **Duplicate Username**: Test prevention of creating duplicate usernames.
- **User Deletion**: Verify proper handling and functionality when deleting a user.

### Project Management:
- **Project Creation**: Ensure the creation of projects and prevent duplicate project names.
- **Project Deletion**: Validate that project deletion functionality works as expected.

### File Management and Annotation:
- **File Upload**: Test file upload functionality, including format validation.
- **Annotator Interactions**: Validate the actions and data integrity of annotators during project interactions.

### System Configuration and Data Viewing:
- **Configuration Adjustments**: Verify that system configuration can be modified as required.
- **Secure Data Viewing**: Ensure that only authorized users can view sensitive project data.

---

## Test Case Design Strategy

### Comprehensive Coverage:
The test cases provide broad coverage across multiple key functionalities, including:
- Authentication
- User and project management
- File handling
- System configuration

### Negative Testing:
Many test cases focus on **negative scenarios** (e.g., attempting to create users with invalid data) to ensure that error handling mechanisms are in place and function correctly.

### Role-Based Testing:
Different roles, such as **Admin**, **Annotator**, and **Validator**, are thoroughly tested to ensure proper role-based access control and functionality.

### Edge Cases:
Special attention is given to edge cases, such as:
- Overly long names
- Invalid email formats
- Incorrect password requirements

---

## Test Case Implementation Details

### Selenium Automation:
Selenium, a browser automation tool, is used to implement all test cases, allowing for dynamic interaction with the web application.

### Modular Design:
Each test case is written as a **separate function** (e.g., `Login`, `UserCreate`, `ProjectCreate`) to promote **reusability** and **readability**. This modular approach ensures that test cases are easier to maintain and scale.


# Test Cases

This document lists and describes various test cases for user login, user creation, project management, and other operations in the system.

## User Login

1. **Case 1: Wrong ID**
   - Description: Attempt to login with an incorrect email ID.

2. **Case 2: Without Password**
   - Description: Attempt to login with an email but without providing a password.

3. **Case 3: Without ID and Password**
   - Description: Attempt to login with both email and password fields left empty.

4. **Case 4: Without ID**
   - Description: Attempt to login without providing an email but with a password.

5. **Case 5: Only Part of the Email**
   - Description: Attempt to login with an incomplete email.

6. **Case 6: Correct ID and Password**
   - Description: Successfully login with the correct email and password.

## User Creation

7. **Case 7: Create User without Role**
   - Description: Attempt to create a user without specifying a role.

8. **Case 8: Create User without Email**
   - Description: Attempt to create a user without providing an email.

9. **Case 9: Create User without Password Requirement**
   - Description: Attempt to create a user with an inadequate password.

10. **Case 10: Create User without Name**
    - Description: Attempt to create a user without providing a name.

11. **Case 11: Create User with All Valid Info**
    - Description: Successfully create a user with all required and valid information.

12. **Case 12: Create User with Password Size >14**
    - Description: Create a user with an excessively long password.

13. **Case 13: Create User with Big Name**
    - Description: Create a user with an overly long name.

14. **Case 14: Create User without Gender**
    - Description: Attempt to create a user without specifying a gender.

15. **Case 15: Create User without Valid Email**
    - Description: Attempt to create a user with an invalid email format.

16. **Case 16: Create User with Non-Integer Mobile Number**
    - Description: Attempt to create a user with an invalid mobile number format.

17. **Case 17: Delete a User**
    - Description: Successfully delete a user.

## Logout

18. **Case 18: Logout**
    - Description: Successfully log out.

## Project Management

19. **Case 19: Create User with Mobile Number <11 Digits**
    - Description: Attempt to create a user with a short mobile number.

20. **Case 20: Create User with Mobile Number >11 Digits**
    - Description: Attempt to create a user with a long mobile number.

21. **Case 21: Create New Project**
    - Description: Successfully create a new project.

22. **Case 22: Create Duplicate Project**
    - Description: Attempt to create a project with a name that already exists.

23. **Case 23: Delete Project**
    - Description: Successfully delete a project.

24. **Case 24: File Upload in Project**
    - Description: Successfully upload a file to a project.

## Role-Based Actions

25. **Case 25: Annotator**
    - Description: Annotator logs in, searches for a project, annotates, and logs out.

26. **Case 26: Validator (No Edit)**
    - Description: Validator logs in, searches for a project, performs validation without edits, and logs out.

27. **Case 27: Validator (Edit)**
    - Description: Validator logs in, searches for a project, performs validation with edits, and logs out.

28. **Case 28: Rejected Annotator**
    - Description: Annotator logs in, searches for a rejected project, reviews rejection, and logs out.

## Admin Actions

29. **Case 29: Configuration**
    - Description: Admin logs in and configures settings.

30. **Case 30: Data View**
    - Description: Admin logs in and views project data.

---

These test cases ensure robust testing of user, project, and admin operations within the system.


# Test report:

Total Tests Conducted: 30

# Test Results

## Passed Tests
27 tests passed successfully, demonstrating expected outcomes in functionalities such as:
- User login
- User creation
- Project management
- File uploads

## Failed Tests
3 tests failed, as detailed below:

### Bug Details

1. **Default User Role Assignment**
   - **Issue**: When creating a user without specifying a role, the system defaulted to the "guest" role.
   - **Expected Behavior**: Either make the role selection mandatory or clearly indicate the default role.
   - **Recommendation**: Modify the system to enforce role selection or clarify the default assignment.

2. **Phone Number Validation**
   - **Issue**: Entering an incorrect phone number format caused the website to crash.
   - **Expected Behavior**: The system should validate phone numbers and handle incorrect inputs gracefully.
   - **Recommendation**: Implement frontend validation for phone numbers and improve backend error handling to prevent crashes.

3. **Performance Issues**
   - **Issue**: The website occasionally experienced slow loading times and displayed 404 errors.
   - **Expected Behavior**: The website should load efficiently and avoid such errors.
   - **Recommendation**: Investigate the server-side issues or configuration inefficiencies causing the slow loading and 404 errors.

## Recommendations

1. **Role Selection Enforcement**
   - Ensure that role selection is mandatory during user creation or provide clearer feedback on default role assignment.

2. **Input Validation and Error Handling**
   - Implement robust frontend validation for phone numbers and improve backend error handling to prevent crashes.

3. **Server and Performance Review**
   - Investigate and resolve the issues causing slow loading times and 404 errors to enhance the stability and performance of the website.

## Conclusion
The majority of tests confirmed that the system's core functionalities are working as intended. However, addressing the identified bugs and performance issues is essential for providing a smoother and more reliable user experience.

