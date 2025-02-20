# Análise de sentimento por IA
Uma IA com análise de sentimento interpreta emoções em textos, 
identificando se o tom é positivo ou negativo. 
Ela usa técnicas de processamento de linguagem natural (NLP) e 
aprendizado de máquina para entender palavras, frases e contexto, 
ajudando empresas a monitorar opiniões em redes sociais, 
avaliar feedbacks de clientes e até automatizar respostas com base no sentimento detectado.

## Dependencias
* VSCode: https://code.visualstudio.com/download
* Python: https://www.python.org/downloads/
* Bibliotecas necessárias (Python): sklearn, nltk, joblib e deep_translator
* Comando utilizado para instalação das bibliotecas: pip install scikit-learn NLTK Joblib deep_translator
* Obs: Caso você tente rodar o programa sem ter as bibliotecas necessárias, existe um SCRIPT que perguntará se você não deseja baixar automaticamente. Caso digite "s". Ele realizará o download automaticamente.
  
## Instruções (Necessário ter pelo menos VSCODE e Python para prosseguir para esse passo)
* Clonar o repositório localmente: git clone https://github.com/devmarangoni/IA-Feeling-Analysis.git
* Inicializar o programa: python IAExecuteFeelingAnalysis.py
* Caso você já tenha baixado as bibliotecas necessárias, aparecerá um feedback exatamente como esse:

![image](https://github.com/user-attachments/assets/e3813558-bc97-4aa2-b0e7-06c80adfd6f2)

* Como eu subi a IA treinada no projeto, você também receberá o feedback de que a IA já está treinada.

![image](https://github.com/user-attachments/assets/994e14ac-1b40-4185-87de-347d208f94f6)

* OBS: Caso deseje que ela seja treinada do 0. Basta apagar o diretório chamado "ModelTraining" antes de utilizar o comando de execução.

## Como utilizar
* O processo é básico, ele te pedirá uma frase para que possa identificar se é POSITIVA ou NEGATIVA.

![image](https://github.com/user-attachments/assets/35eb525b-a1a0-4deb-8aaf-5a743eb9fd8c)

* Após informar a frase, ele te dará o feedback se é positiva ou negativa.

![image](https://github.com/user-attachments/assets/cd48e081-0c50-40f8-b6bd-71d11e6f9e40)

* Encerrando o programa: basta digitar "sair" ou pressionar "CTRL + C"

![image](https://github.com/user-attachments/assets/e3aa3904-73f4-4d05-98e4-ae2212c30442)


## Aprendizado com feedback do usuário

Caso você discorde ela será treinada novamente para entender que essa frase que você enviou é o
contrário do que ela imaginava. Ou seja, caso envie uma frase que deveria ser "POSITIVA" e
ela retorne que é "NEGATIVA". Ao informar para ela que ela estava errada, ela aprenderá e
entenderá que essa frase deveria ser "POSITIVA", sendo assim, com esse novo aprendizado,
nas proximas vezes que enviar uma frase parecida ela entenderá que é "POSITIVA".

* Exemplo de frase errada

![image](https://github.com/user-attachments/assets/20db2b18-ceec-40c3-be4d-c8f3c27c8fd0)

* Após dar meu feedback e enviando novamente a mesma frase

![image](https://github.com/user-attachments/assets/4604dcb5-3540-418e-b9d3-9be42daec269)
