header_template = """
TEST_API int func_{x}(int& val);
int func_in_{x}(int& val);
"""

def_template = """
int func_{x}(int& val) {{
    func_in_{x}(val);
    const int x = {x};
    std::cout << {x};
    for (int i = 0; i < {x}; i++)
    {{
        val += 1;
    }}

    int b = (x | x << 1) * 45;
    val += b;
    val += add(x << 1, x >> 1);
    val += mul(x >> 1, x >> 2);

    return val;
}}
int func_in_{x}(int& val) {{
    const int x = {x};
    std::cout << {x};
    for (int i = 0; i < {x}; i++)
    {{
        val += 1;
    }}

    int b = (x | x << 1) * 45;
    val += b;
    val += add(x << 1, x >> 1);
    val += mul(x >> 1, x >> 2);

    return val;
}}
"""

app_header_template = """
int compute(int& val);
"""

app_def_template = """
    func_{x}(val);
"""

COUNT = 40000
SPLIT = 10

with open("lib.h", "w") as f: 
    f.write("#pragma once\n") 
    f.write('#include "util.h"\n') 

    for i in range(0,COUNT):
        f.write(header_template.format(x=i))


for k in range(0, SPLIT):
    with open("lib{}.cpp".format(k), "w") as f: 
        f.write('#include "lib.h"\n') 
        f.write('#include <iostream>') 
        
        count = int(COUNT / SPLIT)
        for i in range(k * count, (k + 1)* count):
            f.write(def_template.format(x=i))

with open("app.h", "w") as f: 
    f.write("#pragma once\n") 
    f.write('#include "lib.h"\n') 

    f.write(app_header_template.format(x=i))


    
with open("app.cpp", "w") as f: 
    f.write('#include "app.h"\n') 
    
    f.write('int compute(int& val) {')
    for i in range(0,COUNT):
        f.write(app_def_template.format(x=i))

    f.write('return val;}')