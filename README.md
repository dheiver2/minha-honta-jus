# Minha Honra Jus

Sistema inteligente de geração de documentos jurídicos, especializado em contestações e outros documentos processuais.

## Sobre o Projeto

O Minha Honra Jus é uma plataforma que utiliza inteligência artificial para auxiliar advogados na geração de documentos jurídicos. O sistema analisa petições iniciais e modelos de contestação para criar documentos profissionais e bem fundamentados.

### Funcionalidades Principais

- **Análise Inteligente de Petições**: Extração automática de informações relevantes de petições iniciais
- **Geração de Contestação**: Criação de contestações jurídicas com argumentos sólidos e bem fundamentados
- **Formatação Profissional**: Documentos formatados de acordo com as normas jurídicas
- **Exportação Multi-formato**: Suporte para Word (DOCX) e texto (TXT)
- **Interface Intuitiva**: Design moderno e fácil de usar
- **Marca D'água**: Proteção dos documentos com marca d'água da plataforma

## Tecnologias Utilizadas

- **Backend**: Python 3.8+
- **Framework Web**: Flask
- **IA**: Google Gemini AI
- **Frontend**: HTML5, CSS3, JavaScript
- **Bibliotecas**:
  - python-docx: Geração de documentos Word
  - PyMuPDF: Processamento de PDFs
  - Bootstrap 5: Interface responsiva
  - Font Awesome: Ícones

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/minha-honta-jus.git
cd minha-honta-jus
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Execute o projeto:
```bash
python app.py
```

## Estrutura do Projeto

```
minha-honta-jus/
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências
├── .env               # Variáveis de ambiente
├── .gitignore        # Arquivos ignorados pelo git
├── templates/        # Templates HTML
│   ├── index.html    # Página inicial
│   └── resultado.html # Página de resultado
├── static/          # Arquivos estáticos
├── uploads/         # Uploads temporários
└── results/         # Resultados temporários
```

## Variáveis de Ambiente

- `GEMINI_API_KEY`: Chave da API do Google Gemini
- `SECRET_KEY`: Chave secreta para sessões Flask
- `UPLOAD_FOLDER`: Pasta para uploads temporários
- `RESULT_FOLDER`: Pasta para resultados temporários

## Uso

1. Acesse a interface web em `http://localhost:5000`
2. Faça upload da petição inicial (PDF)
3. Faça upload do modelo de contestação (PDF)
4. Aguarde o processamento
5. Revise o documento gerado
6. Baixe em Word ou TXT

## Formatação dos Documentos

Os documentos gerados seguem as seguintes especificações:

- **Fonte**: Times New Roman 12pt
- **Margens**: Superior e esquerda 3cm, inferior e direita 2cm
- **Espaçamento**: 1,5 entre linhas
- **Alinhamento**: Justificado
- **Recuo**: 2cm para início de parágrafo
- **Numeração**: Páginas no canto inferior direito

## Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit das mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autores

- **Dr Dheiver Francisco Santos** 

## Agradecimentos

- Google Gemini AI
- Comunidade open source
- Contribuidores do projeto

## Suporte

Para suporte, envie um email para suporte@minhahonrajus.com.br ou abra uma issue no GitHub. 
