# GitHubSample 프로젝트 상세 가이드

	```

이 문서는 VS Code 환경에서 Git 및 GitHub를 사용하여 Public 저장소를 생성하고, 로컬 소스를 동기화하는 전체 과정을 단계별로 안내합니다.

## 1. Git 설치

1. [Git 공식 사이트](https://git-scm.com/)에서 운영체제에 맞는 Git 설치 파일을 다운로드합니다.
2. 설치 마법사의 기본 옵션을 따라 Git을 설치합니다.
3. 설치가 완료되면 터미널(명령 프롬프트, PowerShell 등)에서 아래 명령어로 정상 설치 여부를 확인합니다.
   ```sh
   git --version
   ```

## 2. Git 사용자 정보(user.name, user.email) 설정 방법

Git에서 커밋 시 아래와 같은 오류가 발생할 수 있습니다:

> Make sure you configure your "user.name" and "user.email" in git.

이 경우 아래 명령어로 사용자 정보를 설정하세요.

```sh
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

설정 후 이미 커밋한 경우, 작성자 정보를 수정하려면 아래 명령어를 사용하세요.

```sh
git commit --amend --reset-author
```

## 3. GitHubSample 저장소 생성 및 동기화

### 3-1. 로컬 프로젝트 폴더 준비
1. 작업할 폴더(예: `C:\Repository\GitHubSample`)를 생성하고 해당 폴더로 이동합니다.

### 3-2. Python Hello World 소스 작성
1. `hello.py` 파일을 생성하고 아래와 같이 작성합니다.
   ```python
   print("Hello, World!")
   ```

### 3-3. Git 저장소 초기화
1. 터미널에서 아래 명령어로 로컬 Git 저장소를 초기화합니다.
   ```sh
   git init
   ```

### 3-4. GitHub CLI 설치 및 인증
1. [GitHub CLI 설치 안내](https://cli.github.com/)에 따라 gh CLI를 설치합니다.
2. 아래 명령어로 GitHub 계정 인증을 진행합니다.
   ```sh
   gh auth login
   ```

### 3-5. 원격 GitHub 저장소 생성
1. 아래 명령어로 Public 저장소를 생성하고, Python .gitignore 파일을 추가합니다.
   ```sh
   gh repo create GitHubSample --public --source=. --remote=origin
   ```

### 3-6. 파일 스테이징 및 커밋
1. 모든 파일을 스테이징합니다.
   ```sh
   git add .
   ```
2. 첫 커밋을 생성합니다.
   ```sh
   git commit -m "Initial commit: Add Hello World and .gitignore"
   ```

### 3-7. 원격 저장소로 푸시
1. main 브랜치로 커밋을 푸시합니다.
   ```sh
   git push -u origin main
   ```

### 3-8. README.md 작성 및 반영
1. 본 README.md 파일을 작성하고, 아래 명령어로 커밋 및 푸시합니다.
   ```sh
   git add README.md
   git commit -m "Add README.md with project summary"
   git push
   ```

---


## 4. .gitignore 설정 방법

1. Python 프로젝트에서 불필요한 파일(캐시, 빌드, 환경설정 등)이 Git에 포함되지 않도록 `.gitignore` 파일을 설정합니다.
2. 아래 명령어로 Python용 기본 .gitignore 파일을 생성할 수 있습니다.
   ```sh
   gh repo create ... --gitignore=Python
   ```
   또는 직접 `.gitignore` 파일을 만들고 아래와 같이 작성합니다.
   ```
   __pycache__/
   *.pyc
   *.pyo
   *.pyd
   .venv/
   .env/
   # 기타 Python 관련 무시 패턴...
   ```

## 5. 변경 내용을 커밋하는 방법

1. 변경 사항을 저장합니다.
2. 터미널에서 아래 명령어를 입력합니다:

```
git add .
git commit -m "커밋 메시지"
git push
```

- `git add .` : 모든 변경 파일을 스테이징합니다.
- `git commit -m "메시지"` : 커밋 메시지와 함께 변경 사항을 커밋합니다.
- `git push` : 원격 저장소에 커밋을 업로드합니다.

## 6. Python 라이브러리 설치 및 가상환경(.venv) 사용 방법

1. 터미널에서 아래 명령어로 가상환경을 생성합니다.

```
python -m venv .venv
```

2. 가상환경을 활성화합니다.
- Windows:
```
.venv\Scripts\activate
```
- macOS/Linux:
```
source .venv/bin/activate
```

3. 필요한 라이브러리(예: requests)를 설치합니다.
```
pip install requests
```

4. hello.py를 실행하여 동작을 확인합니다.
```
python hello.py
```

---
