## Amazon Transcribe Sample Unit Test

A quick code snippet on how to test Amazon Transcibe with moto

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