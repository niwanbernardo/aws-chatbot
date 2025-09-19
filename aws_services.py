import boto3
from datetime import datetime, timedelta
from botocore.exceptions import ClientError, NoCredentialsError

class AWSServices:
    def __init__(self):
        try:
            self.s3_client = boto3.client('s3')
            self.ec2_client = boto3.client('ec2')
            self.ce_client = boto3.client('ce')
        except NoCredentialsError:
            raise Exception("Credenciais AWS não configuradas. Configure suas credenciais AWS.")
    
    def get_cost_estimate(self):
        try:
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=30)
            
            response = self.ce_client.get_cost_and_usage(
                TimePeriod={
                    'Start': start_date.strftime('%Y-%m-%d'),
                    'End': end_date.strftime('%Y-%m-%d')
                },
                Granularity='MONTHLY',
                Metrics=['BlendedCost']
            )
            
            if response['ResultsByTime']:
                amount = response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']
                currency = response['ResultsByTime'][0]['Total']['BlendedCost']['Unit']
                return f"💰 **Custos dos últimos 30 dias:** {currency} ${float(amount):.2f}"
            else:
                return "📊 Não foi possível obter informações de custo no momento."
                
        except ClientError as e:
            return f"❌ Erro ao obter custos: {e.response['Error']['Message']}"
        except Exception as e:
            return f"❌ Erro inesperado: {str(e)}"
    
    def list_s3_buckets(self):
        try:
            response = self.s3_client.list_buckets()
            buckets = response['Buckets']
            
            if not buckets:
                return "📦 Nenhum bucket S3 encontrado."
            
            bucket_list = "🗂️ **Seus buckets S3:**\n\n"
            for bucket in buckets:
                bucket_list += f"• {bucket['Name']} (criado em {bucket['CreationDate'].strftime('%d/%m/%Y')})\n"
            
            return bucket_list
            
        except ClientError as e:
            return f"❌ Erro ao listar buckets: {e.response['Error']['Message']}"
        except Exception as e:
            return f"❌ Erro inesperado: {str(e)}"
    
    def count_s3_objects(self, bucket_name):
        try:
            response = self.s3_client.list_objects_v2(Bucket=bucket_name)
            
            if 'Contents' in response:
                count = len(response['Contents'])
                return f"📁 **Bucket '{bucket_name}':** {count} arquivo(s) encontrado(s)"
            else:
                return f"📁 **Bucket '{bucket_name}':** Vazio (0 arquivos)"
                
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchBucket':
                return f"❌ Bucket '{bucket_name}' não encontrado."
            else:
                return f"❌ Erro ao acessar bucket: {e.response['Error']['Message']}"
        except Exception as e:
            return f"❌ Erro inesperado: {str(e)}"
    
    def list_ec2_instances(self):
        try:
            response = self.ec2_client.describe_instances()
            
            instances = []
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instances.append({
                        'id': instance['InstanceId'],
                        'type': instance['InstanceType'],
                        'state': instance['State']['Name'],
                        'launch_time': instance['LaunchTime']
                    })
            
            if not instances:
                return "🖥️ Nenhuma instância EC2 encontrada."
            
            instance_list = "🖥️ **Suas instâncias EC2:**\n\n"
            for instance in instances:
                status_emoji = "🟢" if instance['state'] == 'running' else "🔴" if instance['state'] == 'stopped' else "🟡"
                instance_list += f"{status_emoji} **{instance['id']}** ({instance['type']}) - {instance['state']}\n"
            
            return instance_list
            
        except ClientError as e:
            return f"❌ Erro ao listar instâncias: {e.response['Error']['Message']}"
        except Exception as e:
            return f"❌ Erro inesperado: {str(e)}"