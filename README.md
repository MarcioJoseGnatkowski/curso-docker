https://github.com/cod3rcursos/curso-docker

6 O QUE É Docker
	Docker é uma plataforma de código aberto, desenvolvido na linguagem Go e criada pelo próprio Google. Por ser de alto desempenho, o software garante maior facilidade na criação e administração de ambientes isolados, garantindo a rápida disponibilização de programas para o usuário final.

7 - DIFERENÇA ENTRE VM E CONTAINER

A VM carrega vários drivers e vários serviços, tem todo um kernel rodando.

Container só tem os processo instalados necessários ex: MYSQL, Redis e utiliza o kernel da máquina e no caso do windows instala um cliente linux só com os recursos necessários esse cliente tem um kernel. 

8 - O QUE SÃO CONTAINERS
   Segregação de processos no mesmo kernel
   No container eu adiciono vários processos, em um posso colocar o servidor, outro o banco e outro um processo de log ex: Redis. Depois os containers vão se comunicar entre eles.
   


9 - O QUE SÃO IMAGENS DOCKER 
    Modelo de isstema de arquivo somente leitura usado para criar containers.
	A imagens ficam no Registry
    Imagens são criadas apartir do comando build, tem um arquivo de build o dockerfile.
	Docker hub repositório de imagens, renomeadas pos tags.
	Cada mudança na sua imagem vai ser criada uma layer isso facilita reuso.
	
10 - IMAGEM VS CONTAINER
   Na orientação de objetos temos as classes e apartir delas podemos criar inumeros objetos usando a classe como modelo. 
   A imagem docker é como se fosse a classe para criar container como se fossem os objetos. Apartir de uma imagem você pode startar inumeros containers. 
	
11 - ARQUITETURA
    Client - Interface de linha de comandos para poder gerar suas aplicações para acessar ex: 'Kitematic'
	Deamon - Recebe comandos e executa no docker hub (registry) e baixa para a máquina local as imagens.
	Registry - Local das imagens publicas.
	
	
12 - VISÃO GERAL DE INSTALAÇAO
    Linux - Docker clint, engine e container tudo na máquina.
	Windows Mac - Client roda no mac-windows Acessando uma VM docker host
	
	
18 - MEU QUERIDO RUN

Run sempre cria novos containers

--Buscar imagem baixar e executar
docker container run hello-world
	
Comando run faz 4 comandos por de trás dele:
Faz o docker container pull, o docker container create, docker container start e docker container exec.

--versão do bash
bash --version

--versão do docker
docker --version

--Versão do debian, no caso o docker tem uma VM que roda o kernel linux
docker container run debian bash --version

--nome das imagens ativas
docker images
--nome de todas as imagens
docker images -a

--listar  containers rodando (o comando container ls -a faz mesma coisa)
docker ps
--lista todos os containes ativos e inativo[
docker ps -a


-- --rm ele executa o debian mostra  a versão, mas não vai aparecer na lista de containers docker ps -a
docker container run --rm debian bash --version

--Entrou n modo interativo do debian
winpty docker container run -it debian bash

--entrou no debian e cria um arquivo 
touch curso-docker.txt

--lista o arquivo só ls lista tudo
ls curso-docker.txt


21 - CONTAINERS DEVEM TER NOME UNICO

--cria com nome o container
winpty docker container run --name mydebian -it debian bash

--lista com meu nome 
container ls -a

22 - REUTILIZAÇÃO DE CONTAINER

-- Entrar no container para alterar
docker container start -ai mydebian

--adicionar um arquivo
touch curso-docker.txt

--lista os arquivos
ls

--sair
exit;

-- Entrar novamente no container para conferir se a alteração está lá, o A é do apache vai pegar o terminal e anexar (ter acesso) o i é de interativo
docker container start -ai mydebian

--lista os arquivos e está lá ele
ls


23 - CEGO, SURDO E MUDO, SÓ QUE NÃO!

O docker engine tem diversos mecanismos para fazer o isolamento. Mas não faz sentido ter um container totalmete isolado é preciso expor uma porta para acessar um banco por exemplo ou acessar um pasta de configurações da sua máquina ou comunicar entre containers por exemplo se você tem um banco de dado em um container e em outro um back-end.


24 - MAPEAR PORTAS DOS CONTAINERS

	Vamos instalar um servidor chamado nginx e mapear a porta 8080 para acessar da minha máquina para acessar o nginx.

-- a porta 8080 exposta para fora do container, vamos acessar a porta 80 do container apartir  da 8080, 80 é a porta padrão do HTTP, nginx é a imagem que vamos baixar
docker container run -p 8080:80 nginx

--Retorna a pagina do nginx, no casso da minha máquina tem que pegar o ip http://192.168.99.100:8080/, pois o engine roda em uma máquina virtual
curl http://localhost:8080  

--no browser
http://localhost:8080

25 - MAPEAR DIRETORIOS PARA CONTANIERS

--Mapear um volume de uma pasta da máquina host para o container, usando aimagem do nginx

cd desktop/
mkdir curso-docker
cd curso-docker/
mkdir ex-volume
cd ex-volume/
cd ..
code . //abre o visual studio code
cd ex-volume/

-- -v mapear volume, pwd pasta corrente (ex-volume) e vai procurar a pasta sub-pasta not-found e vou mapear para usr... aonde o nginx vai ler o index.html, ou seja vai parar de apontar para pasta padrão do nginx e vai apontar para da minha máquina, nesse caso ela não existe aqui
docker container run -p 8080:80 -v $(pwd)/not-found:/usr/share/nginx/html nginx

--Dentro da pasta ex-volume, criar um arquivo html e apontar para pasta do nginx
docker container run -d -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html nginx


26 - RODAR UM SERVIDOR WEB EM BACKGROUND

Executa o container em background se interção do console, posso consultar logs mas não posso interagir com ele, fica rodando como processo.
--d daemon, e vamos mapear a pasta igual ao item anterior
docker container run -d --name ex-daemon-basic -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html nginx

--para verificar se está rodando
docker container ps
--parar 
docker container stop ex-daemon-basic

27 - GERENCIAR O CONTAINER EM BACKGROUND

Podemos usar o restart, start e stop

docker container start ex-daemon-basic

docker container ps

docker container restart ex-daemon-basic

docker container stop ex-daemon-basic


28 - MANIPULAÇÃO DE CONTAINERS EM MODO DAEMON

--listar containers
docker container ls
docker container list 
docker container ps
docker ps


--Acessando logs de um container
docker container start mydebian

docker container logs mydebian

--mostra em json as caracteristicas do container 
docker container  inspect mydebian

--Mostra versão do linux que ta rodando
docker container exec mydebian uname -or

29 - NOVA SINTAXE DO DOCKER CLIENT

docker container ls
docker image ls
docker volume ls

existem diferenças ex apagar a imagem
-- rmi remover imagem, rm é para containers
docker rmi 'IDimagem'

docker rmi 'IDcontainer'

melhor
docker container rm 'idcontainer'
docker image rm 'idimagem'

DEIXANO DE SER USUÁRIO 

30 - INTRODUÇÃO

Existem várias situação para criar imagens, posso definir imagens para integração continua, ambiente de testes, desenvolvimento mais padronizado. 

Ter ambiente de desenvolvimento parecido com o de produção, mesmos paths, SO, etc.

31 - DIFERENÇAS ENTRE CONTAINER E IMAGEM 

Container: Equivalente a objeto. Container é um processo que tem acesso a um sistema de arquivos formados na imagem.
Imagem: Equivalente a classe, modelo de sistema de arquivo somente leitura formado em camadas que é usado no container.

Container é processo e a imagem é o modelo de sistema de arquivos.

docker container -help
docker image --help
docker volume --help 


32 - ENTENDENDO MELHOR AS IMAGENS

Todas imagens e container tem um hash, é melhor ter identificadores container com nomes, são organizadas em registry, repositórios no docker hub. 

docker image pull redis:latest

--Inspecionar imagens.
docker image inspect redis:latest

--criar uma tag para imagem, redis o cod3r terão o mesmo hash
docker image tag redis:latest cod3r-redis
docker image ls

docker image rm redis:latest cod3r-redis

docker image ls
As tags são ponteiros para imagens especificas para hash especificos.

33 COMANDOS BÁSICOS NO GERENCIAMENTO DE IMAGENS

--baixar a imagem do repositório, mas se vc usar o run ele executa o pull por debaixo dos panos
docker image pull

--lista as imagens
docker image ls

--remover imagens
docker image rm

--lista informações sobre a imagens
docker image inspect 'tag' 

--
docker image tag

--constoi imagens apartir de um arquivo que lista os comandos.
docker container build

--após criar sua imagem buildar e dar uma nova tag, você pode publicar no seu registry local o no docker hub.
docker image push

34 - DOCKER HUB X DOCKER REGISTRY

Registry: serviço que disponibiliza uma API para subir e baixar imagens, posso criar imagens dentro da empresa
Docker Hub: Ele é um produto na nuvem, dentro dele tem o registry e contem interface grafica, dentro do docker hub tem várias imagens oficiais. 

35 - MEU PRIMEIRO BUILD

Criar uma pasta ex: primeiro-build, criar o arquivo Dockerfile (Só o D maiusculo e não tem extensão)

--Imagem que vai se basear e imprimir o texto
FROM nginx:latest
RUN echo <h1> Hello World !</h1> > /usr/share/nginx/html/index.html

--entrar na pasta primeiro-build

--(. é a pasta local do Dockerfile) 
docker image build -tex-simple-build . 

docker image ls 

--executar a imagem na porta 8080
docker container run -p -it 80:80 ex-simpl-build

Conferir pelo navegador pegando IP do engine, pois estou usando toolbox, caso contrário usar localhost:80


36 - USO DAS INSTRUÇÕES DE PREPARAÇÃO

Passar argumentos para o dockerfile, para que possamos persnalizar alguns pontos da nossa imagem. Criar uma pasta build-com-arg,
criar um Dockefile.  

FROM debian
LABEL maintainer 'Aluno Cod3r <aluno at cod3r.com.br>'

ARG S3_BUCKET=files
ENV S3_BUCKET=${S3_BUCKET}

docker image build -t ex-build-arg .

--dou echo na variavel de ambientes e vai imprimir files, valor padrão
docker container run ex-build-arg bash -c 'echo $S3_BUCKET'

--Nesse comando eu compilo a imagem alterando a variavel para myapp
docker image build --build-arg S3_BUCKET=myapp -t ex-build-arg .

--Aqui imprimo a variavel de ambiente da imagem
docker container run ex-build-arg bash -c 'echo $S3_BUCKET'

--Fazendo filtros da imagem, ex: quero o mantendedor da imagem, resultado 'Aluno Cod3r <aluno at cod3r.com.br'
docker image inspect --format="{{index .Config.Labels \"maintainer\"}}" ex-build-arg

37 - USO DE INSTRUÇÕES DE POVOAMENTO

Criar uma pasta build-com-copy
--criar index.html, colocar um link para acessar uma página conteudo.html
--arquivo Dcokerfile, para que o arquivo seja enviado a imagem é preciso executar o copy
FROM nginx:latest
LABEL maintainer 'Aluno Marcio <aluno at marcio.com.br>'

RUN echo <h1>Sem conteudo</h1 > /usr/share/nginx/html/conteudo.html

COPY *.html /usr/share/nginx/html/

--criar imagem apartir da pasta atual
docker image build -t ex-build-copy .

--executar container, pegar ip e jogar no browser
docker container run -p 808:80 ex-build-copy

38 - USO DAS INSTRUÇÕES PARA EXECUÇÃO DO CONTAINER PARTE 1

--Criar uma novas pasta
buil-dev

Criar um servidor em python, com uma página html e um servidor.

39 - USO DAS INSTRUÇÕES PARA EXECUÇÃO DO CONTAINER PARTE 2

Vamos criar um descritor fazer com que esse servidor seja executado e a página hrml seja alimentada.

A cada comando é gerada uma layer, podemos concatenar varios comandos para gerar uma layer.
No final sempre colocar as coisas que mais mudam, assim evitando de recompilar as layers iniciais. 

FROM python:3.6
LABEL maintainer 'Aluno Cod3r <aluno at cod3r.com.br>'

RUN useradd www && \
    mkdir /app && \
    mkdir /log && \
    chown www /log 

USER www
VOLUME /log
WORKDIR /app
EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["run.py"]

-- ENTRYPOINT é o ponto de entrada


--Entrar na pasta buil-dev
docker image build -t ex-build-dev .

--mapear o volume para que possa apontar para o arquivo run.py, pois ele não está copiado para o container
docker container run -it -v $(pwd):/app -p 80:8000 --name python-server ex-build-dev

--container baseado em debian, compartilhando a pasta de um container com outro esa pasta '/log/http-server.log/' é do container criado anteiromente no python é o "logging.basicConfig(filename='/log/http-server.log',"
docker container run -it --volumes-from=python-server debian cat /log/http-server.log

40 - ENVIAR IMAGENS PARA O DOCKER HUB

--Criar conta
--Depois da tag a imagem que quero subir, iss cria uma imagem tageada na minha maquina
docker image tag ex-build-dev marciojose/simple-build:1.0

--Tem que fazer logon
docker login --username=marciojose

--marciojose é o usuário, simple-build é a imagem e 1.0 é a tag que aparece no docker hub
docker image push marciojose/simple-build:1.0

41 - VISÃO GERAL E TIPOS DE REDES

Os containers pertencem a mesma rede, mas é possível configurar.

A bridge é a rede diponibilizada pelo docker.
 
Tipos de redes:
None Network: quando não precisa acessar nada externo.
Bridge Network: é uma ponte entre container's e o host para ter acesso a internet
Host Network: Tirar a ponte e acessar direto a interface do host.

docker network ls

42 - REDE TIPO NONE (SEM REDE)

Não tem acesso nenhum ao mundo externo nem entre si, consegue acessar via terminal a volumes e tal.

docker container run -d --net none debian

-- --rm para remover após a execução
docker container run --rm alpine ash -c "ifconfig"

docker container run --rm --net none alpine ash -c "ifconfig"

43 - REDE TIPO Bridge

-- 
docker network inspect bridge

docker container run -d --name container1 alpine sleep 1000

docker container run -d --name container2 alpine sleep 1000

--ping de um container em outro o IP é do container 2
docker container exec -it container1 ping 127.25.172.255

--Fazer ping apartir do container1 para o google
docker container exec -it container1 ping www.google.com.br

--criar nova rede chamada nova_rede
docker network create --driver bridge rede_nova

--ela vai ter seu IP
docker network inspect rede_nova

--criar container com a nova rede
docker container run -d --name container3 --net rede_nova alpine sleep 1000

docker container exec -it container3 ifconfig

docker inspect container1

docker container exec -it container3 ping 172.17.0.2

docker network connect bridge container3 

docker network disconnect bridge container3 

44 - REDE TIPO HOST

Nivel de proteção mais baixa, mas da velocidade já que vc está fazendo acesso direto a máquina host

docker container run -d --name container4 --net host alpine sleep 1000

docker container exec -it container4 ifconfig

SEÇÃO 7  COORDENANDO MULTIPLOS CONTAINERS 

45 - INTRODUÇÃO

É bom disponibilizar todos os elementos em container separados, ex: backend, frontend, banco de dados.
Criar um container para cada serviço.


46 - GERENCIAMENTO DE MICRO SERVICE 

Posso fazer deploys individuais. Ciclo de desenvolvimento mais independente. 

SEÇÃO 8 PROJETO CADASTRO SIMPLES

47 - ESTRUTURA INICIAL

Vamos criar três containers, banco de dados Mongo, front-end uma nginx págin HTML e back-end nodeJS.

Criar um apasta node-mongo-compose e lá vai ter as pastas do projeto com seus arquivos.

Dentro da pasta back-end criar o arquivo package.json
-- Dentro da pasta backend, criar o arquivo descritor do node, mas se não tiver o node na máquina esse comando não vai funcionar. 
npm init -y

--Aqui ele vai instalar as dependencias, mas não precisa desse comando, pois o package.json vai fazer isso
rpm i --save express@4.15.3 mongoose@4.11.1 node-restful@0.2.6 body-parser@1.17.2 cors@2.8.3




 

	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
