import logging
import http.server
import socketserver
import getpass

#Classe  MyHTTPHandler herdar de http.server.SimpleHTTPRequestHandler
#Reescrever o método log_message, personalizar 
#Logar IP e Data e passar os argumentos
class MyHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info("%s - - [%s] %s\n"% (
            self.client_address[0],
            self.log_date_time_string(),
            format%args
        ))
#Passar o nome do arquvio que quero logar
#Formatação do log, tempo e mensagem

logging.basicConfig(
    filename='/log/http-server.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#Logar que ta iniciando o processo
#Definir a porta 8000
logging.getLogger().addHandler(logging.StreamHandler())
logging.info('inicializando...')
PORT = 8000

#Passando a porta e o handler da classe  
#E do método reescrito
#E por ultimo iniciar o servidor nessa porta
httpd = socketserver.TCPServer(("", PORT), MyHTTPHandler) 
logging.info('escutando a porta:%s', PORT)
logging.info('usuario: %s', getpass.getuser())
httpd.serve_forever() 
