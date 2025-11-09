# Script para fazer upload do STREETMOOD para GitHub
# Repositório: https://github.com/srteetm00d-png/streetm00d_

Write-Host "🚀 STREETMOOD - Upload para GitHub" -ForegroundColor Cyan
Write-Host "Repositório: https://github.com/srteetm00d-png/streetm00d_" -ForegroundColor Yellow
Write-Host ""

# Verificar se Git está instalado
try {
    $gitVersion = git --version
    Write-Host "✅ Git encontrado: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git não está instalado!" -ForegroundColor Red
    Write-Host "Por favor, instala Git de: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Pressiona qualquer tecla para sair..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

Write-Host ""
Write-Host "🔄 Inicializando repositório Git..." -ForegroundColor Cyan

# Inicializar Git (se não existir)
if (-not (Test-Path ".git")) {
    git init
    Write-Host "✅ Repositório Git inicializado" -ForegroundColor Green
} else {
    Write-Host "✅ Repositório Git já existe" -ForegroundColor Green
}

# Verificar remote atual
Write-Host ""
Write-Host "🔍 Verificando remote atual..." -ForegroundColor Cyan
$currentRemote = git remote get-url origin 2>$null

if ($currentRemote) {
    Write-Host "Remote atual: $currentRemote" -ForegroundColor Yellow
    if ($currentRemote -ne "https://github.com/srteetm00d-png/streetm00d_.git") {
        Write-Host ""
        Write-Host "⚠️  Remote diferente encontrado. Atualizando..." -ForegroundColor Yellow
        git remote set-url origin https://github.com/srteetm00d-png/streetm00d_.git
        Write-Host "✅ Remote atualizado" -ForegroundColor Green
    } else {
        Write-Host "✅ Remote já está correto" -ForegroundColor Green
    }
} else {
    Write-Host "Adicionando remote..." -ForegroundColor Cyan
    git remote add origin https://github.com/srteetm00d-png/streetm00d_.git
    Write-Host "✅ Remote configurado" -ForegroundColor Green
}

# Verificar remote
Write-Host ""
Write-Host "📋 Remote configurado:" -ForegroundColor Cyan
git remote -v

# Adicionar ficheiros
Write-Host ""
Write-Host "📦 Adicionando ficheiros..." -ForegroundColor Cyan
git add .
Write-Host "✅ Ficheiros adicionados" -ForegroundColor Green

# Verificar se há mudanças para commit
$status = git status --porcelain
if ($status) {
    Write-Host ""
    Write-Host "💾 Fazendo commit..." -ForegroundColor Cyan
    git commit -m "Update: STREETMOOD website com 350 produtos, paginação e imagens"
    Write-Host "✅ Commit criado" -ForegroundColor Green
} else {
    Write-Host "ℹ️  Nenhuma mudança para commitar" -ForegroundColor Yellow
}

# Mudar para branch main
Write-Host ""
Write-Host "🌿 Configurando branch main..." -ForegroundColor Cyan
git branch -M main 2>$null
Write-Host "✅ Branch main configurada" -ForegroundColor Green

# Fazer push
Write-Host ""
Write-Host "🚀 Fazendo push para GitHub..." -ForegroundColor Cyan
Write-Host "⚠️  Será pedido username e password/token" -ForegroundColor Yellow
Write-Host ""
Write-Host "💡 Informações necessárias:" -ForegroundColor Cyan
Write-Host "   Username: srteetm00d-png" -ForegroundColor White
Write-Host "   Password: Personal Access Token (não a password normal)" -ForegroundColor White
Write-Host ""
Write-Host "   Criar token em: https://github.com/settings/tokens" -ForegroundColor Cyan
Write-Host "   Scopes necessários: repo (tudo)" -ForegroundColor Cyan
Write-Host ""

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ SUCESSO! Projeto enviado para GitHub!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📱 Próximos passos:" -ForegroundColor Cyan
    Write-Host "1. Vai a: https://github.com/srteetm00d-png/streetm00d_" -ForegroundColor White
    Write-Host "2. Settings → Pages → Source: main branch" -ForegroundColor White
    Write-Host "3. O site ficará em: https://srteetm00d-png.github.io/streetm00d_/" -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "❌ Erro ao fazer push. Verifica:" -ForegroundColor Red
    Write-Host "- Credenciais corretas (username: srteetm00d-png)" -ForegroundColor Yellow
    Write-Host "- Personal Access Token válido com permissões 'repo'" -ForegroundColor Yellow
    Write-Host "- Repositório existe e tens permissões" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "💡 Criar token: https://github.com/settings/tokens" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Pressiona qualquer tecla para sair..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

