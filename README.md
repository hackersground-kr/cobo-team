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

## 설치 방법

> **아래 제공하는 설치 방법을 통해 심사위원단이 여러분의 제품/서비스를 실제 Microsoft 애저 클라우드에 배포하고 설치할 수 있어야 합니다. 만약 아래 설치 방법대로 따라해서 배포 및 설치가 되지 않을 경우 본선에 진출할 수 없습니다.**

## 1. 기능 구현 과정

- 음성 인식->텍스트로 변환하는 과정 구현(파이썬, azure potal에서 음성 리소스 만들기, 파이썬용 speech sdk를 통해 환경 설정, 환경 변수 설정, 언어-한국어 설정), 애저 참고(https://learn.microsoft.com/ko-kr/azure/cognitive-services/speech-service/get-started-speech-to-text?tabs=windows%2Cterminal&pivots=programming-language-python), "코보"를 인식할 때까지 음성 인식을 하는 함수 반복 실행, "코보" 인식 시, 음성->텍스트 변환 시작, 만약 문장 인식을 못하였을 경우 다시 음성->텍스트 변환 함수 호출

- Open Ai(chatgpt)와 상호작용 과정 구현(파이썬), 참고(https://platform.openai.com/docs/guides/gpt), chatgpt API 요청 후 상호작용, 그리고 그 결과 반환

- 텍스트->음성으로 출력하는 과정 구현(파이썬, azure potal에서 음성 리소스 만들기, 파이썬용 speech sdk를 통해 환경 설정, 환경 변수 설정, 언어-한국어 설정), 애저 참고(https://azure.microsoft.com/ko-kr/products/cognitive-services/text-to-speech/#features), ai와의 대화를 통하여 얻은 답변으로 부터 받은 text를 음성으로 출력

- 프론트엔드 구현(html, js, css 활용), 음파에 따라 진동하는 주파수 디자인 넣기

- 리소스로 생성하기 위해 이전의 기능들을 깃헙에 총 정리 (추가적으로, 파이썬 기반 프레임워크인 Flask 설치, pip install flask로 웹 어플리케이션 개발 준비하는 코드 작성)

- 시간을 인식하고 아침, 점심, 저녁과 같은 특정 시간이 된 경우 코보 Ai가 대화를 시작, 시간대별로 미리 설정되어있는 대화 질문들 중 랜덤으로 하나를 질문으로 던짐

## 2. 애저 포털에서 정적 웹 앱 만들기
애저 포털에서 리소스 만들기 선택, static web Apps 검색 및 선택, 만들기 선택, 이후 기본사항 섹션에서 앱 구성 후, 깃허브 리포지토리에 연결하여 만들기 시작

## 3. 웹 앱 배포

### 사전 준비 사항

> **여러분의 제품/서비스를 Microsoft 애저 클라우드에 배포하기 위해 사전에 필요한 준비 사항들을 적어주세요.**

Azure 계정 생성

깃허브 계정 및 레포지토리 생성

파이썬(3.7 버전이상) 및 vscode 설치

flask 설치 

애저구독을 하고있는 상태에서 OpenAi 사이트에서 OpenAi API키 발급 받기

## 시작하기

> **여러분의 제품/서비스를 Microsoft 애저 클라우드에 배포하기 위한 절차를 구체적으로 나열해 주세요.**

## 1. 환경 변수 설정
- 콘솔 창에 setx SPEECH_KEY your-key  setx SPEECH_REGION your-region 을 입력

## 2. 음성인식언어 변경
- en-US를 ko-KR로 변경

## 3. speech SDK 설치 
- 콘솔에 pip install azure-cognitiveservices-speech 명령 실행

## 4. OpenAi 선언
- OpenAi를 선언하고 사전 준비 사항에서 발급 받았던 OpenAi키를 입력란에 입력
 
## 5. ChatGPT와 상호 작용하는 함수 생성
- "def interact_with_chatgpt(prompt):"를 이용하여 생성

## 6. 조건 정하기
- ChatGPT API에 요청하여 여러 조건들을 정하기 (engine, temperature 등등)

## 7. 출력
- 상호작용 결과를 if else문을 이용하여 출력

## 8. Azure 웹앱 배포하기

- 본 진행에 앞서 Azure CLI가 설치되어있어야 합니다 (더 많은 정보: https://learn.microsoft.com/ko-kr/cli/azure/install-azure-cli)

## 9. Azure CLI에 다음의 명령어를 입력합니다

- `az login`

- 웹앱 및 기타 리소스를 만든 다음, az webapp up을 사용하여 Azure에 코드를 배포합니다.

## 10. Azure CLI에 다음의 명령어를 입력합니다

- `az webapp up --runtime PYTHON:3.9 --sku <요금제> --name <앱 이름>`

- --sku 매개 변수는 App Service 요금제의 크기(CPU, 메모리) 및 비용을 정의합니다.

App Service 요금제의 전체 목록은 App Service 가격 책정 페이지를 참조하세요.
요금제: B1(기본) 

웹 브라우저에서 배포된 애플리케이션(URL: http://`app-name`.azurewebsites.net)으로 이동합니다.

## 11. 축하합니다! Python 앱을 App Service에 배포했습니다.
