### Lamina supports executing these commands

```bash
lamina <> || start repl
lamina <path> || run the file at path
lamina run <path> || run the file at path
lamina version || show the version of lamina
lamina repl || start repl
lamina help || show help
```

### How to run the development environment?

**Step 1**
If you are using the MinGW GCC suite
and did not use static linking during compilation, you need to copy the following files to the same directory as Lamina.exe:

```plaintext
libgcc_s_seh-1.dll
libstdc++-6.dll
libwinpthread-1.dll
```

These files are located in the MinGW bin directory (e.g., C:\mingw64\bin).

**Step 2** Switch to the `cmake-build-debug` directory.

```bash
cd .\cmake-build-debug
```

**Step 3** Try

```bash
.\Lamina.exe version
```

If there is output, it was successful.

### Add Lamina to the PATH variable

If you are using Windows, run add_path_debug.bat (must be run as administrator)

If you are not using Windows, run add_path_debug.sh (must be run as administrator)