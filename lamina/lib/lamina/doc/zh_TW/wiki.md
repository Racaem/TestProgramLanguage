# Lamina 語言 Wiki

## 優點
1.  **精確數學計算**：從底層解決浮點數精度遺失問題，支援有理數（分數）和無理數（√、π、e）的符號化儲存與運算，多次迴圈運算仍保持精確。
2.  **語法簡潔直觀**：支援自動補充分號、省略 if/while 語句的圓括號、無參函式簡寫等，降低程式碼冗餘，符合數學表達習慣。
3.  **原生數學友善**：無需第三方函式庫，直接支援向量、矩陣運算、大整數階乘等數學操作，滿足複雜數學問題需求。
4.  **友善開發體驗**：互動式 REPL 支援關鍵字高亮、自動補齊，提供完整錯誤堆疊追蹤，便於偵錯；智慧終端自動適應色彩，避免亂碼。
5.  **模組化設計**：透過 `include` 語句引入外部模組，支援 `::` 命名空間存取符，實現程式碼複用與隔離。
6.  **靈活資料型別**：涵蓋精確數值型別（rational/irrational）、複合型別（陣列/矩陣/結構體）及匿名函式，適應多樣開發場景。


## 基本語法
### 1. 變數宣告
**範本**：
```lamina
// 普通變數宣告
var var_name = expression;
// 大整數變數宣告（任意精度）
bigint big_var_name = expression;
```
**範例**：
```lamina
var pi = 3.1415; // 宣告浮點數變數pi
var score = 95; // 宣告整數變數score
var half = 1/2; // 宣告有理數變數half（自動以分數形式儲存）
bigint fact_25 = 25!; // 宣告大整數變數，儲存25的階乘
```

### 2. 註解
**範本**：
```lamina
// 單行註解：註解內容
/*
   區塊註解：
   支援多行文字
   適合長註解說明
*/
```
**範例**：```lamina
// 這是單行註解，用於說明下一行程式碼功能
var radius = 5; // 宣告圓的半徑變數

/*
區塊註解範例：
以下程式碼計算圓的面積
依賴pi()函式獲取精確圓周率
*/
var area = pi() * radius ^ 2;
```

### 3. 條件語句（if-else）
**範本**：
```lamina
if condition {
    // 條件為true時執行的程式碼
} else {
    // 條件為false時執行的程式碼
}
```
**範例**：
```lamina
var num = 8;
if num > 0 {
    print("num是正數"); // 條件成立，輸出此內容
} else {
    print("num是非正數");
}
```

### 4. 迴圈語句
#### （1）while迴圈
**範本**：
```lamina
while condition {
    // 條件為true時重複執行的程式碼
}
```
**範例**：
```lamina
var count = 1;
while count <= 3 {
    print("當前計數：", count); // 依序輸出1、2、3
    count = count + 1;
}
```

#### （2）loop迴圈（無限迴圈）
**範本**：
```lamina
loop {
    // 無限重複執行的程式碼
    if stop_condition {
        break; // 滿足終止條件時退出迴圈
    }
}
```
**範例**：
```lamina
var i = 1;
loop {
    print("迴圈次數：", i);
    if i >= 2 {
        break; // 執行2次後退出
    }
    i = i + 1;
}
```

### 5. 函式定義
#### （1）無參函式
**範本**：
```lamina
func func_name {
    // 函式主體程式碼
    return return_value; // 可選，無回傳值可省略
}
```
**範例**：
```lamina
func say_hello {
    print("Hello, Lamina!"); // 無回傳值，直接輸出
}
say_hello(); // 呼叫函式，輸出"Hello, Lamina!"
```

#### （2）有參函式
**範本**：
```lamina
func func_name(param1, param2) {
    // 基於參數的邏輯程式碼
    return result; // 回傳計算結果
}
```
**範例**：
```lamina
func add(a, b) {
    return a + b; // 回傳a與b的和
}
var sum = add(3, 5); // 呼叫函式，sum = 8
print("3 + 5 =", sum);
```

### 6. 匿名函式
**範本**：
```lamina
var func_var = do |param1, param2| {
    // 函式主體程式碼
    return result;
};

// 只有單一運算式時可以簡寫
var simple_func = |param1, param2| expression;
```
**範例**：
```lamina
var multiply = do |x, y| {
    return x * y; // 匿名函式實現乘法
};
var product = multiply(4, 6); // 呼叫匿名函式，product = 24
print("4 * 6 =", product);

var add = |a,b| a+b;
var result = add(1,33)
print("1 + 33 =", result)
```

### 7. 結構體宣告
**範本**：
```lamina
var struct_name = {
    key1 = value1;
    key2 = value2;
    // 更多鍵值對...
};
```
**範例**：
```lamina
var student = {
    name = "Tom";
    age = 15;
    scores = [90, 85, 92]; // 結構體巢狀陣列
};
```

### 8. 結構體成員存取
**範本**：
```lamina
struct_name.key; // 存取結構體的指定成員
```
**範例**：
```lamina
var student = { name = "Tom"; age = 15; };
print("學生姓名：", student.name); // 輸出"學生姓名：Tom"
print("學生年齡：", student.age); // 輸出"學生年齡：15"
student.age = 16
```

### 9. 模組引入
**範本**：
```lamina
include "module_path"; // 引入指定路徑的模組，自動補全.lm副檔名
```
**範例**：
```lamina
include "math_utils"; // 引入數學工具模組
include "lib/vectors"; // 引入向量計算模組（相對路徑）
var root = math::sqrt(2); // 透過命名空間存取模組函式
```

### 10. 續行符
**範本**：
```lamina
var long_expression = expression1 + expression2 + \
                      expression3 + expression4; // \ 用於拆分長運算式
```
**範例**：
```lamina
var total = 10 + 20 + 30 + \
            40 + 50; // 等價於var total = 10+20+30+40+50;
print("總和：", total); // 輸出"總和：150"
```


## 基本型別
1.  **int**：普通整數型別，支援正負整數的算術運算，無需顯式宣告型別。
    範例：
    ```lamina
    var a = 42; // 正整數
    var b = -10; // 負整數
    var c = a + b; // c = 32（int型別）
    ```

2.  **float**：浮點數型別，用於相容傳統浮點運算場景，存在精度限制。
    範例：
    ```lamina
    var pi_approx = 3.14; // 浮點數
    var temp = -0.5; // 負浮點數
    ```

3.  **rational**：精確有理數型別，自動以分數形式儲存除法結果，避免精度遺失，支援自動化簡。
    範例：
    ```lamina
    var frac1 = 16/9; // 儲存為16/9，非1.777...
    var frac2 = 4/6; // 自動化簡為2/3
    var sum_frac = frac1 + frac2; // 精確計算，結果為34/9
    ```

4.  **irrational**：精確無理數型別，以符號形式儲存（如√、π、e），支援符號化運算與化簡。
    範例：
    ```lamina
    var root2 = sqrt(2); // 儲存為√2
    var root8 = sqrt(8); // 自動化簡為2√2
    var pi_val = pi(); // 儲存為π
    var product = root2 * root2; // 結果為2（int型別）
    ```

5.  **bool**：布林型別，僅包含 `true`（真）和 `false`（假）兩個值，用於條件判斷。
    範例：
    ```lamina
    var is_pass = true;
    var is_empty = false;
    if is_pass {
        print("考試通過");
    }
    ```

6.  **string**：字串型別，用雙引號包裹文本內容，支援字串相關函式操作。
    範例：
    ```lamina
    var greeting = "Hello, Lamina!";
    var name = "Alice";
    ```

7.  **null**：空值型別，僅表示 `null` 一個值，用於表示變數未賦值或無回傳值。
    範例：
    ```lamina
    var empty_var = null;
    func no_return() {
        print("無回傳值");
        return null; // 顯式回傳空值
    }
    ```

8.  **bigint**：任意精度大整數型別，需顯式宣告，支援超大整數（如階乘、大數值運算）。
    範例：
    ```lamina
    bigint large_num = 999999999999999; // 超大整數
    bigint fact_30 = 30!; // 30的階乘（大整數結果）
    ```

9.  **array**：陣列型別，用方括號包裹元素，支援索引存取和陣列相關函式。
    範例：
    ```lamina
    var scores = [90, 85, 92]; // 一維陣列
    var names = ["Tom", "Alice", "Bob"]; // 字串陣列
    ```

10. **matrix**：矩陣型別，用巢狀陣列表示（二維陣列），支援矩陣行列式、乘法等運算。
    範例：
    ```lamina
    var mat2x2 = [[1, 2], [3, 4]]; // 2x2矩陣
    var mat3x1 = [[1], [2], [3]]; // 3x1列矩陣
    ```

11. **struct**：結構體型別，用大括號包裹鍵值對，支援自訂成員和成員存取。
    範例：
    ```lamina
    var person = {
        name = "Bob";
        age = 20;
        is_student = true;
    };
    ```

12. **lambda**：匿名函式型別，用於表示未命名的函式，可賦值給變數或作為參數傳遞。
    範例：
    ```lamina
    var subtract = |a, b| a - b ; // lambda型別變數
    ```

13. **module**：模組型別，透過 `include` 引入，包含模組內定義的函式、變數，支援 `::` 命名空間存取。
    範例：
    ```lamina
    include random; // 引入模組，module型別
    var result = random::random(); // 存取模組函式
    ```


## 函式庫
### 1. 數學函式
-   **平方根函式**：用於計算數值的精確平方根，若為完全平方數回傳int，否則回傳irrational。
    ```lamina
    sqrt(x) -> int/irrational
    ```
-   **圓周率函式**：回傳精確的圓周率符號π，型別為irrational。
    ```lamina
    pi() -> irrational
    ```
-   **自然常數函式**：回傳精確的自然常數符號e，型別為irrational。
    ```lamina
    e() -> irrational
    ```-   **正弦函式**：計算角度的正弦值，支援精確數值輸入，回傳對應精度結果。
    ```lamina
    sin(x) -> rational/irrational/float
    ```
-   **餘弦函式**：計算角度的餘弦值，支援精確數值輸入，回傳對應精度結果。
    ```lamina
    cos(x) -> rational/irrational/float
    ```
-   **絕對值函式**：回傳輸入數值的絕對值，保持原類型不變。
    ```lamina
    abs(x) -> int/float/rational/irrational
    ```
-   **自然對數函式**：計算數值的自然對數（以e為底），回傳對應精度結果。
    ```lamina
    log(x) -> rational/irrational/float
    ```
-   **階乘函式**：計算非負整數的階乘，支援int和bigint型別輸入，回傳對應整數型別。
    ```lamina
    factorial(n) -> int/bigint
    ```

### 2. 向量/矩陣函式
-   **向量點積函式**：計算兩個同維度向量的點積，回傳數值型別（int/rational等）。
    ```lamina
    dot(v1: array, v2: array) -> int/rational/float
    ```
-   **向量叉積函式**：計算兩個三維向量的叉積，回傳新的三維陣列（矩陣）。
    ```lamina
    cross(v1: array, v2: array) -> array
    ```
-   **向量模長函式**：計算向量的模長（長度），回傳精確數值型別（irrational/rational等）。
    ```lamina
    norm(v: array) -> rational/irrational/float
    ```
-   **矩陣行列式函式**：計算二維方陣的行列式，回傳數值型別（int/rational等）。
    ```lamina
    det(mat: array) -> int/rational/float
    ```

### 3. 工具函式
-   **列印函式**：向控制台輸出一個或多個內容，結尾自動換行，無回傳值。
    ```lamina
    print(...) -> null
    ```
-   **輸入函式**：在控制台顯示提示文本，獲取使用者輸入內容，回傳字串型別。
    ```lamina
    input(prompt: string) -> string/float
    ```
-   **小數轉分數函式**：將浮點數轉換為精確的有理數（分數），自動化簡。
    ```lamina
    fraction(x: float) -> rational
    ```
-   **分數轉小數函式**：將有理數（分數）轉換為浮點數，支援按需保留精度。
    ```lamina
    decimal(x: rational) -> float
    ```
-   **型別獲取函式**：回傳變數的型別名稱，以字串形式表示。
    ```lamina
    typeof(x) -> string
    ```
-   **深層複製函式**：對結構體、陣列、匿名函式、模組等複合型別進行深層複製，修改複本不影響原物件。
    ```lamina
    copy(x) -> any
    ```
-   **大小獲取函式**：回傳陣列的長度或結構體的成員數量，回傳int型別。
    ```lamina
    size(x: array/struct) -> int
    ```
-   **斷言函式**：判斷條件是否為true，若為false則拋出錯誤並顯示自訂訊息。
    ```lamina
    assert(condition: bool, msg: string = "") -> null
    ```

### 4. 陣列函式
-   **陣列遍歷函式**：遍歷陣列的每個元素，對元素執行指定函式，無回傳值。
    ```lamina
    foreach(arr: array, func: lambda) -> null
    ```
-   **陣列映射函式**：遍歷陣列的每個元素，用指定函式處理元素，回傳新的陣列。
    ```lamina
    map(arr: array, func: lambda) -> array
    ```
-   **陣列尋找函式**：在陣列中尋找首個滿足條件的元素，回傳元素值或null。
    ```lamina
    find(arr: array, func: lambda) -> any/null
    ```
-   **陣列取代函式**：取代陣列中滿足條件的元素，回傳null。
    ```lamina
    replace(arr: array, func: lambda, new_val) -> null
    ```

### 5. 字串函式
-   **字串串接函式**：串接多個字串，回傳串接後的新字串。
    ```lamina
    string::cat(...) -> string
    ```
-   **字元獲取函式**：獲取指定索引的字元
    ```lamina
    string::at(index: int) -> int
    ```
-   **子字串截取函式**：從指定索引開始，截取指定長度的子字串，回傳新字串。
    ```lamina
    string::sub(str: string, start_index: int, len: int) -> string
    ```### 6. 隨機函式
-   **隨機浮點數函式**：回傳0（含）到1（不含）之間的隨機浮點數。
    ```lamina
    random::random() -> float
    ```
-   **隨機整數函式**：回傳 `[start, end]` 範圍內的隨機整數（包含邊界值）。
    ```lamina
    random::randint(start: int, end: int) -> int
    ```
-   **隨機字串函式**：從輸入字串中隨機選取一個字元，回傳該字元（string型別）。
    ```lamina
    random::randstr(chars: string) -> string
    ```

### 7. 時間函式
-   **時間獲取函式**：回傳當前系統時間，格式為"HH:MM:SS"，字串型別。
    ```lamina
    time::time() -> string
    ```
-   **日期獲取函式**：回傳當前系統日期，格式為"YYYY-MM-DD"，字串型別。
    ```lamina
    time::date() -> string
    ```
-   **日期格式化函式**：將日期字串按指定格式轉換，回傳格式化後的日期字串。
    ```lamina
    time::format_date(date: string, format: string = "YYYY-MM-DD") -> string
    ```

### 8. CAS相關函式
-   **CAS解析函式**：解析數學運算式，將其轉換為CAS可處理的內部格式，回傳解析後的CAS物件。
    ```lamina
    cas::parse(expr: string) -> cas_object
    ```
-   **CAS簡化函式**：對CAS物件表示的數學運算式進行簡化，回傳簡化後的CAS物件。
    ```lamina
    cas::simplify(cas_obj: cas_object) -> cas_object
    ```
-   **CAS求導函式**：對CAS物件表示的函式求導，回傳求導後的CAS物件。
    ```lamina
    cas::differentiate(cas_obj: cas_object, var: string) -> cas_object
    ```
-   **CAS計算函式**：對CAS物件表示的運算式進行數值或符號計算，回傳計算結果（CAS物件或基礎資料型別）。
    ```lamina
    cas::evaluate(cas_obj: cas_object) -> any
    ```
-   **CAS儲存函式**：將指定名稱與CAS物件關聯並儲存，便於後續呼叫，無回傳值或回傳儲存成功標識（布林型別）。
    ```lamina
    cas::store(name: string, cas_obj: cas_object) -> bool/void
    ```
-   **CAS載入函式**：根據指定名稱載入已儲存的CAS物件，回傳對應的CAS物件（若不存在則回傳空）。
    ```lamina
    cas::load(name: string) -> cas_object/null
    ```
-   **CAS定點計算函式**：在指定變數值處計算CAS物件表示的運算式，回傳計算結果（數值型別）。
    ```lamina
    cas::evaluate_at(cas_obj: cas_object, var: string, value: number) -> number
    ```
-   **CAS線性求解函式**：求解線性方程式或線性方程組（需以CAS物件形式傳入），回傳方程式的解（CAS物件或解的集合）。
    ```lamina
    cas::solve_linear(cas_obj: cas_object) -> cas_object/array
    ```
-   **CAS數值求導函式**：透過數值方法對函式（CAS物件表示）求導，回傳數值導數結果（數值型別）。
    ```lamina
    cas::numerical_derivative(cas_obj: cas_object, var: string, value: number) -> number
    ```


### 9.IO函式
1.  **讀取檔案**：根據指定路徑和匹配模式讀取檔案內容，回傳讀取到的字串資料。
```lamina
fast_io::read(path, pattern) -> string
```
2.  **寫入檔案**：向指定路徑的檔案中寫入內容（註：需確保函式實際包含內容參數，此處按標準邏輯補充），回傳寫入成功與否的布林值。
```lamina
fast_io::write(path) -> bool
```
3.  **建立檔案**：在指定路徑建立新檔案，並寫入初始內容，回傳建立成功與否的布林值。
```lamina
fast_io::create(path, init_conten) -> bool
```

### 10. 程式控制函式
-   **程式退出函式**：終止當前程式運行，可指定退出碼（0表示正常退出，非0表示異常）。
    ```lamina
    exit(code: int = 0) -> null
    ```
-   **型別轉換函式**：將任意型別的變數轉換為字串型別，回傳轉換後的字串。
    ```lamina
    to_string(x) -> string
    ```
-   **系統執行函式**：執行系統指令
```
system(cmd: string) -> null
```

### 11. 變數與函式查詢函式
-   **所有作用域變數查詢函式**：回傳當前所有全域變數的名稱列表，陣列型別。
    ```lamina
    vars() -> array
    ```
-   **局部變數查詢函式**：回傳當前作用域內所有局部變數的名稱列表，結構體型別。
    ```lamina
    locals() -> struct
    ```
-   **全域變數查詢函式**：回傳全域作用域變數的名稱列表，結構體型別。
    ```lamina
    locals() -> struct
    ```