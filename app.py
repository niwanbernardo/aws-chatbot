from flask import Flask, render_template, request, jsonify
from aws_services import AWSServices
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
aws_services = AWSServices()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.json.get('message', '').lower().strip()
        
        if not message:
            return jsonify({'response': 'Por favor, digite uma mensagem.'})
        
        # Processar comandos
        if 'custos' in message:
            response = aws_services.get_cost_estimate()
        elif 's3 buckets' in message:
            response = aws_services.list_s3_buckets()
        elif 's3 arquivos' in message:
            bucket_name = message.replace('s3 arquivos', '').strip()
            if bucket_name:
                response = aws_services.count_s3_objects(bucket_name)
            else:
                response = "Por favor, especifique o nome do bucket. Exemplo: 's3 arquivos meu-bucket'"
        elif 'ec2 instancias' in message or 'ec2 instâncias' in message:
            response = aws_services.list_ec2_instances()
        elif 'ajuda' in message or 'help' in message:
            response = """
            🤖 **Comandos disponíveis:**
            
            • `custos` - Estimativa de custos da conta
            • `s3 buckets` - Lista todos os buckets S3
            • `s3 arquivos nome-do-bucket` - Conta arquivos em um bucket
            • `ec2 instancias` - Lista instâncias EC2
            • `ajuda` - Mostra esta mensagem
            
            📊 **Projeto TDC 2025 Q Developer Quest**
            Todas as 4 etapas concluídas! ✅
            """
        else:
            response = "Comando não reconhecido. Digite 'ajuda' para ver os comandos disponíveis."
        
        return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'response': f'Erro: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)