import unittest
import json
import sys
import os
from unittest.mock import patch

# Adicionar o diretório pai ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class TestIntegration(unittest.TestCase):
    """Testes de integração end-to-end"""
    
    def setUp(self):
        """Configurar o cliente de teste"""
        self.app = app.test_client()
        self.app.testing = True
    
    @patch('aws_services.boto3')
    def test_full_chat_workflow(self, mock_boto3):
        """Testar fluxo completo de chat"""
        # Mock dos clientes AWS
        mock_s3_client = mock_boto3.client.return_value
        mock_s3_client.list_buckets.return_value = {
            'Buckets': [{'Name': 'test-bucket', 'CreationDate': '2024-01-01'}]
        }
        
        # 1. Acessar página principal
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
        # 2. Testar comando de ajuda
        response = self.app.post('/chat',
                                json={'message': 'ajuda'},
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('Comandos disponíveis', data['response'])
        
        # 3. Testar comando S3 (com mock)
        response = self.app.post('/chat',
                                json={'message': 's3 buckets'},
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_error_handling(self):
        """Testar tratamento de erros"""
        # Testar JSON inválido
        response = self.app.post('/chat',
                                data='invalid json',
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
        # Testar método não permitido
        response = self.app.get('/chat')
        self.assertEqual(response.status_code, 405)
    
    def test_static_files(self):
        """Testar se arquivos estáticos são servidos"""
        # Testar CSS
        response = self.app.get('/static/style.css')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'body', response.data)
        
        # Testar JavaScript
        response = self.app.get('/static/script.js')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'function', response.data)

if __name__ == '__main__':
    unittest.main()