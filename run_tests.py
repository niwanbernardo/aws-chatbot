#!/usr/bin/env python3
"""
Script para executar todos os testes do projeto
"""
import subprocess
import sys
import os

def run_tests():
    """Executar todos os testes com coverage"""
    print("🧪 Executando testes automatizados...\n")
    
    # Verificar se pytest está instalado
    try:
        import pytest
    except ImportError:
        print("❌ pytest não encontrado. Instale com: pip install pytest pytest-cov")
        return False
    
    # Executar testes unitários
    print("📋 Executando testes unitários...")
    result_unit = subprocess.run([
        sys.executable, '-m', 'pytest', 
        'tests/test_app.py', 'tests/test_aws_services.py',
        '-v', '--tb=short'
    ], capture_output=True, text=True)
    
    print(result_unit.stdout)
    if result_unit.stderr:
        print(result_unit.stderr)
    
    # Executar testes de integração
    print("\n🔗 Executando testes de integração...")
    result_integration = subprocess.run([
        sys.executable, '-m', 'pytest', 
        'tests/test_integration.py',
        '-v', '--tb=short'
    ], capture_output=True, text=True)
    
    print(result_integration.stdout)
    if result_integration.stderr:
        print(result_integration.stderr)
    
    # Executar todos os testes com coverage
    print("\n📊 Executando análise de cobertura...")
    result_coverage = subprocess.run([
        sys.executable, '-m', 'pytest', 
        'tests/',
        '--cov=.',
        '--cov-report=term-missing',
        '--cov-report=html:htmlcov'
    ], capture_output=True, text=True)
    
    print(result_coverage.stdout)
    if result_coverage.stderr:
        print(result_coverage.stderr)
    
    # Verificar resultados
    success = (result_unit.returncode == 0 and 
               result_integration.returncode == 0 and 
               result_coverage.returncode == 0)
    
    if success:
        print("\n✅ Todos os testes passaram!")
        print("📊 Relatório de cobertura gerado em: htmlcov/index.html")
    else:
        print("\n❌ Alguns testes falharam.")
    
    return success

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)