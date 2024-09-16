# Automação de Configuração do Aplicativo de Câmeras HikVision

## Descrição

Este projeto é uma automação desenvolvida em Python utilizando as bibliotecas **`pyautogui`** e **`time`** para automatizar o processo de abertura e configuração do aplicativo de câmeras HikVision. A automação foi criada para ser executada ao iniciar o computador, permitindo que os computadores dedicados à portaria de uma empresa possam iniciar e configurar o aplicativo automaticamente, garantindo a exibição correta das câmeras de segurança sem a necessidade de intervenção manual.

A solução foi desenvolvida para reduzir o tempo de configuração manual e evitar erros humanos durante o processo. A automação mapeia todas as posições necessárias na interface do aplicativo, executando as interações como cliques, entradas de teclado e seleções de modo preciso.

  
## Tecnologias Utilizadas

- **Python 3.x**
- **pyautogui**: Biblioteca utilizada para simular as interações com a interface gráfica (cliques, movimentos de mouse, digitação).
- **time**: Biblioteca utilizada para controlar os intervalos entre as interações e garantir que a interface tenha tempo para carregar adequadamente entre as ações.

## Requisitos

Antes de executar a automação, certifique-se de que seu ambiente atenda aos seguintes requisitos:

- Python 3.x instalado.
- Instalar as dependências listadas no arquivo `requirements.txt`:
  ```bash
  pip install -r requirements.txt

## Como usar
1. Certifique-se de que o aplicativo de câmeras HikVision está corretamente instalado e acessível em um diretório conhecido.

2. Adicione o executável da aplicação no Inicializar do Windows (SO) para que ele inicialize automaticamente no login do sistema.

## Configuração
Se houver a necessidade de ajustar o mapeamento das coordenadas (caso a interface do aplicativo ou resolução do monitor seja diferente), siga os passos abaixo:

1. Utilize o comando pyautogui.position() para capturar as coordenadas dos elementos que precisam ser interagidos na interface do aplicativo HikVision.

2. Substitua as coordenadas no script onde as ações correspondentes são realizadas.

## Licença
Este projeto está licenciado sob a MIT License.