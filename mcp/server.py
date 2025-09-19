#!/usr/bin/env python3
"""
Servidor MCP (Model Context Protocol) para AWS Chatbot
Fornece contexto sobre recursos AWS para Amazon Q Developer
"""

import json
import asyncio
from typing import Dict, List, Any
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MCPServer:
    """Servidor MCP para fornecer contexto AWS"""
    
    def __init__(self):
        self.name = "aws-chatbot-mcp"
        self.version = "1.0.0"
        self.resources = {}
        self.tools = {}
        
    async def initialize(self):
        """Inicializar servidor MCP"""
        logger.info(f"Inicializando servidor MCP {self.name} v{self.version}")
        
        # Registrar recursos disponíveis
        self.resources = {
            "aws-costs": {
                "uri": "aws://costs",
                "name": "AWS Cost Information",
                "description": "Informações de custos da conta AWS"
            },
            "s3-buckets": {
                "uri": "aws://s3/buckets",
                "name": "S3 Buckets",
                "description": "Lista de buckets S3 e seus objetos"
            },
            "ec2-instances": {
                "uri": "aws://ec2/instances", 
                "name": "EC2 Instances",
                "description": "Informações sobre instâncias EC2"
            }
        }
        
        # Registrar ferramentas disponíveis
        self.tools = {
            "get_aws_context": {
                "name": "get_aws_context",
                "description": "Obter contexto sobre recursos AWS",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "resource_type": {
                            "type": "string",
                            "enum": ["costs", "s3", "ec2", "all"]
                        }
                    },
                    "required": ["resource_type"]
                }
            }
        }
        
        logger.info("Servidor MCP inicializado com sucesso")
    
    async def list_resources(self) -> List[Dict[str, Any]]:
        """Listar recursos disponíveis"""
        return list(self.resources.values())
    
    async def list_tools(self) -> List[Dict[str, Any]]:
        """Listar ferramentas disponíveis"""
        return list(self.tools.values())
    
    async def get_resource(self, uri: str) -> Dict[str, Any]:
        """Obter recurso específico"""
        for resource in self.resources.values():
            if resource["uri"] == uri:
                return {
                    "uri": uri,
                    "mimeType": "application/json",
                    "text": json.dumps({
                        "context": f"Contexto para {resource['name']}",
                        "description": resource["description"],
                        "last_updated": "2024-01-01T00:00:00Z"
                    })
                }
        
        raise ValueError(f"Recurso não encontrado: {uri}")
    
    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Executar ferramenta"""
        if name == "get_aws_context":
            resource_type = arguments.get("resource_type", "all")
            
            context = {
                "costs": "Contexto de custos AWS disponível",
                "s3": "Contexto de buckets S3 disponível", 
                "ec2": "Contexto de instâncias EC2 disponível",
                "all": "Contexto completo AWS disponível"
            }
            
            return {
                "content": [{
                    "type": "text",
                    "text": context.get(resource_type, "Contexto não encontrado")
                }]
            }
        
        raise ValueError(f"Ferramenta não encontrada: {name}")

# Configuração do servidor
async def main():
    """Função principal do servidor MCP"""
    server = MCPServer()
    await server.initialize()
    
    logger.info("Servidor MCP rodando...")
    logger.info("Para usar com Amazon Q Developer, configure o arquivo mcp_config.json")
    
    # Manter servidor rodando
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        logger.info("Servidor MCP finalizado")

if __name__ == "__main__":
    asyncio.run(main())