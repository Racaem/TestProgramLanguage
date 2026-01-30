### Lamina支援執行這些指令

```bash
lamina <>          ||  start repl
lamina <path>      ||  run the file at path
lamina run <path>  ||  run the file at path
lamina version     ||  show the version of lamina
lamina repl        ||  start repl
lamina help        ||  show help
```

### 開發環境如何執行?

**第一步**
如果你是mingw gcc 套件
且編譯時未使用靜態鏈接，需將以下檔案複製到 Lamina.exe 同級目錄：

```plaintext
libgcc_s_seh-1.dll
libstdc++-6.dll
libwinpthread-1.dll
```

這些檔案位於 MinGW 的bin目錄（如C:\mingw64\bin）。

**第二步** 切換到`cmake-build-debug`目錄·

```bash[CLI.md](../zh_CN/CLI.md)
 cd .\cmake-build-debug[CLI.md](../zh_CN/CLI.md)
```

**第三步** 嘗試

『`bash
.\Lamina.exe version
```

如果有輸出，就成功了

### 加入lamina到PATH變量

如果你是**Windows**系統
執行add_path_debug.bat(需要管理員身分執行)

如果你**不**是**Windows**系統
執行add_path_debug.sh(需要管理員身分執行)
