**Planilha de Farm Semanal Automatizada**
Este projeto tem como objetivo automatizar o acompanhamento do farm semanal de membros em um jogo, utilizando o Google Planilhas, Google Apps Script, Python e GitHub Actions. O sistema gera, de forma automática, a distribuição de metas semanais entre os membros e envia atualizações via Discord.

**Funcionalidades**
**Distribuição de Produtos:**

A planilha gerencia a distribuição de produtos entre os membros.

O processo de distribuição prioriza 2 produtos e gera outros 3 de forma randômica, com possibilidade de repetição.

**Atualização Automática de Metas:**

A cada segunda-feira, às 00:00, as metas semanais são automaticamente alteradas via acionador configurado no Google Apps Script.

**Integração com Discord:**

Um webhook no Discord é utilizado para enviar atualizações da planilha.

Um script Python é responsável por acessar a planilha, gerar uma captura de tela e enviar a imagem no canal do Discord.

**Automação no GitHub Actions:**

O processo é agendado utilizando YAML no GitHub Actions, garantindo que a planilha seja atualizada e os prints enviados automaticamente.

O uso de secrets no GitHub Actions protege URLs sensíveis, como a URL da planilha e o webhook do Discord.

**Tecnologias Utilizadas**
**Google Planilhas e Google Apps Script:** Para automação e manipulação da planilha.

**Python:** Para automação da captura de tela da planilha e envio para o Discord.

**GitHub Actions:** Para orquestrar jobs e agendar a execução do script.

**Discord Webhook:** Para enviar as atualizações da planilha para o canal do Discord.

**YAML:** Para configurar os workflows no GitHub Actions.

**Como Funciona**
**1. Planilha no Google Planilhas**
A planilha é configurada para distribuir produtos entre os membros. Um script Google Apps Script é utilizado para gerar a distribuição randômica dos produtos, priorizando dois produtos e gerando outros três de forma aleatória. A cada semana, as metas são alteradas automaticamente através de um acionador configurado no Apps Script.

**2. Automação com Python**
O script Python acessa a planilha, tira uma captura de tela da mesma e envia a imagem para o Discord.

O script é agendado para rodar automaticamente, utilizando GitHub Actions.

**3. Integração com Discord**
O webhook no Discord é configurado para receber a captura de tela da planilha sempre que a automação Python for executada. Isso mantém todos os membros atualizados sobre as metas semanais.

**4. GitHub Actions**
YAML é usado para configurar os workflows no GitHub Actions.

Secrets são utilizados para proteger URLs e informações sensíveis, como a URL da planilha e o webhook do Discord.

**Como Configurar**
1. Criando a Planilha no Google Planilhas
Crie uma nova planilha no Google Planilhas.

Adicione as colunas necessárias para rastrear os membros e os produtos.

Use o Google Apps Script para implementar o código que distribui os produtos entre os membros.

**2. Configurando o Google Apps Script**
Abra a planilha e vá para Extensões > Apps Script.

Implemente o código necessário para a distribuição dos produtos.

Crie um acionador que dispare toda segunda-feira, às 00:00, para atualizar as metas.

**3. Criando o Webhook do Discord**
No Discord, crie um novo canal.

Vá para Configurações do Canal > Integrações > Webhooks e crie um novo webhook.

Copie o URL do webhook.

**4. Configurando o Script Python**
Instale as dependências necessárias:
> pip install selenium requests webdriver_manager

Altere o script Python para incluir a URL da sua planilha e o webhook do Discord.

**5. Configurando GitHub Actions**
Crie um arquivo .yml dentro da pasta .github/workflows/ no seu repositório.

Configure o job para rodar o script Python automaticamente.

Use secrets do GitHub para armazenar a URL da planilha e o webhook do Discord de forma segura.
