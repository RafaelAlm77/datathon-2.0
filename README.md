# MVP de IA para Recrutamento - Datathon Pós-Tech

Este projeto foi desenvolvido como solução para o Datathon da Pós-Tech (Fase 5), com o objetivo de criar uma aplicação de Inteligência Artificial para otimizar o processo de recrutamento e seleção, prevendo a probabilidade de "match" entre um candidato e uma vaga.

A aplicação web, desenvolvida com Streamlit, permite que um recrutador insira os dados de uma vaga e o currículo de um candidato para receber uma análise preditiva instantânea, auxiliando na tomada de decisão.

**➡️ Link para a aplicação ativa:** [https://rafaelalm77-datathon-2-0-app-84veeg.streamlit.app/](https://rafaelalm77-datathon-2-0-app-84veeg.streamlit.app/)

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

## 🚀 Como Executar o Projeto Localmente

Para clonar e executar esta aplicação na sua própria máquina, siga os passos abaixo.

**Pré-requisitos:**
* [Git](https://git-scm.com/downloads) instalado.
* [Git LFS](https://git-lfs.github.com/) instalado.

**Passos:**

1.  **Clone o Repositório**
    Abra o terminal e clone este repositório para a sua máquina.
    ```bash
    git clone [https://github.com/RafaelAlm77/datathon-2.0.git](https://github.com/RafaelAlm77/datathon-2.0.git)
    cd Datathon-2.0
    ```

2.  **Crie e Ative o Ambiente Virtual**
    É uma boa prática criar um ambiente isolado para o projeto.
    ```bash
    # Criar o ambiente (pode usar 'python3' dependendo da sua instalação)
    python -m venv .venv

    # Ativar o ambiente no Windows (CMD)
    .\.venv\Scripts\activate
    ```

3.  **Instale as Dependências**
    O arquivo `requirements.txt` contém todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Baixe os Arquivos Grandes do LFS**
    Este projeto usa Git LFS para gerenciar o modelo treinado e os arquivos de dados. Execute o comando abaixo para baixá-los do armazenamento do LFS para sua máquina.
    ```bash
    git lfs pull
    ```

5.  **Rode a Aplicação Streamlit**
    Com tudo instalado e o ambiente ativado, execute o comando para iniciar a aplicação.
    ```bash
    streamlit run app.py
    ```
    Uma nova aba abrirá no seu navegador com a aplicação funcionando!



## 📁 Estrutura do Projeto

├── .gitattributes           # Configuração do Git LFS
├── .gitignore               # Arquivos a serem ignorados pelo Git
├── app.py                   # Script principal da aplicação web com Streamlit
├── recruitment_model.joblib   # Modelo treinado (gerenciado pelo LFS)
├── requirements.txt         # Lista de dependências Python
└── README.md                # Este arquivo de instruções


## ✒️ Autores

* **Vitor Bazzo**
* **Marcelo Gonçalves Adade**
* **Rafael Gustavo Basso Izidio de Almeida**
* **Athos Matheus Pugliese da Silva**
* **Murilo Santos**