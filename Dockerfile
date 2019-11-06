FROM python:2.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "./cinepy.py"]
# docker build -t nomedaimagem
# docker run -it --rm --name nomedaaplicaçao nomedaimagem



# COPY copia coisas para host docker
# ENTRYPOINT um processo seja o principal processo do container, se o processo morrer o container morre
# ENV variaveis de ambiente para o container
# EXPOSE expor uma porta do container
# RUN executa comandos no container (quanto mais utilizado, mais camadas vai ter no conainer...quanto menos melhor ou concatena em um unico comando RUN)
# VOLUME cria um volume no container
# MAINTAINER é quem escreve o Dockerfile

# determina imagem como base e versão para construir sua propria imagem
# FROM python:3

# add arquivos no host docker
# ADD . /src

# define diretorio raiz do container
# WORKDIR /src

# RUN pip install install requirements.txt

# parametro para entrypoint
# CMD python cinepy.py