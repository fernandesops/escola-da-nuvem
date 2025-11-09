import re
import statistics

def analisar_logs(nome_arquivo: str):

    padrao_regex = r"Execution Time: (\d+\.\d+)s"
    
    tempos_execucao = []
    
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            for linha in f:

                match = re.search(padrao_regex, linha)
                if match:

                    tempo_str = match.group(1)
                    tempos_execucao.append(float(tempo_str))
        

        if tempos_execucao:
            media = statistics.mean(tempos_execucao)
            desvio_padrao = statistics.stdev(tempos_execucao)
            
            print(f"--- Análise do Log: {nome_arquivo} ---")
            print(f"Tempos coletados: {tempos_execucao}")
            print(f"Total de amostras: {len(tempos_execucao)}")
            print(f"Média do Tempo: {media:.2f}s")
            print(f"Desvio Padrão: {desvio_padrao:.2f}s")
        else:
            print("Nenhum tempo de execução encontrado no log.")
            
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# criar o log antes no arquivo 7.1criarlogml.py
analisar_logs("modelo.log")