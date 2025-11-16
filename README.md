# CamFiesta 📷

A modern e-commerce platform for camera equipment featuring an AI-powered chatbot assistant.

## Overview

CamFiesta is a Django-based e-commerce website specializing in camera sales. The platform features a comprehensive product catalog, user authentication, shopping cart functionality, order management, and an intelligent AI chatbot powered by Google's Gemini API to assist customers with photography-related queries.

## Features

### 🛍️ E-Commerce Functionality
- **Product Catalog**: Browse cameras from various brands (Canon, Sony, Fuji, GoPro, etc.)
- **Category Filtering**: Filter products by camera categories
- **Product Details**: Detailed product pages with images, descriptions, and specifications
- **Image Gallery**: Multiple product images with interactive gallery view
- **Search**: Advanced search functionality with similar product suggestions
- **Reviews & Ratings**: Customer reviews and ratings system

### 🛒 Shopping Experience
- **Shopping Cart**: Add, update, and remove items from cart
- **Cart Management**: Real-time cart updates with quantity adjustment
- **Order Processing**: Seamless checkout process
- **Order History**: Track past orders and order details
- **Invoice Generation**: Download PDF invoices for orders

### 👤 User Management
- **User Registration**: Create new accounts with email verification
- **User Authentication**: Secure login/logout functionality
- **User Profiles**: Manage personal information and addresses
- **Password Management**: Password reset and profile password update
- **Profile Completion Middleware**: Ensures complete user profiles

### 🤖 AI Chatbot Assistant
- **Gemini-Powered**: Uses Google's Gemini 2.0 Flash model
- **Photography Expert**: Specialized in camera and photography advice
- **Real-time Responses**: Instant answers to photography questions
- **Contextual Understanding**: Maintains conversation context
- **Available on All Pages**: Chatbot accessible on home and product pages

### 📱 User Interface
- **Responsive Design**: Mobile-friendly interface
- **Modern UI**: Clean, professional design with smooth animations
- **Interactive Elements**: Hover effects, transitions, and loading states
- **Sticky Navigation**: Easy access to navigation from anywhere
- **Product Image Zoom**: Detailed product image viewing

## Technology Stack

### Backend
- **Framework**: Django 5.2.5
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: Django Auth
- **File Storage**: Local storage / Azure Blob Storage (production)

### Frontend
- **HTML5 & CSS3**: Modern web standards
- **JavaScript**: Vanilla JS for interactivity
- **Font Awesome**: Icon library
- **Responsive Design**: Mobile-first approach

### AI & APIs
- **Google Gemini API**: AI chatbot functionality
- **google-generativeai**: Python client for Gemini
- **python-dotenv**: Environment variable management

### Additional Libraries
- **Pillow**: Image processing
- **ReportLab**: PDF generation for invoices
- **WhiteNoise**: Static file serving
- **Gunicorn**: WSGI HTTP Server (production)

## Project Structure

```
camfiesta/
├── camfiesta/              # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── production.py      # Production settings
├── myapp/                 # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # App URL routing
│   ├── forms.py           # Django forms
│   ├── admin.py           # Admin configuration
│   ├── middleware.py      # Custom middleware
│   ├── signals.py         # Django signals
│   ├── chatbot_logic.py   # Chatbot AI logic
│   ├── templates/         # HTML templates
│   ├── static/            # Static files (CSS, JS, images)
│   └── migrations/        # Database migrations
├── media/                 # User-uploaded files
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
├── .env                  # Environment variables (not in repo)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### 1. Clone the Repository
```bash
git clone https://github.com/arjuntanil/CamFiesta2.git
cd CamFiesta2
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=True
```

**Get Gemini API Key:**
1. Visit https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Create a new API key
4. Copy and paste into `.env` file

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Configuration

### Admin Panel
Access the admin panel at `http://127.0.0.1:8000/admin/`
- Add products, categories, and manage orders
- View and moderate user reviews
- Manage user accounts

### Chatbot Configuration
The chatbot is configured in `myapp/chatbot_logic.py`:
- **Model**: Gemini 2.0 Flash
- **Timeout**: 30 seconds
- **Context**: Photography and camera expertise
- **Response Length**: Under 100 words (configurable)

### Database Models

**User Profile**
- Extended user model with address and phone number

**Product**
- Name, description, price, category
- Multiple images support
- Stock tracking

**Category**
- Product categorization

**Cart & CartItem**
- Shopping cart management
- Quantity tracking

**Order & OrderItem**
- Order processing
- Order history
- Status tracking

**Review**
- Product reviews
- User ratings

## Usage

### For Customers
1. **Browse Products**: Visit home page to see all cameras
2. **Search**: Use search bar to find specific products
3. **Filter**: Select categories to filter products
4. **View Details**: Click on products for detailed information
5. **Add to Cart**: Select quantity and add items to cart
6. **Checkout**: Review cart and place order
7. **Track Orders**: View order history in profile
8. **Ask Chatbot**: Click chat icon for photography advice

### For Administrators
1. **Login**: Access `/admin/` with superuser credentials
2. **Add Products**: Upload product images and details
3. **Manage Orders**: Update order status
4. **Review Management**: Moderate customer reviews
5. **User Management**: View and manage user accounts

## API Integration

### Gemini AI Chatbot
- **Endpoint**: `/chatbot/`
- **Method**: POST
- **Request Body**: `{ "message": "user question" }`
- **Response**: `{ "response": "AI response" }`

## Security Features

- CSRF protection enabled
- Password validation (minimum 4 characters, 2 digits)
- Secure session management
- SQL injection protection (Django ORM)
- XSS protection
- Login required for sensitive operations

## Performance Optimization

- Static file compression with WhiteNoise
- Database query optimization
- Image optimization
- Lazy loading for images
- Caching headers
- Efficient database indexing

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Contributing

This is a student project. For any suggestions or issues, please contact the repository owner.

## License

This project is developed for educational purposes.

## Contact & Support

- **GitHub**: [arjuntanil](https://github.com/arjuntanil)
- **Repository**: [CamFiesta2](https://github.com/arjuntanil/CamFiesta2)
- **Email**: arjuntanil123@gmail.com

## Acknowledgments

- Google Gemini API for AI chatbot functionality
- Django framework and community
- Font Awesome for icons
- All open-source libraries used in this project

## Future Enhancements

- Payment gateway integration (Stripe/Razorpay)
- Email notifications for orders
- Wishlist functionality
- Product comparison feature
- Advanced filtering (price range, brand)
- Real-time inventory tracking
- Customer support ticket system
- Social media integration
- Product recommendations based on browsing history
- Multi-language support

---

**Version**: 1.0.0  
**Last Updated**: November 2025  
**Status**: Active Development
