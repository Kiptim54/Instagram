from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_message(name, receiver):
    '''
    message to memeber
    '''
    subject='Welcome to Moringa Tribune'
    sender='kiptim54@gmail.com'

    #passing in the context variables
    text_content=render_to_string('email/welcomeemail.txt'),{'name':name}
    html_content=render_to_string('email/welcomeemail.html', {"name":name})
    msg=EmailMultiAlternatives(subject,text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()