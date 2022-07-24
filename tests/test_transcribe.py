import os
import unittest

import boto3
from moto import mock_transcribe


@mock_transcribe()
class TranscibeTest(unittest.TestCase):

    def aws_credentials(self):
        """Mocked AWS Credentials for moto."""
        os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
        os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
        os.environ['AWS_SECURITY_TOKEN'] = 'testing'
        os.environ['AWS_SESSION_TOKEN'] = 'testing'
        os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

    def test_start_transcribe(self):
        """Unit Test to test out connection to amazon transcribe"""
        import src.transcribe as transcribe
        file_name = 'test_audio.wav'
        transcribe_client = boto3.client('transcribe', region_name='us-east-1')
        transcribe_manager = transcribe.TranscibeBatch(
            bucket_name='test_bucket',
            file_name=file_name
        )
        transcribe_manager.start_transcribe()
        response = transcribe_client.list_transcription_jobs()

        assert response['TranscriptionJobSummaries'][0]['TranscriptionJobName'] == file_name
