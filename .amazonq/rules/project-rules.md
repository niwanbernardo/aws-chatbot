# Regras do Projeto AWS Chatbot para Amazon Q Developer

## 🎯 Contexto do Projeto
Este é um chatbot web para consultar informações da conta AWS usando Flask e boto3.

## 📋 Regras de Desenvolvimento

### Estrutura de Código
- Use Python 3.8+ com type hints quando possível
- Siga PEP 8 para formatação de código
- Mantenha funções pequenas e focadas (máximo 20 linhas)
- Use docstrings para todas as funções públicas

### Padrões AWS
- Sempre use boto3 para integração com serviços AWS
- Implemente tratamento de erros para ClientError e NoCredentialsError
- Use AWS SSO quando possível para autenticação
- Mantenha credenciais em variáveis de ambiente ou AWS CLI

### Padrões Flask
- Use blueprints para organizar rotas quando o projeto crescer
- Implemente validação de entrada para todas as rotas POST
- Retorne sempre JSON nas APIs com status codes apropriados
- Use templates Jinja2 para renderização HTML

### Segurança
- Nunca commite credenciais AWS no código
- Valide todas as entradas do usuário
- Use HTTPS em produção
- Implemente rate limiting para APIs

### Testes
- Mantenha cobertura de testes acima de 80%
- Use mocks para serviços AWS em testes
- Teste cenários de erro além dos casos de sucesso
- Execute testes antes de cada commit

### Interface
- Mantenha design responsivo para mobile e desktop
- Use cores da paleta AWS (azul #232f3e, laranja #ff9900)
- Implemente loading states para operações assíncronas
- Forneça feedback claro para ações do usuário

## 🚀 Comandos Úteis

```bash
# Executar testes
python run_tests.py

# Executar aplicação
python app.py

# Login AWS SSO
aws sso login
```

## 📝 Convenções de Commit
- feat: nova funcionalidade
- fix: correção de bug
- docs: documentação
- test: testes
- refactor: refatoração de código