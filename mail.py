import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from excel_read import pas_lst


def mail(name, mail_id, type='partners', filename='Dhishna.pdf'):
    print(name, ' | ', mail_id)
    email_send = mail_id
    email_user = 'hr@dhishna.org'

    subject = 'Sponsorship Proposal | Dhishna 2020'

    msg = MIMEMultipart()
    msg['From'] = "Dhishna HR <{}>".format(email_user)
    msg['To'] = email_send
    msg['Subject'] = subject

    body = ''' 

Respected Sir,
 

 We are writing to request for your consideration for sponsorship of Dhishna 2020. Dhishna is the techno-cultural extravaganza, held annually in the School of Engineering, CUSAT Kochi. This annual event is in its ninth year and it is to be held on February 19, 20, 21 2020. Since it’s inception, Dhishna has grown significantly due to the quality of the technical and cultural programs being showcased every year, the publicity and press we have received and the wonderful outdoor venue in the heart of Kerala’s most booming city Kochi. This event is free to the public and has received active participation from all over South India and from over 200 schools and colleges in the state.

Dhishna attracts over 20000 attendees and there have been over 2 million views of our promotional videos on our online pages on Facebook and YouTube in the last six months alone. In addition to features in local news outlets such as The Hindu, The Deccan Chronicle and The Times of India, this tech-fest  has garnered national media attention with features on Asianet News.

Each year Dhishna has grown larger and we expect that it will continue to grow. Dhishna 2019 was a grand success due to the valuable support offered by our strategic and generous sponsors.
    
We would like to build a mutually beneficial  relationship with {0} who share our vision for this tech-fest, who support the advancement of education and technology to unify our society and who would like their marketing and goodwill efforts to reach a large, captive target audience. We believe that your company shares those values and together, we can create a magical and significant event for our local and online communities. As a key sponsor, you can reach not only those attending the festival, but the thousands who view our festival through our website, online handles and Android apps. It is also important for you to know that 100% of your sponsorship funds will be used to promote and fund the event, since our dedicated staff are all students of this institution. 

It was our honour to have your esteemed company as our {1} for Dhishna 2019 and we would like to continue strengthening our ties with you. We humbly request for a meeting where we can consider options to make this mutually beneficial for your company and Dhishna 2020. Any time and venue of your convenience will be perfect for us. I would like to follow up with you in the coming weeks for your insights and look forward to working with you as we continue to grow and develop this amazing event. 



Kindest regards, 
 

Vaishnavi Singh
Sponsorship Head - Dhishna 2020
Ph - +91 8921397119


H Vishnu Das
Sponsorship Head - Dhishna 2020
Ph - +91 9048711970

'''.format(name, type)

    body = 'Hey there, this is mail to test for automatic mailing. Kindly ignore this message. For any enquiries, contact mail@jyothisp.co' + body
    print('--Attaching files.')
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    msg.attach(part)
    text = msg.as_string()
    print('--Sending mail')
    server.sendmail(email_user, email_send, text)
    print('--Mail sent')
    print('********************************************************')


if __name__ == '__main__':
    email_user = 'hr@dhishna.org'
    print('Setting up server')
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    server = smtplib.SMTP('smtp.zoho.com', 587)
    server.starttls()
    print('Logging in')
    server.login(email_user, email_password)
    print('********************************************************')
    company_list = pas_lst()
    for company in company_list:
        mail(*company)
    server.quit()
