import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from botocore.exceptions import ClientError, NoCredentialsError

# Adicionar o diretório pai ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aws_services import AWSServices

class TestAWSServices(unittest.TestCase):
    
    @patch('aws_services.boto3')
    def setUp(self, mock_boto3):
        """Configurar mocks para os clientes AWS"""
        self.mock_s3_client = MagicMock()
        self.mock_ec2_client = MagicMock()
        self.mock_ce_client = MagicMock()
        
        mock_boto3.client.side_effect = lambda service: {
            's3': self.mock_s3_client,
            'ec2': self.mock_ec2_client,
            'ce': self.mock_ce_client
        }[service]
        
        self.aws_services = AWSServices()
    
    def test_get_cost_estimate_success(self):
        """Testar estimativa de custos com sucesso"""
        self.mock_ce_client.get_cost_and_usage.return_value = {
            'ResultsByTime': [{
                'Total': {
                    'BlendedCost': {
                        'Amount': '25.50',
                        'Unit': 'USD'
                    }
                }
            }]
        }
        
        result = self.aws_services.get_cost_estimate()
        self.assertIn('$25.50', result)
        self.assertIn('💰', result)
    
    def test_get_cost_estimate_no_data(self):
        """Testar estimativa de custos sem dados"""
        self.mock_ce_client.get_cost_and_usage.return_value = {
            'ResultsByTime': []
        }
        
        result = self.aws_services.get_cost_estimate()
        self.assertIn('Não foi possível obter', result)
    
    def test_get_cost_estimate_client_error(self):
        """Testar erro do cliente na estimativa de custos"""
        self.mock_ce_client.get_cost_and_usage.side_effect = ClientError(
            {'Error': {'Message': 'Access denied'}}, 'GetCostAndUsage'
        )
        
        result = self.aws_services.get_cost_estimate()
        self.assertIn('❌ Erro ao obter custos', result)
        self.assertIn('Access denied', result)
    
    def test_list_s3_buckets_success(self):
        """Testar listagem de buckets S3 com sucesso"""
        self.mock_s3_client.list_buckets.return_value = {
            'Buckets': [
                {'Name': 'bucket1', 'CreationDate': MagicMock()},
                {'Name': 'bucket2', 'CreationDate': MagicMock()}
            ]
        }
        
        # Mock do strftime
        for bucket in self.mock_s3_client.list_buckets.return_value['Buckets']:
            bucket['CreationDate'].strftime.return_value = '01/01/2024'
        
        result = self.aws_services.list_s3_buckets()
        self.assertIn('bucket1', result)
        self.assertIn('bucket2', result)
        self.assertIn('🗂️', result)
    
    def test_list_s3_buckets_empty(self):
        """Testar listagem de buckets S3 vazia"""
        self.mock_s3_client.list_buckets.return_value = {'Buckets': []}
        
        result = self.aws_services.list_s3_buckets()
        self.assertIn('Nenhum bucket S3 encontrado', result)
    
    def test_count_s3_objects_success(self):
        """Testar contagem de objetos S3 com sucesso"""
        self.mock_s3_client.list_objects_v2.return_value = {
            'Contents': [{'Key': 'file1'}, {'Key': 'file2'}]
        }
        
        result = self.aws_services.count_s3_objects('test-bucket')
        self.assertIn('2 arquivo(s)', result)
        self.assertIn('test-bucket', result)
    
    def test_count_s3_objects_empty_bucket(self):
        """Testar contagem de objetos em bucket vazio"""
        self.mock_s3_client.list_objects_v2.return_value = {}
        
        result = self.aws_services.count_s3_objects('empty-bucket')
        self.assertIn('Vazio (0 arquivos)', result)
    
    def test_count_s3_objects_bucket_not_found(self):
        """Testar contagem de objetos em bucket inexistente"""
        self.mock_s3_client.list_objects_v2.side_effect = ClientError(
            {'Error': {'Code': 'NoSuchBucket'}}, 'ListObjectsV2'
        )
        
        result = self.aws_services.count_s3_objects('nonexistent-bucket')
        self.assertIn('não encontrado', result)
    
    def test_list_ec2_instances_success(self):
        """Testar listagem de instâncias EC2 com sucesso"""
        self.mock_ec2_client.describe_instances.return_value = {
            'Reservations': [{
                'Instances': [{
                    'InstanceId': 'i-123456789',
                    'InstanceType': 't3.micro',
                    'State': {'Name': 'running'},
                    'LaunchTime': MagicMock()
                }]
            }]
        }
        
        result = self.aws_services.list_ec2_instances()
        self.assertIn('i-123456789', result)
        self.assertIn('t3.micro', result)
        self.assertIn('running', result)
        self.assertIn('🟢', result)  # Emoji verde para running
    
    def test_list_ec2_instances_empty(self):
        """Testar listagem de instâncias EC2 vazia"""
        self.mock_ec2_client.describe_instances.return_value = {'Reservations': []}
        
        result = self.aws_services.list_ec2_instances()
        self.assertIn('Nenhuma instância EC2 encontrada', result)
    
    @patch('aws_services.boto3')
    def test_init_no_credentials(self, mock_boto3):
        """Testar inicialização sem credenciais"""
        mock_boto3.client.side_effect = NoCredentialsError()
        
        with self.assertRaises(Exception) as context:
            AWSServices()
        
        self.assertIn('Credenciais AWS não configuradas', str(context.exception))

if __name__ == '__main__':
    unittest.main()