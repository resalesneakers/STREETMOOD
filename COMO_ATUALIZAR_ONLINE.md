# 🚀 Como Atualizar o Site Online

## ✅ Commit Criado com Sucesso!

As alterações foram preparadas para upload.

## 📤 Fazer Push para GitHub

### Opção 1: Via GitHub Desktop (Mais Fácil)

1. Abre o **GitHub Desktop**
2. Deves ver o commit que acabámos de criar
3. Clica no botão **"Push origin"** (no topo)
4. Aguarda alguns segundos...

### Opção 2: Via PowerShell (Comando)

Se preferires usar comandos, executa:
```powershell
$gitPath = (Get-ChildItem "$env:LOCALAPPDATA\GitHubDesktop\app-*\resources\app\git\cmd\git.exe" | Sort-Object LastWriteTime -Descending | Select-Object -First 1).FullName
& $gitPath push origin main
```

## 🌐 Verificar GitHub Pages

Depois do push:

1. Vai ao teu repositório: **https://github.com/resalesneakers/STREETMOOD**
2. Verifica que os ficheiros foram atualizados
3. O GitHub Pages atualiza automaticamente em **1-2 minutos**

## 🔗 Link do Site

O teu site estará disponível em:
```
https://resalesneakers.github.io/STREETMOOD/
```

## 📋 O que foi atualizado:

- ✅ `all_products_output.js` - 439 produtos processados
- ✅ `scripts/main.js` - Removido 3D, atualizado mensagens
- ✅ `index.html` - Textos atualizados
- ✅ `process_ubzy_csv.py` - Script de processamento

## 🔄 Para Atualizar no Futuro:

1. Faz alterações nos ficheiros
2. Executa:
   ```powershell
   $gitPath = (Get-ChildItem "$env:LOCALAPPDATA\GitHubDesktop\app-*\resources\app\git\cmd\git.exe" | Sort-Object LastWriteTime -Descending | Select-Object -First 1).FullName
   & $gitPath add .
   & $gitPath commit -m "Descrição das alterações"
   & $gitPath push origin main
   ```
3. Aguarda 1-2 minutos
4. O site atualiza automaticamente!

## ✨ Pronto!

O site está atualizado e online! 🎉

