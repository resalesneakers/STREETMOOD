# Script para fazer push automático para GitHub
# Este script prepara tudo e abre o GitHub Desktop

$gitPath = (Get-ChildItem "$env:LOCALAPPDATA\GitHubDesktop\app-*\resources\app\git\cmd\git.exe" | Sort-Object LastWriteTime -Descending | Select-Object -First 1).FullName

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "STREETMOOD - Push para GitHub" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se já existe remote
$remote = & $gitPath remote get-url origin 2>$null

if ($remote) {
    Write-Host "[INFO] Remote já configurado: $remote" -ForegroundColor Green
    Write-Host ""
    Write-Host "Fazendo push..." -ForegroundColor Yellow
    & $gitPath push -u origin main
    Write-Host ""
    Write-Host "[SUCESSO] Push concluído!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Agora vai ao GitHub e ativa Pages:" -ForegroundColor Cyan
    Write-Host "1. Vai ao teu repositório no GitHub" -ForegroundColor White
    Write-Host "2. Settings -> Pages" -ForegroundColor White
    Write-Host "3. Source: main -> Save" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host "[INFO] Remote não configurado ainda." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "PASSO 1: Cria o repositório no GitHub:" -ForegroundColor Cyan
    Write-Host "1. Vai a: https://github.com/new" -ForegroundColor White
    Write-Host "2. Nome: streetmood-catalog" -ForegroundColor White
    Write-Host "3. Public" -ForegroundColor White
    Write-Host "4. NÃO marques 'Initialize with README'" -ForegroundColor White
    Write-Host "5. Clica 'Create repository'" -ForegroundColor White
    Write-Host ""
    
    $username = Read-Host "Qual é o teu username do GitHub?"
    
    if ($username) {
        Write-Host ""
        Write-Host "Configurando remote..." -ForegroundColor Yellow
        & $gitPath remote add origin "https://github.com/$username/streetmood-catalog.git"
        Write-Host "[OK] Remote configurado!" -ForegroundColor Green
        Write-Host ""
        Write-Host "Fazendo push..." -ForegroundColor Yellow
        & $gitPath push -u origin main
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "[SUCESSO] Push concluído!" -ForegroundColor Green
            Write-Host ""
            Write-Host "Agora ativa GitHub Pages:" -ForegroundColor Cyan
            Write-Host "1. Vai a: https://github.com/$username/streetmood-catalog/settings/pages" -ForegroundColor White
            Write-Host "2. Source: main -> Save" -ForegroundColor White
            Write-Host ""
            Write-Host "O teu site estará em:" -ForegroundColor Yellow
            Write-Host "https://$username.github.io/streetmood-catalog/" -ForegroundColor Green
        } else {
            Write-Host ""
            Write-Host "[ERRO] Falha no push. Verifica:" -ForegroundColor Red
            Write-Host "- O repositório foi criado no GitHub?" -ForegroundColor White
            Write-Host "- O nome do repositório está correto?" -ForegroundColor White
            Write-Host "- Estás autenticado no GitHub Desktop?" -ForegroundColor White
            Write-Host ""
            Write-Host "Abrindo GitHub Desktop para fazer push manualmente..." -ForegroundColor Yellow
            Start-Process "$env:LOCALAPPDATA\GitHubDesktop\GitHubDesktop.exe"
        }
    }
}

Write-Host ""
Write-Host "Pressiona Enter para sair..."
Read-Host

