# 📦 Guia: Upload STREETMOOD para GitHub

## 🎯 Repositório de Destino

**URL:** https://github.com/srteetm00d-png/streetm00d_

## ⚡ Método Rápido (Recomendado)

1. Abre PowerShell na pasta `STREETMOOD`
2. Executa:
   ```powershell
   .\upload-para-github.ps1
   ```
3. Segue as instruções no ecrã

## 📋 Método Manual (Passo a Passo)

### Passo 1: Verificar se o Repositório Existe

O repositório já existe em: https://github.com/srteetm00d-png/streetm00d_

Se não tiveres acesso, certifica-te que:
- Estás logado na conta `srteetm00d-png`
- Tens permissões de escrita no repositório

## Passo 2: Instalar Git (se necessário)

Se o Git não estiver instalado:

1. Descarrega Git: https://git-scm.com/download/win
2. Instala seguindo o assistente
3. Reinicia o terminal/PowerShell

## Passo 3: Inicializar Git no Projeto

Abre PowerShell na pasta `C:\Users\User\Desktop\STREETMOOD` e executa:

```powershell
# Inicializar repositório Git
git init

# Adicionar todos os ficheiros
git add .

# Fazer primeiro commit
git commit -m "Initial commit - STREETMOOD website com 350 produtos"
```

## Passo 4: Ligar ao Repositório GitHub

```powershell
# Adicionar remote (ou atualizar se já existir)
git remote add origin https://github.com/srteetm00d-png/streetm00d_.git

# Se já existe remote, atualizar:
git remote set-url origin https://github.com/srteetm00d-png/streetm00d_.git

# Verificar se está correto
git remote -v
```

**Deve mostrar:**
```
origin  https://github.com/srteetm00d-png/streetm00d_.git (fetch)
origin  https://github.com/srteetm00d-png/streetm00d_.git (push)
```

## Passo 5: Fazer Push para GitHub

```powershell
# Mudar para branch main (se necessário)
git branch -M main

# Fazer push para GitHub
git push -u origin main
```

**Nota:** Se pedir credenciais:
- **Username:** `srteetm00d-png`
- **Password:** usa um **Personal Access Token** (não a password normal)

### Como criar Personal Access Token:

1. Vai a: https://github.com/settings/tokens
2. Clica **"Generate new token (classic)"**
3. Dá um nome (ex: "STREETMOOD")
4. Seleciona scopes: **`repo`** (marca tudo em repo)
5. Clica **"Generate token"**
6. **Copia o token** (só aparece uma vez! Guarda-o bem)
7. Usa esse token como password quando fizeres push

## Passo 6: Verificar

1. Vai ao teu novo repositório no GitHub
2. Verifica se todos os ficheiros aparecem
3. Abre `index.html` para ver se está tudo correto

## 🔄 Se já tens um repositório Git antigo

Se já tens um repositório Git ligado à conta antiga:

```powershell
# Remover remote antigo
git remote remove origin

# Adicionar novo remote
git remote add origin https://github.com/srteetm00d-png/streetm00d_.git

# Verificar
git remote -v

# Fazer push
git push -u origin main
```

## 📝 Ficheiros Importantes a Incluir

Certifica-te que estes ficheiros estão incluídos:
- ✅ `index.html` (página principal)
- ✅ `streetmood_products.js` (350 produtos)
- ✅ `scripts/main.js` (se ainda for usado)
- ✅ `style.css` (se ainda for usado)
- ✅ `imagens_produtos/` (pasta com todas as imagens)
- ✅ `streetmood_images_mapping.json` (se existir)

## ⚠️ Ficheiros a NÃO Incluir (já no .gitignore)

- ❌ `node_modules/`
- ❌ `.env`
- ❌ Ficheiros temporários

## 🚀 Depois do Upload

1. Vai a: https://github.com/srteetm00d-png/streetm00d_/settings/pages
2. **Source**: seleciona `main` branch
3. **Folder**: `/ (root)`
4. Clica **Save**
5. O site ficará disponível em: **https://srteetm00d-png.github.io/streetm00d_/**

## 💡 Dica Rápida

Se preferires usar GitHub Desktop:
1. Instala GitHub Desktop
2. File → Add Local Repository
3. Seleciona a pasta `STREETMOOD`
4. Publish repository → escolhe a nova conta
5. Clica "Publish repository"

