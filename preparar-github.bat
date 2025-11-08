@echo off
echo ========================================
echo STREETMOOD - Preparar para GitHub
echo ========================================
echo.

echo Verificando se Git esta instalado...
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERRO] Git nao encontrado!
    echo.
    echo Por favor instala Git primeiro:
    echo https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

echo [OK] Git encontrado!
echo.

echo Inicializando repositorio Git...
git init

echo.
echo Adicionando ficheiros...
git add index.html style.css scripts/ streetmood_images_mapping.json .gitignore README_SETUP.md 3d/README.md

echo.
echo Ficheiros essenciais adicionados!
echo.
echo Para adicionar TODOS os ficheiros (incluindo produtos e imagens):
echo   git add .
echo.
echo Para fazer commit:
echo   git commit -m "Initial commit: STREETMOOD catalog"
echo.
echo Para criar repositorio no GitHub:
echo   1. Vai a https://github.com/new
echo   2. Cria um repositorio PUBLICO chamado "streetmood-catalog"
echo   3. NAO inicializes com README
echo   4. Copia o comando que aparece no GitHub
echo   5. Executa aqui neste terminal
echo.
echo Exemplo do comando do GitHub:
echo   git remote add origin https://github.com/TEU-USERNAME/streetmood-catalog.git
echo   git branch -M main
echo   git push -u origin main
echo.
echo Depois de fazer push:
echo   1. Vai ao repositorio no GitHub
echo   2. Settings ^> Pages
echo   3. Source: main
echo   4. Save
echo.
echo O teu site estara em:
echo   https://TEU-USERNAME.github.io/streetmood-catalog/
echo.
pause

