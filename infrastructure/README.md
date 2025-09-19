# 🏗️ Infrastructure as Code (IaC)

Este diretório contém a configuração Terraform para deploy do AWS Chatbot na AWS.

## 📋 Pré-requisitos

- Terraform >= 1.0
- AWS CLI configurado
- Credenciais AWS com permissões adequadas

## 🚀 Deploy

### 1. Configurar Variáveis
```bash
cp terraform.tfvars.example terraform.tfvars
# Edite terraform.tfvars com seus valores
```

### 2. Inicializar Terraform
```bash
cd infrastructure/
terraform init
```

### 3. Planejar Deploy
```bash
terraform plan
```

### 4. Aplicar Configuração
```bash
terraform apply
```

### 5. Obter URL da Aplicação
```bash
terraform output load_balancer_dns
```

## 🏗️ Arquitetura Implantada

- **VPC** com 2 subnets públicas
- **Application Load Balancer** (ALB)
- **ECS Fargate** cluster e service
- **CloudWatch** logs
- **IAM** roles com permissões mínimas

## 💰 Estimativa de Custos

### Recursos Criados:
- **ECS Fargate (1 task):** ~$8.50/mês
- **Application Load Balancer:** ~$16.20/mês
- **CloudWatch Logs:** ~$0.50/mês
- **NAT Gateway:** $0 (usando subnets públicas)

**Total estimado:** ~$25.20/mês

## 🧹 Limpeza

Para remover todos os recursos:
```bash
terraform destroy
```

## 📁 Arquivos

- `main.tf` - VPC, subnets, security groups
- `ecs.tf` - ECS cluster, service, task definition
- `alb.tf` - Application Load Balancer
- `iam.tf` - IAM roles e políticas
- `terraform.tfvars.example` - Exemplo de variáveis

## ⚠️ Importante

- Este é um exemplo para fins educacionais
- Revise as configurações antes do deploy
- Monitore os custos AWS após o deploy
- Use ambientes separados para dev/prod