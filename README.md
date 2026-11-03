<div align="center">
  
  <h1>🚀 Django Job Portal</h1>
  <p>A Full Stack Web Application connecting top talent with industry-leading employers.</p>

  <!-- Badges -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  </a>
  <a href="https://www.sqlite.org/index.html">
    <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  </a>
  <a href="https://github.com/DevYash-001/job-portal">
    <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge" alt="Maintained" />
  </a>
</div>

<br />

## 📑 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Application Workflow](#-application-workflow)
- [Technology Stack](#-technology-stack)
- [Project Architecture](#-project-architecture)
- [Database Design](#-database-design)
- [Installation and Setup (Windows)](#-installation-and-setup-windows)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About the Project

The **Django Job Portal** is a robust, full-stack web application designed to bridge the gap between job seekers and employers. Built with Python and Django Web Development principles, the platform streamlines the recruitment process through role-based dashboards, secure authentication, and seamless CRUD operations for job postings and applications.

**Target Users:**
- **Job Seekers:** Professionals looking for new career opportunities.
- **Employers/Recruiters:** Companies aiming to post vacancies and manage incoming applications.

---

## ✨ Key Features

### 🔐 Authentication and Authorization
- **Role-Based Access Control:** Custom user models supporting distinct `Job Seeker` and `Employer` profiles.
- **Dedicated Registration:** Separate, optimized registration workflows for companies and candidates.
- **Secure Sessions:** Django-backed secure session management and password hashing.

### 🏢 Employer Features (Implemented & Planned)
- **Company Profiles:** Establish and manage corporate branding and details.
- **Job Management (CRUD):** Post, update, view, and delete job listings.
- **Applicant Tracking:** Review incoming applications via a dedicated employer dashboard.

### 🧑‍💻 Job Seeker Features (Implemented & Planned)
- **Job Discovery:** Browse and view detailed job postings.
- **Application Workflows:** Apply to positions directly through the portal.
- **Candidate Dashboard:** Track application statuses and manage personal profiles.

---

## 📸 Application Screenshots

<div align="center">
  <table>
    <tr>
      <td align="center"><b>Home Page</b><br><img src="docs/screenshots/home-page.png" alt="Home Page" width="400"/></td>
      <td align="center"><b>Employer Dashboard</b><br><img src="docs/screenshots/employer-dashboard.png" alt="Employer Dashboard" width="400"/></td>
    </tr>
    <tr>
      <td align="center"><b>Role-Based Registration</b><br><img src="docs/screenshots/registration.png" alt="Registration" width="400"/></td>
      <td align="center"><b>Job Listings</b><br><img src="docs/screenshots/job-listings.png" alt="Job Listings" width="400"/></td>
    </tr>
  </table>
</div>

> *Note: Screenshots represent the current UI state. Placeholders are used above until final repository images are captured.*

---

## 🛠️ Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Backend** | Python, Django |
| **Frontend** | HTML5, CSS3, Django Templates |
| **Database** | SQLite (Development) / PostgreSQL (Ready) |
| **Architecture** | MVT (Model-View-Template) |
| **Media/Static** | Django File Handling |

---

## 🏗️ Project Architecture

The application is structured into five highly cohesive, decoupled Django apps ensuring modular Full Stack Development:

*   **`accounts`**: Manages the custom authentication system and role-based profiles.
*   **`companies`**: Handles employer company profiles and branding.
*   **`jobs`**: Core CRUD operations for job postings and requirement specifications.
*   **`applications`**: Tracks the many-to-many relationship between users and jobs.
*   **`dashboard`**: Provides centralized, role-specific views for metrics and management.

---

## ⚙️ Installation and Setup (Windows)

This project requires **Python 3.8+**. The following instructions are optimized for Windows 11 PowerShell.

<details>
<summary><b>Click to view installation instructions</b></summary>

1. **Clone the repository**
   ```powershell
   git clone [https://github.com/DevYash-001/job-portal.git](https://github.com/DevYash-001/job-portal.git)
   cd job-portal
