# Estatísticas e Gráficos - Projeto IFPI

Este projeto foi desenvolvido como parte de um trabalho para o curso de **Análise e Desenvolvimento de Sistemas** do **Instituto Federal do Piauí, Campus Pedro II**. O objetivo é calcular estatísticas descritivas e gerar gráficos baseados em dados inseridos pelo usuário.

## Tecnologias Utilizadas

- **Python** (Flask, Numpy, Matplotlib)
- **HTML, CSS, JavaScript**

## Funcionalidades

Este projeto permite que o usuário insira uma série de dados e suas respectivas frequências, a partir dos quais o sistema calcula as seguintes estatísticas:

- **Média**
- **Mediana**
- **Moda**
- **Variância**
- **Desvio Padrão**

Além disso, o sistema gera um gráfico de variância para visualizar a distribuição dos dados.

## Como Usar

### Pré-requisitos

1. **Instalar as dependências**:

   Certifique-se de ter o Python e as bibliotecas necessárias instaladas.

    ```bash
   pip install flask numpy matplotlib

3. **Executar o servidor Flask**:

   Para iniciar o servidor, basta rodar o arquivo `app.py`. Após a execução, o terminal irá fornecer um endereço local (geralmente algo como `http://127.0.0.1:5000/`). Clique nesse endereço com `Ctrl + Click` ou copie e cole no seu navegador para acessar a aplicação.

4. **Inserir os Dados**:

   - Acesse a página principal no navegador.
   - No formulário, insira os valores dos dados e suas respectivas frequências.
   - Para adicionar mais entradas, clique no botão **Adicionar mais**.
   - Clique em **Calcular** para obter os resultados.

### Resultados

Após o cálculo, a página exibirá os seguintes resultados:

- Média
- Mediana
- Moda
- Variância
- Desvio Padrão

Além disso, será gerado um gráfico de variância que será exibido abaixo dos resultados.

## Estrutura do Código

### `app.py`

Este é o arquivo principal que contém a lógica do servidor, utilizando o Flask. Ele recebe os dados enviados pelo formulário, calcula as estatísticas e gera o gráfico de variância.

### `index.html`

O arquivo HTML contém a estrutura da página, com um formulário para inserção de dados e a exibição dos resultados. Além disso, ele inclui o código JavaScript necessário para fazer a requisição ao servidor Flask e mostrar os resultados dinamicamente.

## Contribuição

Este projeto foi desenvolvido com o objetivo acadêmico e está aberto a contribuições. Se você quiser melhorar o código ou adicionar novas funcionalidades, sinta-se à vontade para abrir um **pull request**.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.
