# 🏗️ Diagrama de Arquitetura

## Arquitetura da Solução

```mermaid
graph TB
    subgraph "Cliente"
        U[👤 Usuário]
        B[🌐 Navegador Web]
    end
    
    subgraph "Aplicação Flask"
        F[⚡ Flask App]
        AS[🔧 AWS Services Module]
        ST[📁 Static Files]
        TP[📄 Templates]
    end
    
    subgraph "AWS Services"
        S3[🗂️ Amazon S3]
        EC2[🖥️ Amazon EC2]
        CE[💰 Cost Explorer]
        IAM[🔐 AWS IAM]
    end
    
    subgraph "Autenticação"
        CLI[⚙️ AWS CLI]
        SSO[🔑 AWS SSO]
        CRED[📋 Credenciais]
    end
    
    U --> B
    B --> F
    F --> AS
    F --> ST
    F --> TP
    
    AS --> S3
    AS --> EC2
    AS --> CE
    
    AS --> CLI
    CLI --> SSO
    CLI --> CRED
    CLI --> IAM
    
    style F fill:#ff9900,stroke:#232f3e,stroke-width:3px,color:#fff
    style AS fill:#ffb84d,stroke:#232f3e,stroke-width:2px
    style S3 fill:#569a31,stroke:#232f3e,stroke-width:2px,color:#fff
    style EC2 fill:#f58536,stroke:#232f3e,stroke-width:2px,color:#fff
    style CE fill:#7aa116,stroke:#232f3e,stroke-width:2px,color:#fff
```

## Fluxo de Dados

```mermaid
sequenceDiagram
    participant U as 👤 Usuário
    participant B as 🌐 Browser
    participant F as ⚡ Flask
    participant AS as 🔧 AWS Services
    participant AWS as ☁️ AWS APIs
    
    U->>B: Digite comando
    B->>F: POST /chat
    F->>AS: Processa comando
    AS->>AWS: Chama API AWS
    AWS-->>AS: Retorna dados
    AS-->>F: Formata resposta
    F-->>B: JSON response
    B-->>U: Exibe resultado
```

## Componentes Principais

### 🖥️ Frontend
- **HTML/CSS/JS**: Interface responsiva inspirada na AWS
- **WebSocket**: Comunicação em tempo real (futuro)
- **Responsive Design**: Compatível com mobile e desktop

### ⚡ Backend (Flask)
- **app.py**: Servidor principal e rotas
- **aws_services.py**: Integração com APIs AWS
- **Middleware**: Tratamento de erros e logging

### ☁️ AWS Services
- **S3**: Listagem de buckets e objetos
- **EC2**: Status de instâncias
- **Cost Explorer**: Análise de custos
- **IAM**: Autenticação e autorização

### 🔐 Segurança
- **AWS SSO**: Autenticação moderna
- **IAM Roles**: Permissões granulares
- **Environment Variables**: Configurações sensíveis

## Padrões de Design

- **MVC Pattern**: Separação de responsabilidades
- **Service Layer**: Abstração das APIs AWS
- **Error Handling**: Tratamento robusto de exceções
- **Configuration Management**: Variáveis de ambiente