# Script para fazer upload do STREETMOOD para nova conta GitHub
# Executa este script na pasta STREETMOOD

Write-Host "🚀 STREETMOOD - Upload para Nova Conta GitHub" -ForegroundColor Cyan
Write-Host ""

# Verificar se Git está instalado
try {
    $gitVersion = git --version
    Write-Host "✅ Git encontrado: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git não está instalado!" -ForegroundColor Red
    Write-Host "Por favor, instala Git de: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "📝 Por favor, fornece as seguintes informações:" -ForegroundColor Yellow
Write-Host ""

# Pedir informações
$novoUsername = Read-Host "Novo username GitHub"
$nomeRepositorio = Read-Host "Nome do repositório (ex: streetmood)"

if ([string]::IsNullOrWhiteSpace($novoUsername) -or [string]::IsNullOrWhiteSpace($nomeRepositorio)) {
    Write-Host "❌ Username e nome do repositório são obrigatórios!" -ForegroundColor Red
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

# Verificar se há remote antigo
$remoteExists = git remote -v 2>$null
if ($remoteExists) {
    Write-Host ""
    Write-Host "⚠️  Remote antigo encontrado:" -ForegroundColor Yellow
    git remote -v
    $remover = Read-Host "Remover remote antigo? (s/n)"
    if ($remover -eq "s" -or $remover -eq "S") {
        git remote remove origin
        Write-Host "✅ Remote antigo removido" -ForegroundColor Green
    }
}

# Adicionar novo remote
Write-Host ""
Write-Host "🔗 Adicionando novo remote..." -ForegroundColor Cyan
$remoteUrl = "https://github.com/$novoUsername/$nomeRepositorio.git"
git remote add origin $remoteUrl 2>$null
if ($LASTEXITCODE -ne 0) {
    # Se falhar, pode ser que já existe, tentar set-url
    git remote set-url origin $remoteUrl
}
Write-Host "✅ Remote configurado: $remoteUrl" -ForegroundColor Green

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
    git commit -m "Initial commit - STREETMOOD website com 350 produtos e paginação"
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
Write-Host "💡 Dica: Usa um Personal Access Token como password" -ForegroundColor Cyan
Write-Host "   Criar em: GitHub → Settings → Developer settings → Personal access tokens" -ForegroundColor Cyan
Write-Host ""

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ SUCESSO! Projeto enviado para GitHub!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📱 Próximos passos:" -ForegroundColor Cyan
    Write-Host "1. Vai a: https://github.com/$novoUsername/$nomeRepositorio" -ForegroundColor White
    Write-Host "2. Settings → Pages → Source: main branch" -ForegroundColor White
    Write-Host "3. O site ficará em: https://$novoUsername.github.io/$nomeRepositorio/" -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "❌ Erro ao fazer push. Verifica:" -ForegroundColor Red
    Write-Host "- Credenciais corretas" -ForegroundColor Yellow
    Write-Host "- Repositório criado no GitHub" -ForegroundColor Yellow
    Write-Host "- Personal Access Token válido" -ForegroundColor Yellow
}

