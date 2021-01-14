# Python-to-.exe
Como Converter seu programa .py para .exe para Windows? bem, de forma bem simples a primeira coisa a se fazer é instalar a biblioteca do pyinstaller no seu ambiente.
Detalhe importante! não precisa ter o python instalado na máquina para rodar o programa exe. =)

## Passo 1:
Abra o console(CMD ou Prompt no Anaconda) e digite: pip install pyinstaller

## Passo 2:
Pegue os arquivos .py que compoem seu programa e movam para o diretório de instalação do Python na sua máquina: C:\Users\SeuUsuário\AppData\Local\Programs\Python\Python38-32\Scripts
É claro que esse diretório pode mudar dependendo da instalação do Python na sua máquina. Ah! eu tentei fazer esse procedimento direto no diretório de desenvolvimento, no meu caso eu uso o Anaconda, e o meu relato é que não deu certo, por isso que optei por mover os arquivos .py para o diretório do exe. do python conforme diretório descrito no início desse artigo.

## Passo 3:
Ok, temos agora o arquivo do seu programa .py no diretório da instalação do Python na sua máquina, navegue no prompt de comando até o diretório da instalação do Python em sua máquina, no Windows:

cd C:\Users\SeuUsuário\AppData\Local\Programs\Python\Python38-32\Scripts

Agora com o simples comando: pyinstaller --onedir -- seuarquivomain.py
espere até que todo o processo seja completo e pronto agora temos duas pastas criadas dentro do diretório o Dist e o build, o programa.exe está na pasta Dist. 

 - Outra dica importante é que caso você deseje debugar o programa, você pode utilizar o seguinte comando:
      pyinstaller --onedir --debug all seuarquivomain.py

Para então efetuar o debug do sistema, basta abrir o cmd e executar main.exe por lá =)

Deixei um exemplo de código bem simples(InterfaceGUI.py) que utiliza interface gráfica com a biblioteca Tkinter, ele apenas abre uma tela de seleção de arquivo e depois exibe uma mensagem, pode ser facilmente utilizado para treinar o procedimento de converter arquivo .py para .exe


É isso =)

