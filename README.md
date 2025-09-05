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
