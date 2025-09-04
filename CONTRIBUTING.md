# Contributing to HMS - Hospital Management System

Thank you for your interest in contributing to the Hospital Management System! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Django 4.2+
- Git
- Basic knowledge of Django, HTML, CSS, and JavaScript

### Setting Up Development Environment

1. **Fork the Repository**
   ```bash
   # Click the "Fork" button on GitHub
   # Clone your forked repository
   git clone https://github.com/YOUR_USERNAME/Hospital-management.git
   cd Hospital-management
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## 🎯 How to Contribute

### Reporting Bugs
- Use the GitHub Issues tab
- Provide detailed description of the bug
- Include steps to reproduce
- Mention your environment (OS, Python version, Django version)

### Suggesting Features
- Open an issue with the "enhancement" label
- Clearly describe the feature and its benefits
- Provide mockups or examples if possible

### Code Contributions

#### 1. Choose an Issue
- Look for issues labeled "good first issue" for beginners
- Comment on the issue to let others know you're working on it

#### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
```

#### 3. Make Changes
- Follow the coding standards (see below)
- Write clear, concise commit messages
- Test your changes thoroughly

#### 4. Submit Pull Request
- Push your branch to your forked repository
- Create a pull request with a clear title and description
- Reference any related issues

## 📝 Coding Standards

### Python/Django Code
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Use Django best practices

### HTML/CSS
- Use semantic HTML elements
- Follow Bootstrap conventions
- Keep CSS organized and commented
- Ensure responsive design

### JavaScript
- Use modern ES6+ syntax
- Add comments for complex logic
- Follow consistent naming conventions

### Database
- Use descriptive model names
- Add helpful comments to complex queries
- Follow Django ORM best practices

## 🧪 Testing

### Running Tests
```bash
python manage.py test
```

### Writing Tests
- Write tests for new features
- Include both positive and negative test cases
- Test edge cases and error conditions
- Follow Django testing conventions

### Test Coverage
- Aim for high test coverage on new code
- Run coverage reports:
```bash
coverage run --source='.' manage.py test
coverage report
```

## 📚 Documentation

### Code Documentation
- Add docstrings to all functions and classes
- Comment complex business logic
- Update README.md if needed

### API Documentation
- Document any new API endpoints
- Include request/response examples
- Update API documentation

## 🔍 Code Review Process

### For Contributors
- Ensure your code follows the style guidelines
- Write clear commit messages
- Include tests for new functionality
- Update documentation as needed

### For Reviewers
- Be constructive and helpful in feedback
- Test the changes locally if possible
- Check for security implications
- Verify documentation is updated

## 🚦 Pull Request Guidelines

### Before Submitting
- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] No merge conflicts with main branch

### PR Description Should Include
- Summary of changes
- Related issue numbers
- Testing steps
- Screenshots (for UI changes)
- Any breaking changes

## 🔒 Security

### Reporting Security Issues
- Do NOT create public issues for security vulnerabilities
- Email security concerns to: [maintainer-email]
- Include detailed description and steps to reproduce

### Security Best Practices
- Never commit sensitive data (API keys, passwords)
- Use environment variables for configuration
- Follow Django security best practices
- Validate all user inputs

## 🎨 UI/UX Guidelines

### Design Principles
- Keep it simple and intuitive
- Ensure accessibility compliance
- Maintain consistency with existing design
- Test on different screen sizes

### Bootstrap Usage
- Use existing Bootstrap components when possible
- Follow Bootstrap conventions for spacing and layout
- Ensure responsive design principles

## 📋 Issue Templates

### Bug Report Template
```
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment**
- OS: [e.g. Windows 10]
- Python version: [e.g. 3.9]
- Django version: [e.g. 4.2.2]
```

### Feature Request Template
```
**Is your feature request related to a problem?**
A clear description of what the problem is.

**Describe the solution you'd like**
What you want to happen.

**Additional context**
Any other context or screenshots.
```

## 🏷️ Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `documentation` - Improvements to documentation
- `question` - Further information is requested

## 🤝 Community Guidelines

### Be Respectful
- Treat everyone with respect and kindness
- Be patient with beginners
- Provide constructive feedback
- Help create a welcoming environment

### Communication
- Use clear and professional language
- Ask questions when unsure
- Provide helpful and detailed responses
- Be open to feedback and suggestions

## 📞 Getting Help

### Questions or Issues
- Check existing issues and documentation first
- Use GitHub Discussions for questions
- Join our community chat (if available)
- Tag maintainers in issues when appropriate

### Maintainers
- [@MRSHAKILS](https://github.com/MRSHAKILS) - Project Owner

Thank you for contributing to HMS! 🏥✨
