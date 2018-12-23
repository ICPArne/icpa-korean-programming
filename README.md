# 3기 ICPA R&E: 한글 프로그래밍 언어 제작
인천포스코고등학교 3기 R&E- 초등 교육을 위한 한글 프로그래밍 언어 '고래'입니다.

<언어 사용법>
- 해당 폴더에 첨부되어 있는 whales.exe의 경우 Pyinstaller의 onefile 기능을 사용하여 제작되어, 초기 실행 속도에 지연이 존재합니다. (whale.py의 경우 지연 없음)
- 이를 해결하기 위해 PyPI에 패키지를 배포하였습니다. "pip install whale"을 이용해 설치하신 후, "from whale import whale"을 이용해 실행하시면 됩니다. (2018년 12월 24일 기준, 최신 버전은 1.1.2입니다. 이하의 버전에서는 작동이 되지 않으므로 반드시 1.1.2 버전을 설치하시길 바랍니다.)
- 구문 분석 파일은 silhaeng.py, 토큰 관련 파일은 token_p.py를 참조하시고 사용법은 Keyword.txt나 Example.txt를 참조하시길 바랍니다.

<실행 파일 사용법>
- '작성시작' 입력 시 코드를 자유롭게 작성할 수 있는 창이 열립니다.
  코드를 다 작성한 후 F5를 누를 경우 작성한 코드가 실행됩니다.
- '기존코드' 입력 시 기존에 '작성시작'을 통해 입력했던 코드가 그대로 들어있는 창이 열립니다.
  이를 통해 기존에 작성한 코드를 수정 및 재실행할 수 있습니다.
- '종료' 입력 시 프로그램이 종료됩니다.
  기존에 저장되어 있던 코드는 모두 저장되지 않고 사라집니다.
- 그 외의 경우에는 일반적인 인터프리터 언어의 형태로 작동합니다.

<기타>
버그가 발생했을 경우 pjc05@naver.com으로 보내주시기 바랍니다.
