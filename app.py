from flask import Flask, render_template, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def calculo_estatistico(dados, frequencia):
    # Expande os dados baseado na frequencia
    conjunto_dados = np.repeat(dados, frequencia)
    
    media = np.mean(conjunto_dados)
    mediana = np.median(conjunto_dados)
    moda = max(set(conjunto_dados), key=list(conjunto_dados).count)
    variancia = np.var(conjunto_dados)
    desvio_padrao = np.std(conjunto_dados)

    return {
        'media': media,
        'mediana': mediana,
        'moda': moda,
        'variancia': variancia,
        'desvio_padrao': desvio_padrao
    }

@app.route('/')
def indice():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    dados = list(map(float, request.form.getlist('dados[]')))
    frequencia = list(map(int, request.form.getlist('frequencia[]')))
    
    estatisticas = calculo_estatistico(dados, frequencia)
    
    # Gera o gráfico
    plt.figure()
    barras = plt.bar(dados, frequencia)
    plt.title('Gráfico de Variância')
    plt.xlabel('Dados')
    plt.ylabel('Frequência')
    
    # Calcula o total para porcentagens
    total = sum(frequencia)
    
    # Adiciona as porcentagens acima dos pilares
    for barra in barras:
        altura = barra.get_height()
        porcentagem = (altura / total) * 100
        plt.text(barra.get_x() + barra.get_width() / 2, altura, f'{porcentagem:.1f}%', 
                 ha='center', va='bottom')
    
    # Ajusta os ticks do eixo Y para que subam de 2 em 2
    max_frequencia = max(frequencia)
    plt.yticks(np.arange(0, max_frequencia + 2, 2))
    
    # Salva o gráfico para ser embutido no html
    img = io.BytesIO()
    plt.savefig(img, format='jpeg')
    img.seek(0)
    grafico_url = base64.b64encode(img.getvalue()).decode()

    return jsonify({'estatisticas': estatisticas, 'grafico_url': f'data:image/png;base64,{grafico_url}'})


if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)
