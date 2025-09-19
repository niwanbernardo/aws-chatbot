#!/usr/bin/env python3
"""
Calculadora de custos detalhada para o AWS Chatbot
Estima custos de desenvolvimento, produção e diferentes cenários de uso
"""

from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass
class CostItem:
    """Item de custo individual"""
    service: str
    description: str
    monthly_cost: float
    unit: str = "USD"
    notes: str = ""

class AWSCostCalculator:
    """Calculadora de custos AWS para o projeto"""
    
    def __init__(self, region: str = "us-east-1"):
        self.region = region
        self.currency = "USD"
    
    def get_development_costs(self) -> List[CostItem]:
        """Custos de desenvolvimento (Free Tier)"""
        return [
            CostItem("AWS Free Tier", "Desenvolvimento e testes", 0.00, notes="12 meses gratuitos"),
            CostItem("ECS Fargate", "750 horas/mês gratuitas", 0.00, notes="Suficiente para desenvolvimento"),
            CostItem("Application Load Balancer", "750 horas/mês gratuitas", 0.00, notes="Primeiro ano"),
            CostItem("CloudWatch Logs", "5GB gratuitos/mês", 0.00, notes="Logs básicos"),
            CostItem("S3", "5GB armazenamento gratuito", 0.00, notes="Para assets estáticos"),
            CostItem("EC2", "750 horas t2.micro/mês", 0.00, notes="Para testes se necessário")
        ]
    
    def get_production_costs_basic(self) -> List[CostItem]:
        """Custos de produção - configuração básica"""
        return [
            CostItem("ECS Fargate", "1 task, 0.25 vCPU, 0.5GB RAM", 8.50, notes="24/7 uptime"),
            CostItem("Application Load Balancer", "Básico com health checks", 16.20, notes="Inclui 1 LCU/hora"),
            CostItem("CloudWatch Logs", "Logs da aplicação", 0.50, notes="~1GB/mês"),
            CostItem("Route 53", "Hosted zone + queries", 0.50, notes="DNS personalizado"),
            CostItem("Data Transfer", "Tráfego de saída", 1.00, notes="~10GB/mês"),
            CostItem("S3", "Assets estáticos", 0.30, notes="1GB armazenamento + requests")
        ]
    
    def get_production_costs_scaled(self) -> List[CostItem]:
        """Custos de produção - configuração escalada"""
        return [
            CostItem("ECS Fargate", "2 tasks, 0.5 vCPU, 1GB RAM cada", 34.00, notes="Alta disponibilidade"),
            CostItem("Application Load Balancer", "Com SSL e múltiplas regras", 18.50, notes="2-3 LCU/hora"),
            CostItem("CloudWatch Logs", "Logs detalhados + métricas", 2.00, notes="~4GB/mês"),
            CostItem("Route 53", "Hosted zone + health checks", 1.50, notes="DNS + monitoramento"),
            CostItem("Data Transfer", "Tráfego moderado", 5.00, notes="~50GB/mês"),
            CostItem("S3", "Assets + backups", 1.00, notes="5GB + versionamento"),
            CostItem("RDS", "db.t3.micro PostgreSQL", 12.50, notes="Para dados persistentes"),
            CostItem("ElastiCache", "cache.t3.micro Redis", 11.50, notes="Cache de sessões")
        ]
    
    def get_enterprise_costs(self) -> List[CostItem]:
        """Custos enterprise - configuração completa"""
        return [
            CostItem("ECS Fargate", "4 tasks, 1 vCPU, 2GB RAM cada", 136.00, notes="Multi-AZ, auto-scaling"),
            CostItem("Application Load Balancer", "Multi-AZ com WAF", 25.00, notes="5+ LCU/hora + WAF"),
            CostItem("CloudWatch", "Logs + métricas + dashboards", 8.00, notes="Monitoramento completo"),
            CostItem("Route 53", "DNS + health checks + failover", 3.00, notes="DNS avançado"),
            CostItem("Data Transfer", "Tráfego alto", 20.00, notes="~200GB/mês"),
            CostItem("S3", "Multi-class storage", 5.00, notes="IA + Glacier para backups"),
            CostItem("RDS", "db.t3.small Multi-AZ", 35.00, notes="Alta disponibilidade"),
            CostItem("ElastiCache", "cache.t3.small cluster", 25.00, notes="Redis cluster"),
            CostItem("CloudFront", "CDN global", 10.00, notes="Distribuição de conteúdo"),
            CostItem("AWS WAF", "Proteção web", 5.00, notes="Segurança adicional"),
            CostItem("Systems Manager", "Gerenciamento de parâmetros", 2.00, notes="Configurações seguras")
        ]
    
    def calculate_total(self, cost_items: List[CostItem]) -> float:
        """Calcula o total de uma lista de itens de custo"""
        return sum(item.monthly_cost for item in cost_items)
    
    def generate_cost_report(self) -> Dict[str, Any]:
        """Gera relatório completo de custos"""
        dev_costs = self.get_development_costs()
        prod_basic_costs = self.get_production_costs_basic()
        prod_scaled_costs = self.get_production_costs_scaled()
        enterprise_costs = self.get_enterprise_costs()
        
        return {
            "generated_at": datetime.now().isoformat(),
            "currency": self.currency,
            "region": self.region,
            "scenarios": {
                "development": {
                    "description": "Desenvolvimento e testes (Free Tier)",
                    "monthly_total": self.calculate_total(dev_costs),
                    "annual_total": self.calculate_total(dev_costs) * 12,
                    "items": [
                        {
                            "service": item.service,
                            "description": item.description,
                            "monthly_cost": item.monthly_cost,
                            "notes": item.notes
                        } for item in dev_costs
                    ]
                },
                "production_basic": {
                    "description": "Produção básica (baixo tráfego)",
                    "monthly_total": self.calculate_total(prod_basic_costs),
                    "annual_total": self.calculate_total(prod_basic_costs) * 12,
                    "items": [
                        {
                            "service": item.service,
                            "description": item.description,
                            "monthly_cost": item.monthly_cost,
                            "notes": item.notes
                        } for item in prod_basic_costs
                    ]
                },
                "production_scaled": {
                    "description": "Produção escalada (tráfego moderado)",
                    "monthly_total": self.calculate_total(prod_scaled_costs),
                    "annual_total": self.calculate_total(prod_scaled_costs) * 12,
                    "items": [
                        {
                            "service": item.service,
                            "description": item.description,
                            "monthly_cost": item.monthly_cost,
                            "notes": item.notes
                        } for item in prod_scaled_costs
                    ]
                },
                "enterprise": {
                    "description": "Enterprise (alto tráfego e disponibilidade)",
                    "monthly_total": self.calculate_total(enterprise_costs),
                    "annual_total": self.calculate_total(enterprise_costs) * 12,
                    "items": [
                        {
                            "service": item.service,
                            "description": item.description,
                            "monthly_cost": item.monthly_cost,
                            "notes": item.notes
                        } for item in enterprise_costs
                    ]
                }
            },
            "recommendations": [
                "Comece com o cenário de desenvolvimento usando Free Tier",
                "Para produção inicial, use a configuração básica",
                "Monitore custos com AWS Cost Explorer e CloudWatch",
                "Configure alertas de billing para evitar surpresas",
                "Use Reserved Instances para economizar em cargas estáveis",
                "Considere Spot Instances para workloads não-críticos"
            ]
        }

if __name__ == "__main__":
    calculator = AWSCostCalculator()
    report = calculator.generate_cost_report()
    
    print("=== RELATÓRIO DE CUSTOS AWS CHATBOT ===\n")
    
    for scenario_name, scenario_data in report["scenarios"].items():
        print(f"📊 {scenario_data['description'].upper()}")
        print(f"💰 Custo mensal: ${scenario_data['monthly_total']:.2f}")
        print(f"💰 Custo anual: ${scenario_data['annual_total']:.2f}")
        print()
        
        for item in scenario_data['items']:
            if item['monthly_cost'] > 0:
                print(f"  • {item['service']}: ${item['monthly_cost']:.2f}/mês - {item['description']}")
        print("\n" + "="*50 + "\n")