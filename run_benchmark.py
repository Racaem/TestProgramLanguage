import os
import subprocess
import time
import signal
import platform

# 获取当前目录
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)

# 超时时间（秒）
TIMEOUT_SECONDS = 300  # 5分钟

# 语言配置
LANGUAGE_CONFIGS = {
    # 特殊语言
    '.ant': {
        'command': [os.path.join(TEST_DIR, 'antc.exe'), '--file', 'test.ant'],
        'cwd': TEST_DIR
    },
    '.syl': {
        'command': ['cargo', 'run', 'test/test.syl'],
        'cwd': ROOT_DIR
    },
    
    # 其他语言
    '.c': {
        'compile': ['gcc', os.path.join(TEST_DIR, 'test.c'), '-o', os.path.join(TEST_DIR, 'test_c.exe')],
        'run': [os.path.join(TEST_DIR, 'test_c.exe')],
        'cwd': TEST_DIR
    },
    '.cpp': {
        'compile': ['g++', os.path.join(TEST_DIR, 'test.cpp'), '-o', os.path.join(TEST_DIR, 'test_cpp.exe')],
        'run': [os.path.join(TEST_DIR, 'test_cpp.exe')],
        'cwd': TEST_DIR
    },
    '.go': {
        'command': ['go', 'run', 'test.go'],
        'cwd': TEST_DIR
    },
    '.nim': {
        'compile': ['nim', 'compile', '--run', 'test.nim'],
        'cwd': TEST_DIR
    },
    '.rs': {
        'compile': ['rustc', os.path.join(TEST_DIR, 'test.rs'), '-o', os.path.join(TEST_DIR, 'test_rs.exe')],
        'run': [os.path.join(TEST_DIR, 'test_rs.exe')],
        'cwd': TEST_DIR
    },
    '.lm': {
        'command': [os.path.join(TEST_DIR, 'lamina', 'bin', 'lamina.exe'), 'test.lm'],
        'cwd': TEST_DIR
    },
}

def run_command(cmd, cwd, timeout):
    """运行命令并返回耗时（毫秒）"""
    start_time = time.time()
    try:
        if platform.system() == 'Windows':
            # Windows系统使用creationflags
            process = subprocess.Popen(
                cmd, 
                cwd=cwd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
            )
        else:
            # 非Windows系统使用preexec_fn
            process = subprocess.Popen(
                cmd, 
                cwd=cwd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid
            )
        
        stdout, stderr = process.communicate(timeout=timeout)
        elapsed = (time.time() - start_time) * 1000  # 转换为毫秒
        return elapsed, stdout.decode('utf-8', errors='replace'), stderr.decode('utf-8', errors='replace')
    except subprocess.TimeoutExpired:
        # 超时处理
        if platform.system() == 'Windows':
            process.kill()
        else:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        return None, None, "Timeout"
    except Exception as e:
        return None, None, str(e)

def main():
    print("===== 斐波那契数列计算性能测试 =====")
    print(f"测试项目: 递归计算第42个斐波那契数")
    print(f"超时时间: {TIMEOUT_SECONDS}秒")
    print("==================================")
    
    results = []
    
    # 获取test目录中的所有文件
    for filename in os.listdir(TEST_DIR):
        if os.path.isfile(os.path.join(TEST_DIR, filename)):
            ext = os.path.splitext(filename)[1].lower()
            if ext in LANGUAGE_CONFIGS:
                print(f"\n测试: {filename}")
                
                config = LANGUAGE_CONFIGS[ext]
                elapsed = None
                
                if 'command' in config:
                    # 直接运行命令
                    elapsed, stdout, stderr = run_command(config['command'], config['cwd'], TIMEOUT_SECONDS)
                elif 'compile' in config:
                    # 先编译后运行
                    if 'run' in config:
                        # 编译
                        compile_elapsed, compile_stdout, compile_stderr = run_command(
                            config['compile'], config['cwd'], TIMEOUT_SECONDS
                        )
                        if compile_elapsed is not None:
                            # 运行
                            elapsed, stdout, stderr = run_command(
                                config['run'], config['cwd'], TIMEOUT_SECONDS
                            )
                        else:
                            stderr = f"编译失败: {compile_stderr}"
                
                if elapsed is not None:
                    print(f"耗时: {elapsed:.2f}毫秒")
                    results.append((filename, elapsed))
                else:
                    print(f"状态: {stderr}")
                    results.append((filename, float('inf')))
    
    # 排序结果
    results.sort(key=lambda x: x[1])
    
    # 输出结果
    print("\n===== 测试结果 =====")
    for i, (filename, elapsed) in enumerate(results, 1):
        if elapsed == float('inf'):
            print(f"{i}. {filename}: 超时")
        else:
            print(f"{i}. {filename}: {elapsed:.2f}毫秒")
    
    # 输出最快的语言
    if results:
        fastest_file, fastest_time = results[0]
        if fastest_time != float('inf'):
            print(f"\n最快的语言: {fastest_file} ({fastest_time:.2f}毫秒)")
        else:
            print("\n所有语言都超时了")

if __name__ == "__main__":
    main()
