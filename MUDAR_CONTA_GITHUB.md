# 📦 Guia: Mudar para Nova Conta GitHub

## Passo 1: Criar Novo Repositório no GitHub

1. Acede à tua **nova conta GitHub**
2. Clica em **"New repository"** (ou **"+"** → **"New repository"**)
3. Dá um nome ao repositório (ex: `streetmood` ou `streetmood-website`)
4. **NÃO** inicializes com README, .gitignore ou licença
5. Clica em **"Create repository"**

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

## Passo 4: Ligar à Nova Conta GitHub

```powershell
# Adicionar remote da nova conta (substitui USERNAME pelo teu novo username)
git remote add origin https://github.com/USERNAME/NOME_DO_REPOSITORIO.git

# Verificar se está correto
git remote -v
```

## Passo 5: Fazer Push para GitHub

```powershell
# Mudar para branch main (se necessário)
git branch -M main

# Fazer push para GitHub
git push -u origin main
```

**Nota:** Se pedir credenciais:
- Username: teu novo username GitHub
- Password: usa um **Personal Access Token** (não a password normal)

### Como criar Personal Access Token:

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Clica "Generate new token (classic)"
3. Dá um nome (ex: "STREETMOOD")
4. Seleciona scopes: `repo` (tudo)
5. Clica "Generate token"
6. **Copia o token** (só aparece uma vez!)
7. Usa esse token como password

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
git remote add origin https://github.com/NOVO_USERNAME/NOME_DO_REPOSITORIO.git

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

1. Vai a **Settings** do repositório
2. **Pages** → **Source**: seleciona `main` branch
3. Clica **Save**
4. O site ficará disponível em: `https://NOVO_USERNAME.github.io/NOME_DO_REPOSITORIO/`

## 💡 Dica Rápida

Se preferires usar GitHub Desktop:
1. Instala GitHub Desktop
2. File → Add Local Repository
3. Seleciona a pasta `STREETMOOD`
4. Publish repository → escolhe a nova conta
5. Clica "Publish repository"

