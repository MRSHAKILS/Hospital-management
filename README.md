# 🏥 HMS - Hospital Management System

A comprehensive Hospital Management System built with Django that streamlines healthcare operations, appointment scheduling, and patient management with role-based access control.



## 🌟 Features

### 👥 User Management
- **Custom User Authentication** with email-based login
- **Role-based Access Control** (Doctor, Patient, Admin)
- **Dynamic Dashboard Visibility** based on user roles
- **User Registration** with automatic profile creation
- **Secure Login/Logout** functionality

### 🩺 Doctor Features
- **Doctor Dashboard** with appointment overview
- **Appointment Management** (view, cancel, complete, activate)
- **Medical Records** creation and editing
- **Lab Test Management** with results tracking
- **Prescription Management** 
- **Patient History** access
- **Video Call Integration** for telemedicine
- **Notification System** for new appointments

### 🤒 Patient Features
- **Patient Dashboard** with personal health overview
- **Service Browsing** and doctor selection
- **Online Appointment Booking** with real-time availability
- **Payment Processing** with billing management
- **Appointment History** and status tracking
- **Medical Records** viewing
- **Notification System** for appointment updates
- **Profile Management** with personal information

### 💰 Billing & Payments
- **Automated Billing** generation with tax calculation
- **Multiple Payment Status** tracking (Paid/Unpaid)
- **Payment Confirmation** with detailed receipts
- **Email Confirmations** after successful payments

### 📧 Email System
- **Professional Email Templates** (HTML + Text)
- **Appointment Confirmations** with complete details
- **SMTP Integration** with Gmail support
- **Error Handling** for email delivery

### 🏥 Service Management
- **Service Catalog** with detailed descriptions
- **Doctor-Service Associations** 
- **Cost Management** with transparent pricing
- **Service Availability** tracking

### 🔧 Admin Features
- **Jazzmin Admin Interface** with custom branding
- **Comprehensive Data Management** 
- **Import/Export** functionality
- **System Monitoring** and user management
- **Dual Dashboard Access** (Doctor + Patient views)

## 🛠 Tech Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite3 (Development)
- **Frontend**: Bootstrap 5.3.3, HTML5, CSS3, JavaScript
- **Email**: Django Email with SMTP (Gmail)
- **Icons**: Font Awesome 6.0, Bootstrap Icons
- **UI**: Jazzmin Admin Theme
- **Authentication**: Django Custom User Model

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+ 
- pip (Python package manager)
- Virtual environment (recommended)

### 1. Clone the Repository
```bash
git clone https://github.com/MRSHAKILS/Hospital-management.git
cd Hospital-management
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux  
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file or update `settings.py` with your email configuration:
```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## 📱 User Roles & Access

### 🔓 Non-Authenticated Users
- Browse services and doctor information
- Access registration and login pages
- View public content only

### 👨‍⚕️ Doctor Users
- Access Doctor Dashboard exclusively
- Manage appointments and patient records
- Create prescriptions and lab orders
- View patient history and notifications

### 🤒 Patient Users  
- Access Patient Dashboard exclusively
- Book appointments with preferred doctors
- View personal medical history
- Manage profile and payment history

### 👑 Admin/Superuser
- Access both Doctor and Patient dashboards
- Full administrative control
- User management and system oversight
- Data import/export capabilities

## 🎨 UI/UX Features

- **Responsive Design** - Works on all device sizes
- **Modern Bootstrap Interface** - Clean and professional
- **Role-based Navigation** - Dynamic menu based on user type
- **User Type Indicators** - Visual badges showing user roles
- **Professional Email Templates** - Branded HTML emails
- **Intuitive Dashboards** - User-friendly interfaces

## 📧 Email Configuration

The system supports automated email notifications:

### Gmail SMTP Setup
1. Enable 2-Factor Authentication in Gmail
2. Generate App Password
3. Update settings.py with credentials:
```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### Email Features
- Appointment confirmation emails
- Professional HTML + text templates
- Automatic sending after payment
- Error handling and logging

## 🗂 Project Structure

```
HMS/
├── base/                    # Core application logic
├── doctor/                  # Doctor-specific features
├── patient/                 # Patient-specific features  
├── userauths/              # User authentication
├── templates/              # HTML templates
│   ├── base/              # Base app templates
│   ├── doctor/            # Doctor templates
│   ├── patient/           # Patient templates
│   ├── userauths/         # Auth templates
│   ├── emails/            # Email templates
│   └── partials/          # Shared components
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User uploaded files
└── hms_prj/               # Project settings
```

## 🔒 Security Features

- **Custom User Model** with email authentication
- **Role-based Access Control** with proper permissions
- **CSRF Protection** on all forms
- **Secure Password Validation** 
- **Session Management** with automatic logout
- **Input Validation** and sanitization

## 🌐 API Endpoints

### Authentication
- `/auth/sign-up/` - User registration
- `/auth/sign-in/` - User login  
- `/auth/sign-out/` - User logout

### Services & Appointments
- `/` - Homepage with services
- `/service/<id>/` - Service details
- `/book-appointment/<service_id>/<doctor_id>/` - Appointment booking
- `/checkout/<billing_id>/` - Payment checkout
- `/payment-status/<billing_id>/` - Payment confirmation

### Dashboards
- `/doctor/dashboard/` - Doctor dashboard
- `/doctor/appointments/` - Doctor appointments
- `/patient/dashboard/` - Patient dashboard  
- `/patient/appointments/` - Patient appointments

## 🧪 Testing

Run the Django test suite:
```bash
python manage.py test
```

Check for any issues:
```bash
python manage.py check
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues

- Video calling integration requires external service setup
- Email delivery depends on SMTP configuration
- Database is SQLite for development (consider PostgreSQL for production)

## 🔮 Future Enhancements

- [ ] Real-time chat between doctors and patients
- [ ] Mobile app development
- [ ] Advanced reporting and analytics
- [ ] Integration with pharmacy systems
- [ ] Telemedicine video calling
- [ ] Insurance claim management
- [ ] Inventory management for medical supplies

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**MRSHAKILS**
- GitHub: [@MRSHAKILS](https://github.com/MRSHAKILS)
- Project: [Hospital-management](https://github.com/MRSHAKILS/Hospital-management)

## 🙏 Acknowledgments

- Django Documentation and Community
- Bootstrap for responsive UI components
- Font Awesome for beautiful icons
- Jazzmin for enhanced admin interface
- All contributors and testers

---

⭐ **Star this repository if you found it helpful!** ⭐

