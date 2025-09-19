import unittest
import json
from unittest.mock import patch, MagicMock
import sys
import os

# Adicionar o diretório pai ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        """Configurar o cliente de teste"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_index_route(self):
        """Testar se a rota principal retorna 200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AWS Chatbot', response.data)
    
    @patch('app.aws_services')
    def test_chat_route_help_command(self, mock_aws_services):
        """Testar comando de ajuda"""
        response = self.app.post('/chat', 
                                json={'message': 'ajuda'},
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('Comandos disponíveis', data['response'])
    
    @patch('app.aws_services')
    def test_chat_route_costs_command(self, mock_aws_services):
        """Testar comando de custos"""
        mock_aws_services.get_cost_estimate.return_value = "💰 Custos: $10.50"
        
        response = self.app.post('/chat',
                                json={'message': 'custos'},
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['response'], "💰 Custos: $10.50")
        mock_aws_services.get_cost_estimate.assert_called_once()
    
    @patch('app.aws_services')
    def test_chat_route_s3_buckets_command(self, mock_aws_services):
        """Testar comando de listagem de buckets S3"""
        mock_aws_services.list_s3_buckets.return_value = "🗂️ Buckets: bucket1, bucket2"
        
        response = self.app.post('/chat',
                                json={'message': 's3 buckets'},
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['response'], "🗂️ Buckets: bucket1, bucket2")
        mock_aws_services.list_s3_buckets.assert_called_once()
    
    @patch('app.aws_services')
    def test_chat_route_ec2_instances_command(self, mock_aws_services):
        """Testar comando de listagem de instâncias EC2"""
        mock_aws_services.list_ec2_instances.return_value = "🖥️ Instâncias: i-123456"
        
        response = self.app.post('/chat',
                                json={'message': 'ec2 instancias'},
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['response'], "🖥️ Instâncias: i-123456")
        mock_aws_services.list_ec2_instances.assert_called_once()
    
    def test_chat_route_empty_message(self):
        """Testar mensagem vazia"""
        response = self.app.post('/chat',
                                json={'message': ''},
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['response'], 'Por favor, digite uma mensagem.')
    
    def test_chat_route_unknown_command(self):
        """Testar comando desconhecido"""
        response = self.app.post('/chat',
                                json={'message': 'comando inexistente'},
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('Comando não reconhecido', data['response'])

if __name__ == '__main__':
    unittest.main()