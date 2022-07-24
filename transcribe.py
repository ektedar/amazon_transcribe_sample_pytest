import logging

import boto3

client = boto3.client('transcribe', region_name='us-east-1')
logging.basicConfig(level=logging.INFO)

class TranscibeBatch:

    def __init__(self, bucket_name, file_name) -> None:
        self.bucket_name = bucket_name
        self.file_name = file_name
    

    def start_transcribe(self) -> dict:
        try:
            logging.info("Attempting to begin transcription")
            response = client.start_transcription_job(
                TranscriptionJobName=self.file_name,
                LanguageCode='en-US',
                Media={
                    'MediaFileUri': self.bucket_name+'/'+self.file_name
                }
            )
            logging.info(response)
            return response
        except Exception as e:
            logging.info(f"The following exception occured when calling Amazon transcribe {e}")
            raise e
