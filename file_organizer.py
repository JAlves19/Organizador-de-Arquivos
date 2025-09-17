import os
import shutil

def organizar_arquivos(pasta_origem):
    # Dicionário de categorias e extensões associadas
    categorias = {
        'imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'docs': ['.pdf', '.txt', '.doc', '.docx', '.xls', '.xlsx'],
        'videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'audios': ['.mp3', '.wav', '.ogg'],
        'outros': []  # Para arquivos não categorizados
    }
    
    # Cria as subpastas se não existirem
    for categoria in categorias:
        subpasta = os.path.join(pasta_origem, categoria)
        if not os.path.exists(subpasta):
            os.makedirs(subpasta)
    
    # Lista todos os arquivos na pasta de origem
    for arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)
        
        # Ignora diretórios e arquivos ocultos
        if os.path.isdir(caminho_arquivo) or arquivo.startswith('.'):
            continue
        
        # Pega a extensão do arquivo
        extensao = os.path.splitext(arquivo)[1].lower()
        
        # Encontra a categoria apropriada
        movido = False
        for categoria, exts in categorias.items():
            if extensao in exts:
                destino = os.path.join(pasta_origem, categoria, arquivo)
                shutil.move(caminho_arquivo, destino)
                print(f'Movido: {arquivo} -> {categoria}')
                movido = True
                break
        
        # Se não encaixar em nenhuma, move para 'outros'
        if not movido:
            destino = os.path.join(pasta_origem, 'outros', arquivo)
            shutil.move(caminho_arquivo, destino)
            print(f'Movido: {arquivo} -> outros')

if __name__ == "__main__":
    pasta = "C:/Users/jvict/Desktop/PastaTeste"
    organizar_arquivos(pasta)