# College Social Network (CSN)

Welcome to the **College Social Network (CSN)** repository! This project aims to enhance communication and collaboration within academic communities by providing a comprehensive platform tailored to the needs of students, faculty, and administrators.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Screenshots](#screenshots)
- [License](#license)

## Project Overview
The **College Social Network** is designed to bridge the gap between students, faculty, and administrators by offering a unified platform for interaction. It supports various academic and social activities, including communication, content sharing, and event organization, enhancing the overall college experience.

### Objectives
- Facilitate easy communication between students, faculty, and administrators.
- Provide a platform for sharing academic resources and announcements.
- Support both private and public interactions within the college community.
- Ensure secure and centralized management of user data and interactions.

## Features
- **User Authentication**: Separate login panels for students, faculty, and administrators with role-based access.
- **Profile Management**: Customizable user profiles highlighting academic achievements, interests, and more.
- **Communication**: Private and public posts, messaging, and interaction tools for students and faculty.
- **Study Materials**: Upload and access academic resources such as notes, documents, and books.
- **Event Management**: Tools for organizing and participating in college events.
- **Admin Dashboard**: Comprehensive control panel for managing users, content, and system settings.

## Technologies Used
### Frontend:
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: To create dynamic and interactive user experiences.
- **Bootstrap**: For responsive design and pre-built UI components.

### Backend:
- **Python**: Core programming language for backend logic.
- **Flask/Django**: Web frameworks for handling requests, routing, and templating.
- **MySQL**: Relational database management system for storing user data.
- **XAMPP**: Local development environment including Apache, MySQL, PHP, and Perl.

## Installation
### Prerequisites
- Python 3.x
- Flask or Django
- MySQL
- XAMPP (for local development)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/csn.git
   cd csn
   ```

2. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   - Configure MySQL with the necessary tables and users as per the provided schema.
   - Update the database connection details in the configuration file.

4. **Run the application**:
   ```bash
   flask run
   ```
   or
   ```bash
   python manage.py runserver
   ```

## Usage
- **Admin**: Manage users, oversee content, and monitor system activities from the admin dashboard.
- **Faculty**: Post announcements, share study materials, and interact with students.
- **Students**: View posts, download study materials, and communicate with peers and faculty.

## Modules
- **Dashboard Module**: Admin interface for managing all aspects of the platform.
- **Settings Module**: Allows admins to customize and configure site settings.
- **Faculty Account Panel**: Interface for faculty to interact with students and manage academic resources.
- **Student Account Panel**: Allows students to manage their profiles, access study materials, and communicate with others.
- **Study Materials Module**: A repository for academic resources uploaded by faculty.

## Screenshots
**Login Page**
![image](https://github.com/user-attachments/assets/6a42678d-0956-4be5-9ec2-eb6830b62e67)

**Admin Login Page**
![image](https://github.com/user-attachments/assets/0dea20c2-9e6e-41f1-be54-71c671b6fa30)

**Faculty Registration Page**
![image](https://github.com/user-attachments/assets/703e0ea1-0bce-4c09-b08b-270d2c2b06e5)

**Faculty Login Page**
![image](https://github.com/user-attachments/assets/57fb6464-5064-419e-934a-820577ec6da7)

**Student Registration Page**
![image](https://github.com/user-attachments/assets/5842c89f-81de-42d2-9e45-c9985c7bf3aa)

**Student Login Page**
![image](https://github.com/user-attachments/assets/17ef33dc-0ab1-4aeb-a307-df1fcaff73f1)

## License
This project is licensed under the MIT License. See the LICENSE file for details.
