# 📝 Prompts Utilizados com Amazon Q Developer

Este documento lista todos os prompts utilizados para criar este projeto com Amazon Q Developer.

## 🚀 Prompt 1: Criação do Projeto Completo

```
Quero que você crie um repositório completo e funcional em Python para um projeto de chatbot conectado aos serviços da AWS.
O repositório deve estar pronto para ser publicado no GitHub e conter toda a documentação necessária para que qualquer pessoa consiga clonar e executar o projeto de forma simples.

Objetivo do projeto:

O sistema será um chatbot web que permite ao usuário conversar e obter informações sobre sua conta da AWS.
O chatbot deve ser capaz de responder perguntas como:

Estimativa de custos da conta;
Quantos arquivos existem em determinado bucket S3;
Quais instâncias EC2 estão rodando;
Outras informações possíveis usando os serviços da AWS.

O projeto deve utilizar Flask para criar uma aplicação web onde o usuário poderá interagir com o chatbot por meio de uma interface visual (não apenas terminal).

A interface deve seguir um estilo inspirado no site da AWS:
Cores sóbrias (tons de azul, cinza e branco);
Layout responsivo;
Um campo de entrada de mensagem e uma área de exibição do chat.
```

## 🔧 Prompt 2: Melhoria AWS CLI e SSO

```
Muito bom! Acho que precisamos incluir uma orientação para a pessoa baixar o aws CLI e dar um aws sso login para poder conectar com a lib boto3, n
```

## 📝 Prompt 3: Documentação TDC 2025

```
Muito bom! Precisamos incluir também essas informações

Cada projeto deve trazer um README.md contendo:
Qual problema inspirou a ideia
Como a solução foi construída
Instruções para rodar
Próximos passos

Etapa 1: Bolsinha cabos exclusiva AWS
Um projeto gerado com Amazon Q Developer ou Amazon Q Developer CLI
Projeto público no Github (com a tag q-developer-quest-tdc-2025)
README.md (com screenshot do projeto rodando)
Lista dos prompts utilizados no README.md
Etapa 2: Mochilinha exclusiva AWS
Tudo da Etapa 1
Diagrama de arquitetura (drawio, mermaid, etc...)
Um ou mais testes automatizados (unidade, integração, E2E)
Etapa 3: Garrafa + Toalha exclusiva AWS
Tudo das Etapas 1 & 2
Utilizar ao menos 1 servidor MCP
Configuração do Amazon Q Developer no repositório
IaC (Terraform, AWS CDK, AWS CloudFormation, etc) para deployar na AWS
Etapa 4: Exclusiva camiseta da capivara AWS
Tudo das Etapas 1, 2 & 3
README.md atualizado com estimativa de custo da solução
```

## 🚀 Prompt 4: Implementação Etapas 2 e 3

```
Vamos implementar as próximas etapas como o diagrama de arquitetura e testes automatizados
```

```
Quero sim! Faça essa implementação de forma completa
```

## ✅ Prompt 5: Finalização e Etapa 4

```
Muito bom! Agora, vamos prosseguir com a etapa 4 de forma completa. Além disso, quero que você atualize o readme e o arquivo de prompts com os prompts que eu te passei. Faça também uma verificação completa em todo o repositório e em todos os arquivos que criamos para ver se há algo para ser corrigido.
```

## 🎯 Resultados Obtidos

| Prompt | Arquivos Gerados | Funcionalidade |
|--------|------------------|----------------|
| **Prompt 1** | 9 arquivos base | Projeto completo funcional |
| **Prompt 2** | README atualizado | Documentação AWS CLI/SSO |
| **Prompt 3** | README + PROMPTS.md | Estrutura TDC 2025 |
| **Prompt 4** | 8 arquivos | Arquitetura + Testes + MCP + IaC |
| **Prompt 5** | 3 arquivos | Análise de custos + Revisão |

**Total:** 23 arquivos criados em 5 interações

## 💡 Dicas para Usar Amazon Q Developer

- **Seja específico:** Detalhe exatamente o que você quer
- **Contextualize:** Explique o objetivo final do projeto
- **Itere:** Use prompts de refinamento para melhorar o resultado
- **Documente:** Mantenha registro dos prompts para referência futura
- **Valide:** Sempre revise e teste o código gerado