import subprocess
import time
import threading
import os

# 测试配置
test_dir = "test"
test_cases = [
    # (语言名称, 命令, 是否需要编译, 编译命令)
    ("C", ["test_c.exe"], True, ["gcc", "-o", "test_c.exe", f"{test_dir}/test.c"]),
    ("C++", ["test_cpp.exe"], True, ["g++", "-o", "test_cpp.exe", f"{test_dir}/test.cpp"]),
    ("Nim", ["test_nim.exe"], True, ["nim", "c", "-o:test_nim.exe", f"{test_dir}/test.nim"]),
    ("Rust", ["test_rust.exe"], True, ["rustc", "-o", "test_rust.exe", f"{test_dir}/test.rs"]),
    ("Ant", [f"{test_dir}/antc.exe", "--file", f"{test_dir}/test.ant"], False, None),
    ("LM", [f"{test_dir}/lamina/bin/lamina.exe", f"{test_dir}/test.lm"], False, None),
    ("Syl", ["cargo", "run"], False, None)  # Syl 语言特殊处理
]

# 存储测试结果
results = {}
lock = threading.Lock()

# 运行命令并测量时间
def run_command(cmd, cwd=None):
    start_time = time.time()
    try:
        print(f"执行命令: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120, text=True)
        print(f"命令输出: {result.stdout}")
        if result.stderr:
            print(f"命令错误: {result.stderr}")
        if result.returncode != 0:
            return False, result.returncode
    except subprocess.TimeoutExpired:
        print("命令超时")
        return None, 120.0  # 超时
    except Exception as e:
        print(f"命令执行错误: {e}")
        return None, None  # 错误
    end_time = time.time()
    return True, end_time - start_time

# 测试单个语言
def test_language(lang_name, cmd, need_compile, compile_cmd):
    print(f"开始测试 {lang_name}...")
    
    # 特殊处理 Syl 语言
    if lang_name == "Syl":
        try:
            # 第一步: cargo run
            print("执行 Syl 第一步: cargo run")
            result = subprocess.run(["cargo", "run"], cwd=".", stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120, text=True)
            print(f"cargo run 输出: {result.stdout}")
            if result.stderr:
                print(f"cargo run 错误: {result.stderr}")
            
            # 第二步: gcc -o test.exe Temp.c
            print("执行 Syl 第二步: gcc -o test.exe Temp.c")
            result = subprocess.run(["gcc","-O3", "-o", "test.exe", "Temp.c"], cwd=".", stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True)
            print(f"gcc 输出: {result.stdout}")
            if result.stderr:
                print(f"gcc 错误: {result.stderr}")
            
            # 第三步: test.exe
            print("执行 Syl 第三步: test.exe")
            start_time = time.time()
            result = subprocess.run(["test.exe"], cwd=".", stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120, text=True)
            end_time = time.time()
            print(f"test.exe 输出: {result.stdout}")
            if result.stderr:
                print(f"test.exe 错误: {result.stderr}")
            
            elapsed = end_time - start_time
            with lock:
                results[lang_name] = elapsed * 1000  # 转换为毫秒
        except Exception as e:
            print(f"Syl 测试失败: {e}")
            with lock:
                results[lang_name] = f"运行错误: {str(e)}"
        finally:
            print(f"{lang_name} 测试完成")
        return
    
    # 先编译（如果需要）
    if need_compile and compile_cmd:
        try:
            print(f"编译 {lang_name}: {' '.join(compile_cmd)}")
            result = subprocess.run(compile_cmd, cwd=".", stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True)
            print(f"编译输出: {result.stdout}")
            if result.stderr:
                print(f"编译错误: {result.stderr}")
            if result.returncode != 0:
                with lock:
                    results[lang_name] = f"编译失败: {result.stderr[:100]}"
                print(f"{lang_name} 编译失败")
                return
        except Exception as e:
            print(f"{lang_name} 编译失败: {e}")
            with lock:
                results[lang_name] = f"编译错误: {str(e)}"
            return
    
    # 运行测试
    success, result = run_command(cmd, cwd=".")
    
    with lock:
        if success is None:
            if isinstance(result, float):
                results[lang_name] = "运行超时"
            else:
                results[lang_name] = f"运行错误: {str(result)}"
        elif success is False:
            results[lang_name] = f"运行失败 (返回码: {result})"
        else:
            results[lang_name] = result * 1000  # 转换为毫秒
    
    print(f"{lang_name} 测试完成")

# 主函数
def main():
    print("开始性能测试...")
    print("测试内容: 递归斐波那契函数，计算第42项")
    print("超时设置: 120秒")
    print("=" * 60)
    
    # 创建并启动线程
    threads = []
    for lang_name, cmd, need_compile, compile_cmd in test_cases:
        thread = threading.Thread(target=test_language, args=(lang_name, cmd, need_compile, compile_cmd))
        threads.append(thread)
        thread.start()
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()
    
    print("=" * 60)
    print("测试结果:")
    print("-" * 60)
    
    # 打印结果并找出最快的
    fastest_lang = None
    fastest_time = float('inf')
    
    for lang_name, time_ms in results.items():
        if isinstance(time_ms, float):
            print(f"{lang_name}: {time_ms:.2f} 毫秒")
            if time_ms < fastest_time:
                fastest_time = time_ms
                fastest_lang = lang_name
        else:
            print(f"{lang_name}: {time_ms}")
    
    print("-" * 60)
    if fastest_lang:
        print(f"最快的语言: {fastest_lang}，耗时: {fastest_time:.2f} 毫秒")
    else:
        print("无法确定最快的语言，部分测试失败")
    
    # 清理生成的可执行文件
    cleanup_files = ["test_c.exe", "test_cpp.exe", "test_nim.exe", "test_rust.exe", "test.exe"]
    for file in cleanup_files:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"已清理: {file}")
            except Exception as e:
                print(f"清理 {file} 失败: {e}")
    
    print("测试完成！")

if __name__ == "__main__":
    main()