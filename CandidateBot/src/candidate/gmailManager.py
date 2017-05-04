from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from io import StringIO
from email.mime.text import MIMEText
import base64

projDir = 'C:/Users/David/Desktop/RandomPessoal/Projects/'
storageDir = projDir + 'storage.json'
cliSecDir = projDir + 'client_secret.json'

def getCredentials(cliSecDir, storageDir):
    #scope maximum
    SCOPES = 'https://mail.google.com/'
    store = file.Storage(storageDir)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(cliSecDir, SCOPES)
        creds = tools.run_flow(flow, store)
    gmail = discovery.build('gmail', 'v1', http=creds.authorize(Http()))
    return gmail

gmail = getCredentials(cliSecDir, storageDir)
threads = gmail.users().threads()
def getListOfAllThreads(gmail):
    return gmail.users().threads().list(userId='me').execute().get('threads', [])


def send_message(service, user_id, message):
    """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print ('Message Id: %s' % message['id'])
        return message
    except:
        print ('An error occurred: %s' % error)


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}
    messages = gmail.users().messages()
    message = messages.send(userId='me', body=body).execute()
    #return {'raw': base64.urlsafe_b64encode(message.as_string())}

mss = create_message('me', 'david.dbmoura@gmail.com', 'testePython', 'esta um belo dia')
#send_message(gmail, 'me', mss)

#for t in ts:
    #dt = threads.get(userId='me', id=t['id']).execute()
    #nms = len(dt['messages'])
    #print(nms)
    
    
#threads = GMAIL.users().threads().list(userId='me').execute().get('threads', [])
#for thread in threads:
#    tdata = GMAIL.users().threads().get(userId='me', id=thread['id']).execute()
#    nmsgs = len(tdata['messages'])

#    if nmsgs > 2:
#        msg = tdata['messages'][0]['payload']
#        subject = ''
#        for header in msg['headers']:
#            if header['name'] == 'Subject':
#                subject = header['value']
#                break
#        if subject:
#            print('%s (%d msgs)' % (subject, nmsgs))'''
