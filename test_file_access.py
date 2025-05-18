import os
import logging
import sys

# Configure logging to console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def test_files():
    uploads_dir = 'uploads'
    print(f"Testing uploads directory: {uploads_dir}")
    
    # Check if uploads directory exists
    if not os.path.exists(uploads_dir):
        logger.error(f"Directory '{uploads_dir}' does not exist")
        os.makedirs(uploads_dir, exist_ok=True)
        logger.info(f"Created directory '{uploads_dir}'")
    else:
        logger.info(f"Directory '{uploads_dir}' exists")
    
    # List files in uploads directory
    try:
        files = os.listdir(uploads_dir)
        if not files:
            logger.info(f"Directory '{uploads_dir}' is empty")
        else:
            logger.info(f"Files in '{uploads_dir}': {files}")
    except Exception as e:
        logger.error(f"Error listing directory: {str(e)}")
    
    # Test file path
    test_file_path = os.path.join(uploads_dir, 'Inicial.pdf')
    logger.info(f"Testing file path: {test_file_path}")
    
    if os.path.exists(test_file_path):
        logger.info(f"File '{test_file_path}' exists")
    else:
        logger.error(f"File '{test_file_path}' does not exist")
        
        # Create an empty test file to verify write permissions
        try:
            with open(test_file_path, 'w') as f:
                f.write("Test file")
            logger.info(f"Created test file '{test_file_path}'")
            
            # Remove the test file
            os.remove(test_file_path)
            logger.info(f"Removed test file '{test_file_path}'")
        except Exception as e:
            logger.error(f"Error creating test file: {str(e)}")

if __name__ == "__main__":
    try:
        logger.info("Starting file access test")
        test_files()
        logger.info("Test completed")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True) 