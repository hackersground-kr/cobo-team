# `CoBo` - `CoBoAI`

해커그라운드 해커톤에 참여하는 `CoBo` 팀의 `CoBoAI`입니다.

## 참고 문서

> 아래 두 링크는 해커톤에서 앱을 개발하면서 참고할 만한 문서들입니다. 이 문서들에서 언급한 서비스 이외에도 더 많은 서비스들이 PaaS, SaaS, 서버리스 형태로 제공되니 참고하세요.

- [순한맛](./REFERENCES_BASIC.md)
- [매운맛](./REFERENCES_ADVANCED.md)

## 제품/서비스 소개

<!-- 아래 링크는 지우지 마세요 -->
[제품/서비스 소개 보기](TOPIC.md)
<!-- 위 링크는 지우지 마세요 -->

## 오픈 소스 라이센스

<!-- 아래 링크는 지우지 마세요 -->
[오픈소스 라이센스 보기](./LICENSE)
<!-- 위 링크는 지우지 마세요 -->

## 기능 구현 과정

- 음성 인식->텍스트로 변환하는 과정 구현(파이썬, azure potal에서 음성 리소스 만들기, 파이썬용 speech sdk를 통해 환경 설정, 환경 변수 설정, 언어-한국어 설정), 애저 참고(https://learn.microsoft.com/ko-kr/azure/cognitive-services/speech-service/get-started-speech-to-text?tabs=windows%2Cterminal&pivots=programming-language-python), "코보"를 인식할 때까지 음성 인식을 하는 함수 반복 실행, "코보" 인식 시, 음성->텍스트 변환 시작, 만약 문장 인식을 못하였을 경우 다시 음성->텍스트 변환 함수 호출

- Open Ai(chatgpt)와 상호작용 과정 구현(파이썬), 참고(https://platform.openai.com/docs/guides/gpt), chatgpt API 요청 후 상호작용, 그리고 그 결과 반환

- 텍스트->음성으로 출력하는 과정 구현(파이썬, azure potal에서 음성 리소스 만들기, 파이썬용 speech sdk를 통해 환경 설정, 환경 변수 설정, 언어-한국어 설정), 애저 참고(https://azure.microsoft.com/ko-kr/products/cognitive-services/text-to-speech/#features), ai와의 대화를 통하여 얻은 답변으로 부터 받은 text를 음성으로 출력

- 프론트엔드 구현(html, js, css 활용), 음파에 따라 진동하는 주파수 디자인 넣기

- 리소스로 생성하기 위해 이전의 기능들을 깃헙에 총 정리 (추가적으로, 파이썬 기반 프레임워크인 Flask 설치, pip install flask로 웹 어플리케이션 개발 준비하는 코드 작성)

- 시간을 인식하고 아침, 점심, 저녁과 같은 특정 시간이 된 경우 코보 Ai가 대화를 시작, 시간대별로 미리 설정되어있는 대화 질문들 중 랜덤으로 하나를 질문으로 던짐

## 설치 방법

> **아래 제공하는 설치 방법을 통해 심사위원단이 여러분의 제품/서비스를 실제 Microsoft 애저 클라우드에 배포하고 설치할 수 있어야 합니다. 만약 아래 설치 방법대로 따라해서 배포 및 설치가 되지 않을 경우 본선에 진출할 수 없습니다.**

# 사전준비사항
- Azure 구독 계정
- GitHub 계정

# 시작하기
## 1. main Fork 해서 repository 만들기

## 2. Azure App Services 리소스 만들기
- https://portal.azure.com 접속
- 만들기 > 웹 앱
- 리소스 그룹 선택
- 웹 앱 이름 설정 
- 게시 - 코드
- 런타임 스택 - 3.9
- 운영 체제 - 리눅스
- 지역 - Korea South

 리소스가 만들어지면, 배포 - 배포 센터에 들어가 설정을 수정합니다. 
소스를 GitHub으로 설정하고, 조직과 리포지토리를 처음 Fork 한 곳으로 설정합니다. 
분기를 설정하고 워크플로 추가 후 저장합니다.

## 3. Azure의 Speech Services 리소스 만들기
- https://portal.azure.com 접속
- 리소스 그룹 선택
- 지역 - Korea Central

 리소스가 만들어지면, 리소스 관리 - 키 및 엔드포인트 의 키 값을 복사합니다. 
speechToText.py 파일과 textToSpeech.py 파일의 speech_key 값에 복사한 값을 넣습니다.

## 4. OpenAI의 api 사용하기.
- https://platform.openai.com/account/api-keys 접속
  
 시크릿 키를 생성하고, 생성한 키를 복사해 저장합니다. 
chatGptApi.py 파일을 열어 openai.api_key 값에 복사한 키를 넣습니다.
 
## 5. GitHub Actions를 이용한 배포
 생성한 워크플로를 이용해 빌드를 진행합니다. 
 웹 앱 리소스의 기본 도메인을 통해 배포를 확인하십시오.
