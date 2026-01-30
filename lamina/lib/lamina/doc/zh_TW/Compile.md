## 編譯方法

<div align="right">
 <strong>繁體中文</strong> | <a href="../zh_CN/Compile.md">簡體中文</a> | <a href="../en_US/Compile.md">English</a>
</div>
<br>

Linux 平台:

```shell
mkdir build
cd build
cmake ..
make
```

Windows 平台（使用MinGW）:

```shell
mkdir build
cd build
cmake .. -G "MinGW Makefiles"
mingw32-make
```

Windows 平台（使用msbuild(i.e. Visual Studio)）

```shell
mkdir build
cd build
cmake .. -G "Visual Studio 17 2022"
msbuild ALL_BUILD.vcxproj
```

使用 xmake 建置:

```shell
xmake
```

# 警告：如果在MacOS下使用cmake無法構建，請嘗試使用Unix Makefiles而不是Xcode