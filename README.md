## Amazon Transcribe Sample Unit Test

A quick code snippet on how to test Amazon Transcibe with moto

## Current Moto Features for Amazon Transcibe
- [ ] create_medical_vocabulary
- [ ] create_vocabulary
- [ ] delete_medical_transcription_job
- [ ] delete_medical_vocabulary
- [ ] delete_transcription_job
- [ ] delete_vocabulary
- [ ] get_medical_transcription_job
- [ ] get_medical_vocabulary
- [ ] get_transcription_job
- [ ] get_vocabulary
- [ ] list_medical_transcription_jobs
- [ ] list_medical_vocabularies
- [x] list_transcription_jobs
- [ ] list_vocabularies
- [ ] start_medical_transcription_job
- [ ] start_transcription_job

More sample unit tests will be added to this repo soon to cover all the available motos

## Output Example

```bash
$ pytest -v
====================================================================================================== test session starts =======================================================================================================
platform win32 -- Python 3.9.12, pytest-7.1.2, pluggy-1.0.0 -- C:\Users\Ekted\miniconda3\envs\aws\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Ekted\OneDrive\Documents\projects\amazon_transcribe_testing
collected 1 item

tests/test_transcribe.py::TranscibeTest::test_start_transcribe PASSED                                                                                                                                                       [100%]

======================================================================================================= 1 passed in 0.41s ========================================================================================================
```