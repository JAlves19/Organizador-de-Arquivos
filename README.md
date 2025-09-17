# Organizador-de-Arquivos

## Descrição
Este é um script simples em Python criado por [Seu Nome] para organizar arquivos em uma pasta com base em suas extensões. Ele cria subpastas como "imagens", "docs", "videos", "audios" e "outros", movendo arquivos automaticamente (ex.: .jpg vai para "imagens", .pdf para "docs"). O projeto foi desenvolvido em 16/09/2025, 23:11 -03, como parte do meu aprendizado em automação e manipulação de arquivos.

## Como Usar
1. Salve o arquivo `file_organizer.py` em uma pasta de sua escolha.
2. Abra o script e ajuste o caminho na variável `pasta` (ex.: `"C:/Users/SeuNome/Desktop/PastaTeste"`).
3. Execute o script no terminal com: `python file_organizer.py`.
4. Verifique as subpastas criadas e os arquivos movidos.

## Pré-requisitos
- Python 3.x instalado no seu computador.
- Nenhum pacote externo é necessário (usa apenas `os` e `shutil`).

## O que Aprendi
- Como usar `os` para manipular pastas e arquivos.
- A importância de `shutil.move` para mover arquivos com segurança.
- Como organizar código com dicionários e loops.

## Melhorias Futuras
- Adicionar suporte a mais extensões (ex.: .zip, .rar).
- Criar uma interface interativa com `input()` para escolher a pasta.
- Incluir uma opção para desfazer as mudanças.

## Licença
[Opcional] Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.
