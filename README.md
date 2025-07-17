# MVP de IA para Recrutamento - Datathon Pós-Tech

Este projeto foi desenvolvido como solução para o Datathon da Pós-Tech (Fase 5) FIAP - turma 7DTAT, com o objetivo de criar uma aplicação de Inteligência Artificial para otimizar o processo de recrutamento e seleção, prevendo a probabilidade de "match" entre um candidato e uma vaga.

A aplicação web, desenvolvida com Streamlit, permite que um recrutador insira os dados de uma vaga e o currículo de um candidato para receber uma análise preditiva instantânea, auxiliando na tomada de decisão.

**➡️ Link para a aplicação ativa:** [https://rafaelalm77-datathon-2-0-app-84veeg.streamlit.app/](https://rafaelalm77-datathon-2-0-app-84veeg.streamlit.app/)

"A Decision é uma empresa especializada em serviços de bodyshop e recrutamento no setor de TI, com foco em conectar talentos qualificados às necessidades específicas dos clientes. O principal desafio é encontrar o candidato ideal para cada vaga em tempo hábil, garantindo tanto o fit técnico quanto o cultural."

---
## 🎯 Problema de Negócio

A Decision enfrenta alguns desafios críticos em seu processo de recrutamento:

* Falta de padronização em entrevistas, gerando perda de informações valiosas
* Dificuldade em identificar o real engajamento dos candidatos
* Tempo excessivo para encontrar o match ideal entre candidato e vaga
* Necessidade de acelerar o processo sem comprometer a qualidade da seleção

---
## ✨ Funcionalidades Principais

* **Análise Preditiva:** Utiliza um modelo `RandomForestClassifier` treinado para prever a probabilidade de um candidato ser "Encaminhado ao Requisitante", o nosso principal indicador de sucesso.
* **Interface Interativa:** Permite a inserção de dados da vaga (nível, remuneração) e do candidato (formação, currículo completo) através de uma interface web simples e intuitiva.
* **Score de Compatibilidade:** Fornece um score percentual e uma recomendação clara (Match Alto, Médio ou Baixo) para auxiliar na priorização de candidatos.
* **Portabilidade e Reprodutibilidade:** O projeto utiliza um ambiente virtual (`venv`), um arquivo de dependências (`requirements.txt`) e Git LFS para gerenciar arquivos grandes, garantindo que possa ser executado em qualquer máquina.

---
## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Análise de Dados:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **Aplicação Web:** Streamlit
* **Controle de Versão:** Git & GitHub
* **Gerenciamento de Arquivos Grandes:** Git LFS

---
## 📊 Dados

Os dados utilizados neste projeto estão disponíveis nos anexos da entrega e incluem:

* Histórico de candidatos e vagas
* Dados de remuneração e níveis profissionais
* Informações acadêmicas dos candidatos
* Currículos e perfis profissionais
* Resultados de processos seletivos anteriores
* Dados dos recrutadores responsáveis

---

## 🚀 Como Executar o Projeto localmente

Para clonar e executar esta aplicação na sua própria máquina, siga os passos abaixo.

**Pré-requisitos:**
* [Git](https://git-scm.com/downloads) instalado.
* [Git LFS](https://git-lfs.github.com/) instalado.

**Passos:**

1.  **Clone o Repositório**
    ```bash
    git clone [https://github.com/RafaelAlm77/datathon-2.0.git](https://github.com/RafaelAlm77/datathon-2.0.git)
    cd Datathon-5
    ```

2.  **Crie e Ative o Ambiente Virtual**
    ```bash
    # Criar o ambiente
    python -m venv .venv

    # Ativar no Windows (CMD)
    .\.venv\Scripts\activate
    ```

3.  **Instale as Dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Baixe os Arquivos Grandes do LFS**
    ```bash
    git lfs pull
    ```

5.  **Rode a Aplicação Streamlit**
    ```bash
    streamlit run app.py
    ```



## 📁 Estrutura do Projeto
```
├── .gitattributes           # Configuração do Git LFS
├── .gitignore               # Arquivos a serem ignorados pelo Git
├── app.py                   # Script principal da aplicação web com Streamlit
├── recruitment_model.joblib   # Modelo treinado (gerenciado pelo LFS)
├── requirements.txt         # Lista de dependências Python
└── README.md                # Este arquivo de instruções
```




## ✒️ Autores
FIAP POSTECH 7DTAT
* **Vitor Bazzo**
* **Marcelo Gonçalves Adade**
* **Rafael Gustavo Basso Izidio de Almeida**
* **Athos Matheus Pugliese da Silva**
* **Murilo Santos**
