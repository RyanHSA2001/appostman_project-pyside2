import socket
from string import Template

import smtplib
import imaplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def auth_smtp(smtp_server:str, port_:str, email_address:str, password:str):
    try:
        # cria a conexão SMTP
        smtp_connection = smtplib.SMTP(smtp_server, port_)
        # inicia a criptografia
        smtp_connection.starttls()
        # loga no servidor SMTP
        smtp_connection.login(email_address, password)
        # encerra a conexão
        smtp_connection.quit()

        # chegando até aqui os dados são válidos
        return True

    # caso dispare qualquer exceção, os dados são inválidos.
    except socket.gaierror:
        return False
    except smtplib.SMTPServerDisconnected:
        return False


def auth_imap(imap_server: str, port_: str, email_address: str, password: str):

    # Cria a conexão IMAP
    imap_connection = imaplib.IMAP4_SSL(imap_server, port_)

    # Loga no servidor IMAP
    imap_connection.login(email_address, password)

    # Encerra a conexão
    imap_connection.logout()

    # Chegando até aqui, os dados são válidos
    return True

# Caso dispare qualquer exceção, os dados são inválidos.

