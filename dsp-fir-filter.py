import numpy as np
import matplotlib.pyplot as plt

# Aplicando um estilo de template ao gráfico
plt.style.use('seaborn-darkgrid')

def fir_filter(signal, coefficients):
    """
    Aplica um filtro FIR a um sinal de entrada.

    Parâmetros:
    signal (array_like): O sinal de entrada.
    coefficients (array_like): Os coeficientes do filtro FIR.

    Retorna:
    array_like: O sinal filtrado.
    """
    # Aplica a convolução entre o sinal de entrada e os coeficientes do filtro
    filtered_signal = np.convolve(signal, coefficients, mode='same')
    return filtered_signal

# Exemplo de uso
if __name__ == "__main__":
    # Sinal de entrada (gerado aleatoriamente para exemplo)
    signal = np.random.randn(100)

    # Coeficientes do filtro FIR (filtro passa-baixa simples)
    cutoff_freq = 0.1  # Frequência de corte do filtro (em fração da frequência de Nyquist)
    num_taps = 11  # Número de coeficientes do filtro
    # Calcula os coeficientes do filtro FIR usando a função sinc
    coefficients = np.sinc(2 * cutoff_freq * (np.arange(num_taps) - (num_taps - 1) / 2))
    
    # Normaliza os coeficientes para garantir que a resposta em frequência seja unitária na frequência de corte
    coefficients /= np.sum(coefficients)

    # Aplica o filtro FIR ao sinal de entrada
    filtered_signal = fir_filter(signal, coefficients)

    # Plotagem do sinal de entrada em roxo e do sinal filtrado em laranja
    plt.figure(figsize=(10, 6))
    plt.plot(signal, color='orange', label='Sinal de Entrada')
    plt.plot(filtered_signal, color='purple', label='Sinal Filtrado')
    plt.title('Comparação entre Sinal de Entrada e Sinal Filtrado')
    plt.xlabel('Amostras')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()
