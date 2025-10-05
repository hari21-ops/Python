# ---- Logging Setup ----
```
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
```
# ---- Decrypt Credentials ----
```
key = "$"  # Add your actual encryption key here (must be same used for encryption)
cipher = Fernet(key)
decrypted_password_email = cipher.decrypt(credentials.email_pass).decode()
decrypted_password_domain = cipher.decrypt(credentials.password).decode()
```

# ---- Configuration ----
```
imap_server = '' # Enter your imap server 
imap_port = '' # Mention port
email_user = '' # email id of your account 
email_pass = decrypted_password_email # Provide pwd and decrypt at runtime 
```
```
site_url = '' # As i said we are using it for sharepoint so you place your site url
list_name = '' # name of list on sharepoint
username = credentials.username # username 
password = decrypted_password_domain 
```

# Mention your team members mail ids as dictionary with their id number onboard 

# Below are functions that I have used: 
# def clean_html_body(html): To check html body in msg and filter required content
# def extract_inline_images(message): After getting message, will move on to extracting actual message in email so that we can fill it in ticket
# def extract_email_from_signature(html): Get user email id so that we can lock this ticket is being raised by that user.
# Last one is create_sharepoint_item function I have used here. 

# Due to some reasons I won't be able to paste each and every piece of code. 
# So you can design your own as per your company requirement. 




















