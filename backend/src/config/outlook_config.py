# Outlook OAuth 2.0 settings
OUTLOOK_CLIENT_ID = "your-outlook-client-id-here"
OUTLOOK_CLIENT_SECRET = "your-outlook-client-secret-here"
OUTLOOK_REDIRECT_URI = "http://localhost:8000/api/mail-accounts/outlook/callback"
OUTLOOK_AUTH_URI = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
OUTLOOK_TOKEN_URI = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
OUTLOOK_SCOPE = [
    "offline_access",
    "Mail.Read",
    "Mail.Send",
    "User.Read"
] 