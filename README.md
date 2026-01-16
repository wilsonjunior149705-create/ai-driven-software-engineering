# ai-driven-software-engineering
# IA na prática: Acelerando o desenvolvimento e garantindo a qualidade com um fluxo de trabalho automatizado por IA

![CI](https://github.com/wilsonjunior149705-create/ai-driven-software-engineering/actions/workflows/ci.yml/badge.svg)

## 1. Contexto e problema (empresa fictícia)
Você faz parte de uma equipe que desenvolve uma ferramenta de colaboração online. A empresa cresce rápido e a pressão por novas features aumentou. O time vive um dilema clássico:

- Se entrega rápido, reduz testes e a qualidade cai (mais bugs em produção).
- Se investe em testes e revisões detalhadas, perde o prazo do roadmap.

### Gargalos identificados
1) **Desenvolvimento lento**: muita repetição ao criar endpoints, funções e estruturas básicas.  
2) **Baixa cobertura de testes**: testes são vistos como “atraso”.  
3) **Feedback lento**: bugs aparecem só no QA manual ou em produção.  
4) **Inconsistência de código**: cada dev resolve do seu jeito, elevando complexidade.

Esses problemas foram descritos no enunciado do trabalho (último trimestre, crescimento e promessa de features) e são típicos de times júnior/pleno com pressão de entrega.

## 2. Papel da IA no ciclo de desenvolvimento (Copilot + CI/CD)

### 2.1 GitHub Copilot (aceleração com qualidade)
O GitHub Copilot atua como “pair programmer”, reduzindo tempo em tarefas repetitivas e ajudando a:
- gerar funções, validações e estruturas de código;
- sugerir padrões e refatorações;
- criar testes automatizados quando o prompt é bem definido.

Estudos publicados pelo próprio GitHub indicam aumento de velocidade em tarefas de programação e melhor experiência do desenvolvedor: em um experimento controlado, participantes com Copilot concluíram tarefas **~55% mais rápido**. :contentReference[oaicite:1]{index=1}

Além da velocidade, há pesquisas sobre qualidade e orientação de boas práticas (ex.: geração de testes e verificação), com recomendação explícita de prompts detalhados e validação humana. :contentReference[oaicite:2]{index=2}

### 2.2 GitHub Actions (automação e feedback rápido)
O GitHub Actions automatiza o pipeline de CI para:
- instalar dependências;
- rodar testes a cada push/pull request;
- reduzir o tempo de feedback (pegar bug cedo = correção mais barata).

A documentação oficial do GitHub mostra como configurar workflows de build e testes para Python. :contentReference[oaicite:3]{index=3}

### 2.3 Qualidade não é só “número de cobertura”
Cobertura de testes é uma ferramenta para localizar partes não testadas, mas **não é sinônimo de qualidade**. Um conjunto pequeno de testes bem escolhidos pode prevenir regressões críticas melhor do que “cobertura alta” com testes fracos. Essa visão é defendida por Martin Fowler no artigo “Test Coverage”. 

## 3. Caso real (uso no mundo real)
Um exemplo real é a adoção do GitHub Copilot em escala corporativa pela **Accenture**, estudada em parceria com o GitHub: o conteúdo reporta melhorias em experiência do desenvolvedor e uso significativo do código sugerido (telemetria e pesquisa), reforçando que o valor vem de integrar a IA ao fluxo de trabalho e não apenas “gerar código”. 

## 4. Protótipo (Parte prática do trabalho)

Este repositório contém:
- Uma **API simples em FastAPI** para simular parte do produto (collab tool) com uma regra de negócio: **cálculo de total de pedidos com desconto e regras de frete**.
- Uma função principal de negócio em `app/pricing.py` + **testes com pytest** em `tests/test_pricing.py`.
- Um pipeline de **GitHub Actions** (`.github/workflows/ci.yml`) que instala dependências e roda testes automaticamente.

### 4.1 Como rodar localmente
```bash
pip install -r requirements.txt
pytest -q
uvicorn app.api:app --reload
