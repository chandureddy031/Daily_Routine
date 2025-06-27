from imapclient import IMAPClient
from utils.config import Config
import email

def fetch_unread_emails():
    config = Config()
    emails = []
    with IMAPClient(config.IMAP_SERVER) as client:
        client.login(config.IMAP_USER, config.IMAP_PASSWORD)
        client.select_folder('INBOX')
        messages = client.search(['UNSEEN'])
        
        for uid, message_data in client.fetch(messages, 'RFC822').items():
            email_message = email.message_from_bytes(message_data[b'RFC822'])
            body = ""
            if email_message.is_multipart():
                for part in email_message.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = email_message.get_payload(decode=True).decode()
            
            emails.append({
                'subject': email_message['Subject'],
                'from': email_message['From'],
                'body': body
            })
    return emails