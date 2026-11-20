# Projeto_Python_Unisave_2026
Sistema de votacao de chefe da turma foi desenvolvido em Python que permite gerir eleicoes para a escolha do chefe da turma de forma simples, organizada e transparente. O sistema permite adicionar, visualizar e eliminar os candidatos, registar votos, impedir que um eleitor vote mais que uma vez e apresentar os resultados finais.

# Sistema de Gestão de Eleições – Chefe da Turma

Sistema de gestão de eleições desenvolvido em Python, com interface de linha de comandos (terminal). Permite registar candidatos, visualizar candidaturas, realizar votações, acompanhar os resultados em tempo real e identificar automaticamente o vencedor ou situações de empate. O sistema também permite impedir que um eleitor vote mais de uma vez e guardar os dados dos candidatos num ficheiro JSON.

## Funcionalidades

- Registo de novos candidatos.
- Verificação de candidatos duplicados.
- Visualização da lista de candidatos registados.
- Registo de votos através da identificação do eleitor.
- Restrição de um voto por eleitor.
- Cálculo automático do total de votos.
- Apresentação dos resultados da votação.
- Identificação automática do candidato vencedor.
- Deteção e apresentação de situações de empate.
- Remoção de candidatos registados.
- Armazenamento dos dados dos candidatos em ficheiro JSON.

## Stack Técnica

| Componente | Tecnologia |
|---|---|
| Linguagem | Python 3.8+ |
| Interface | Linha de comandos (CLI) |
| Armazenamento | JSON (local) |
| Biblioteca | JSON (biblioteca padrão) |
| Dependências | Nenhuma externa |

## Arquitetura

Aplicação desenvolvida num único ficheiro Python, sem necessidade de dependências externas. A organização interna segue três componentes lógicos:

- **Gestão de candidatos** – permite adicionar, visualizar e eliminar candidatos, incluindo a verificação de duplicados.
- **Lógica de votação** – controla o registo dos eleitores, impede votos repetidos, contabiliza os votos e determina o vencedor ou empate.
- **Persistência de dados** – utiliza a biblioteca JSON para guardar os dados dos candidatos num ficheiro local chamado `dados.json` ao terminar a execução.

## Requisitos

- Python 3.8 ou superior.
- Terminal ou CMD para executar o programa.
- Biblioteca JSON (incluída na instalação padrão do Python).

## Instalação e Execução

1. Instalar o Python 3.8 ou superior.
2. Guardar o ficheiro `Trabalho1.py` numa pasta.
3. Abrir o terminal na localização do ficheiro.
4. Executar o seguinte comando:

```bash

```

Após a execução, será apresentado um menu interativo com as opções de gestão de candidatos, votação, consulta de resultados e encerramento do sistema.
