# Morse Code Interpreter

## Descrição

Este projeto tem o intuíto de atuar como uma pequena aplicação web, que possibilitará a seu usuário traduzir **código morse** para texto e vice-versa.

## Tecnologias empregadas

A aplicação foi desenvolvida com as seguintes tecnologias:

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
