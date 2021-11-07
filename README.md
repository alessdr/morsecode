# Morse Code Interpreter


## Descrição

Este projeto tem o intuíto de atuar como uma pequena aplicação web, que possibilitará a seu usuário traduzir **código morse** para texto e vice-versa.


## Tecnologias empregadas

Para o desenvolvimento de nossa aplicação tomamos como base as seguintes tecnologias:

* Backend: Python
* Frontend: HTML5, CSS e JS

Durante o processo de desenvolvimento, foram utilizadas algumas libs de apoio, tanto no Frontend quanto no Backend, para facilitar sua implementação.
As principais libs utilizadas foram:

* Frontend:
  * [Bootstrap](https://getbootstrap.com/)
  * [Socket.io](https://socket.io/)
* Backend:
  * [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  * [Gunicorn](https://gunicorn.org/)
  * [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
  * [Simple-WebSocket](https://pypi.org/project/simple-websocket/)


## Fluxo de funcionamento

![Fluxo de Funcionamento](./images/fluxo.png)


## Arquitetura inicial


## Arquitetura ideal

Não existe um padrão de arquitetura que resolva todos os problemas de todas as aplicações. Cada caso é um caso particular que deve ser estudado com atenção e cuidados.

Para nosso exemplo acima, por se tratar de uma aplicação web simple que nem banco de dados utiliza, podemos sugerir alguns modelos que atenderiam as necessidades de escalar a aplicação para grandes quantidades de usuários, que por sua vez, se traduz em elevado número de acessos.

Seja abaixo alguns modelos sugeridos.


### Nuvem AWS:

Supondo que nossa aplicação foi instalada em um servidor **EC2** (Elastic Compute Cloud) da Amazon Web Server (AWS), poderíamos nos valer de um escalonamento horizontal (criação de servidores em paralelo, e preferencialmente em zonas diferentes para garantir disponibilidade), com a utilização do serviço **Auto Scaling**.

Este serviço utiliza-se do **Cloud Watch** (outro serviço da AWS) para monitorar um servidor específico (ou pull de servidores). Com base em métricas definidas, quando um valor X é atingido, ele envia uma notificação via **SNS** (outro serviço da AWS) para o serviço EC2, afim de que este último crie e instancie um novo servidor, e o introduza em nosso pull de recursos, com isso garantindo completo atendimento aos nossos usuários.

Para complementar, da mesma forma que o **Auto Scaling** é utilizado para aumentar nossos recursos, também pode ser utilizado para diminuí-los.
### 


## Pré-Requisitos

* Git
* Docker

## Execução

Como o projeto foi desenvolvido e preparado para container (Docker), não será preciso várias ferramentas, linguagens, bibliotecas e compiladores. Para executa-lô, basta seguir os passos abaixo:

1) Clonar o repositório em sua máquina
```
git clone git@github.com:alessdr/morsecode.git
```

2) Criar a imagem docker com o código clonado
```
docker build -t morse . 
```

3) Criar/executar o container 
```
docker run -d --rm --name morse -p 5000:5000 morse
```

4) Abrir o browser e acessar o endereço abaixo
```
http://127.0.0.1:5000
```
