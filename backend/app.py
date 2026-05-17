from flask import Flask, jsonify
from flask_cors import CORS  # Importação necessária

app = Flask(__name__)
# Permite que qualquer origem (incluindo o Next.js na porta 3000) acesse a API sem bloqueios
CORS(app, resources={r"/*": {"origins": "*"}})

# --- CONCEITO DE POO: CLASSE BASE PARA HERANÇA ---
class EntidadeBase:
    """Classe mãe para fornecer métodos utilitários, como conversão para dicionário."""
    def to_dict(self):
        # Retorna os atributos do objeto como um dicionário de forma limpa
        return vars(self)

# --- SUAS CLASSES REFACTORADAS COM HERANÇA ---

class Continente(EntidadeBase):
    def __init__(self, nome, area_km2=0, populacao=0, lingua_oficial='Português', regioes=None):
        self.nome = nome
        self.area_km2 = area_km2
        self.populacao = populacao
        self.lingua_oficial = lingua_oficial
        self.regioes = [] if regioes is None else regioes

class Satelite(EntidadeBase):
    def __init__(self, nome, funcao='Pesquisa', status='Ativo', altitude=0, fabricante=''):
        self.nome = nome
        self.funcao = funcao
        self.status = status
        self.altitude = altitude
        self.fabricante = fabricante

class Foguete(EntidadeBase):
    def __init__(self, componente, descricao='', quantidade=1, peso=0, ativo=True):
        self.componente = componente
        self.nome = componente # Adicionado para espelhar o título perfeitamente no Next.js
        self.descricao = descricao
        self.quantidade = quantidade
        self.peso = peso
        self.ativo = ativo

class Chip(EntidadeBase):
    def __init__(self, nome, tipo='', fabricante='', consumo=0, tecnologia=''):
        self.nome = nome
        self.tipo = tipo
        self.fabricante = fabricante
        self.consumo = consumo
        self.tecnologia = tecnologia

class Plano(EntidadeBase):
    def __init__(self, nome, velocidade='100 Mbps', preco=0.0, franquia='Ilimitada', tipo='Residencial'):
        self.nome = nome
        self.velocidade = velocidade
        self.preco = preco
        self.franquia = franquia
        self.tipo = tipo

# --- INSTÂNCIAS (OBJETOS) ---
continentes = [
    Continente('América', 42549000, 1002000000, 'Espanhol/Português/Inglês', ['Norte', 'Central', 'Sul']),
    Continente('África', 30370000, 1340000000, 'Árabe/Francês/Inglês', ['Norte', 'Sahel', 'Sul', 'Leste', 'Oeste']),
    Continente('Ásia', 44579000, 4724000000, 'Chinês/Árabe/Hindi', ['Oriente Médio', 'Sul da Ásia']),
    Continente('Europa', 10180000, 747000000, 'Inglês/Alemão/Francês', ['Ocidental', 'Oriental']),
    Continente('Oceania', 8525989, 42000000, 'Inglês', ['Austrália'])
]

satelites = [
    Satelite('Starlink V2', 'Internet banda larga', 'Ativo', 550, 'SpaceX'),
    Satelite('GPS III', 'Navegação', 'Ativo', 20200, 'Lockheed Martin'), 
    Satelite('Sensor Térmico', 'Climatologia', 'Manutenção', 400, 'NASA')
]

foguetes = [
    Foguete('Falcon 9', 'Propulsor principal reutilizável', 1, 549000), 
    Foguete('Falcon Heavy', 'Foguete de carga super pesada', 3, 1420000), 
    Foguete('Starship', 'Sistema de transporte totalmente reutilizável', 1, 5000000)
]

chips = [
    Chip('Silicio Quântico', 'Processador', 'TSMC', 15, '3nm'), 
    Chip('Transistor RF', 'Amplificador de Sinal', 'Intel', 5, '7nm'), 
    Chip('Conector Óptico', 'Interface de Dados', 'Nvidia', 2, 'Laser')
]

planos = [
    Plano('Mini', '50 Mbps', 49.9, '100 GB', 'Mobilidade'), 
    Plano('Residencial', '150 Mbps', 99.9, 'Ilimitada', 'Fixo'),
    Plano('Business', '350 Mbps', 249.9, 'Ilimitada', 'Corporativo')
]

# --- ROTAS DA API ---

@app.route('/')
def home():
    return "API Starlink Ativa!"

@app.route('/continentes', methods=['GET'])
def get_continentes():
    return jsonify([c.to_dict() for c in continentes])

@app.route('/satelites', methods=['GET'])
def get_satelites():
    return jsonify([s.to_dict() for s in satelites])

@app.route('/foguetes', methods=['GET'])
def get_foguetes():
    return jsonify([f.to_dict() for f in foguetes])

@app.route('/chips', methods=['GET'])
def get_chips():
    return jsonify([ch.to_dict() for ch in chips])

@app.route('/planos', methods=['GET'])
def get_planos():
    return jsonify([p.to_dict() for p in planos])

if __name__ == '__main__':
    # Roda o servidor localmente na porta 5000
    app.run(host='127.0.0.1', port=5000, debug=True)