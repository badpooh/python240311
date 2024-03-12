import re

# 샘플 데이터
sample_data = """
이메일 주소는 abc@example.com 입니다.
다른 이메일은 test@test.com 과 xyz@gmail.com 입니다.
abc@domaincom 으로 잘못 입력되었습니다.
"""

# 이메일 주소를 찾는 정규표현식
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# 샘플 데이터에서 이메일 주소를 찾아내는 함수
def find_email(text):
    match = re.search(email_regex, text)
    if match:
        return match.group()
    else:
        return None

# 샘플 데이터에서 이메일 주소를 찾아 출력
email_found = find_email(sample_data)
if email_found:
    print("Found email address:", email_found)
else:
    print("No email address found in the sample data.")
