# Extrator de Chats do Telegram

Este projeto tem como finalidade principal extrair textos das exportações em JSON de chats do aplicativo de mensagens Telegram.

## Requerimentos

* **Docker Engine**: versão 20.10.18 ou mais recente.
* **Docker Compose**: versão 2.10.2 ou mais recente.

## Scripts

Os scripts estão na pasta `scripts/` e pode ser rodados a partir da pasta do projeto dando primeiro a permissão via `chmod +x ./scripts/*.sh`. Após dada a devida permissão, rode-os usando a sintaxe `./scripts/[nome_script].sh`.

## Entrada e Saída

### Entrada
Para o extrator funcionar corretamente, ele exige um arquivo de entrada que deve ser colocado na pasta `/in` chamado `result.json`, este arquivo pode ser de qualquer chat ou canal exportado do telegram no formato JSON.


### Saída

Após rodar o script, o script python gerará um arquivo `texts.csv` na pasta `/out` com os dados das mensagens de texto extraídas do arquivo `result.json`.

## Como rodar o extrator

1) Após dada a permissão adequada aos scripts:
```
$ ./scripts/up.sh
```

2) Se precisar fazer a construção da imagem novamente para se livrar de erros:

```
$ ./scripts/build.sh
```
Em seguida rode o script do passo 1.

---
Há também um script extra para apagar o container se ocorrer um problema de execução no passo 1:

```
$ ./scripts/down.sh
```

Este script irá rodar o `docker compose down`e apagar todas as configurações do compose seguidas no `docker-compose.yml`.

## Depuração via VS Code:

Há presentes nesse repositório a configuração necessária para realizar a depuração do script caso necessário.

Para realizar a depuração do script `main.py` dentro do container Docker, descomente a linha que está presente no arquivo `Dockerfile`:

```Dockerfile
#CMD python -m debugpy --listen 0.0.0.0:5678 --wait-for-client main.py
```

E comente a linha principal:

```
CMD python main.py
```

Após realizar as alterações no Dockerfile, rode o script do extrator como documentado na seção `Como rodar o extrator` logo acima.

O script só irá rodar depois que o cliente de depuração do VS Code for inicializado corretamente. Veja este vídeo de exemplo no YouTube demostrando seu uso:

https://www.youtube.com/watch?v=ywfsLKRLmf4

## Autores e Contribuidores

Lucas Plus 10

## Licença

[GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)