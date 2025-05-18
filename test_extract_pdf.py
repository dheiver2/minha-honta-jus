import os
import logging
import sys
import fitz  # PyMuPDF

# Configure logging to console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyMuPDF"""
    text = ""
    try:
        # Verificar se o arquivo existe antes de tentar abri-lo
        if not os.path.exists(pdf_path):
            logger.error(f"Arquivo PDF não encontrado: {pdf_path}")
            return f"Error: O arquivo {pdf_path} não foi encontrado"
        
        # Open the PDF file
        logger.info(f"Abrindo arquivo PDF: {pdf_path}")
        pdf_document = fitz.open(pdf_path)
        
        # Get the number of pages
        num_pages = len(pdf_document)
        logger.info(f"Extraindo texto de PDF com {num_pages} páginas")
        
        # Extract text from each page
        for page_num in range(num_pages):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
            
        # Close the PDF file
        pdf_document.close()
        
        logger.info(f"Texto extraído com sucesso: {len(text)} caracteres")
        return text
    except Exception as e:
        logger.error(f"Erro ao extrair texto do PDF: {str(e)}")
        return f"Error extracting text from PDF: {str(e)}"

if __name__ == "__main__":
    # Test with existing file
    test_pdf = os.path.join('uploads', 'test.pdf')
    logger.info(f"Testando extração de PDF de arquivo existente: {test_pdf}")
    text = extract_text_from_pdf(test_pdf)
    print(f"Extracted text: {text}")
    
    # Test with non-existent file
    non_existent_pdf = os.path.join('uploads', 'Inicial.pdf')
    logger.info(f"Testando extração de PDF de arquivo inexistente: {non_existent_pdf}")
    text = extract_text_from_pdf(non_existent_pdf)
    print(f"Result for non-existent file: {text}") 