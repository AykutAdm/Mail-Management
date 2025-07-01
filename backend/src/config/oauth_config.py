GOOGLE_CLIENT_ID = "your-google-client-id-here"
GOOGLE_CLIENT_SECRET = "your-google-client-secret-here"
GOOGLE_REDIRECT_URI = "http://localhost:8000/api/mail-accounts/gmail/callback"
GOOGLE_AUTH_URI = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URI = "https://oauth2.googleapis.com/token"
GOOGLE_SCOPE = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://mail.google.com/"  # Kalıcı silme işlemi için gerekli scope
]

# Frontend URL for redirecting after OAuth process
FRONTEND_URL = "http://localhost:5173" 