import logging
from urllib import response

import constants as c
import transcribe

logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    bucket_name = 'test_bucket'
    audio_file = event['Records'][0]['body']
    try:
        trans = transcribe.TranscibeBatch(
            bucket_name=bucket_name,
            file_name=audio_file
        )
        response = trans.start_transcribe()
        return response
    except Exception as e:
        logging.info(f"The following exception occured when calling Amazon transcribe {e}")
        raise e



if __name__ == "__main__":
    lambda_handler(c.S3_EVENT, "")
