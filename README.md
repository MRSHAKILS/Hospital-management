# Hospital-management

Hospital Management using django as backend. It will have core functionalities of a standard hospital management, Email Authentication, Payment method

Project Update:
Whole project structure has been made
All Database, schema and tables are created (Models.py in every app)
Full admin UI is done
Also, Admin can sign in successfully

## 🔒 Security Configuration

### Environment Variables Setup

This project uses environment variables to keep sensitive information secure. Follow these steps:

#### 1. Create Environment File
```bash
# Copy the example file
cp .env.example .env
```

#### 2. Configure Your Variables
Edit `.env` with your actual values:

```env
# Django Secret Key - Generate a new one for production
SECRET_KEY=your-secret-key-here

# Debug Mode (set to False in production)  
DEBUG=True

# Email Configuration (for Gmail)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Payment Gateway Keys (optional)
STRIPE_SECRET_KEY=your-stripe-secret-key
STRIPE_PUBLIC_KEY=your-stripe-public-key
PAYPAL_CLIENT_ID=your-paypal-client-id
PAYPAL_SECRET_ID=your-paypal-secret-id

# Allowed Hosts (for production)
# ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

#### 3. Gmail Setup for Email
1. Enable 2-Factor Authentication in your Gmail account
2. Generate an App Password:
   - Go to Google Account Settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Use this password in `EMAIL_HOST_PASSWORD`

### 🚨 Security Best Practices

- ✅ **Never commit `.env` files** - They are automatically ignored by Git
- ✅ **Use strong SECRET_KEY** - Generate new ones for each environment
- ✅ **Set DEBUG=False** in production
- ✅ **Use App Passwords** for Gmail, not your regular password
- ✅ **Configure ALLOWED_HOSTS** for production deployments
- ✅ **Regular security updates** - Keep dependencies updated

### 🛠 Installation & Setup

```bash
# Clone repository
git clone https://github.com/MRSHAKILS/Hospital-management.git
cd Hospital-management

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (see above)
cp .env.example .env
# Edit .env with your values

# Database setup
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### 📁 Protected Files

The following sensitive files are automatically ignored by Git:

- `.env` - Environment variables
- `db.sqlite3` - Database file  
- `__pycache__/` - Python cache files
- `media/` - User uploaded files
- `staticfiles/` - Collected static files

### 🔐 Production Deployment

For production deployment:

1. Set `DEBUG=False` in `.env`
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL recommended)
4. Set up proper static file serving
5. Use HTTPS for all communications
6. Regular backups and monitoring