import re
import os

INPUT_FILE = "tests/corpus/Scripts_Merged.txt"
OUTPUT_DIR = "tests/corpus/valid_tv_pass"

def split_corpus():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        
    parts = re.split(r'##-- File Name: (.*?) \| File No: \d+ \| Started --##', content)
    
    count = 0
    # Limit to 50 for environment limits
    limit = 100 
    loop_limit = min(len(parts), limit * 2) 
    
    for i in range(1, loop_limit, 2):
        fname = parts[i].strip()
        fname = os.path.basename(fname.replace('\\', '/'))
        # Ensure safe filename
        fname = re.sub(r'[^\w\.-]', '_', fname)
        
        if not fname.endswith('.pine') and not fname.endswith('.txt'):
            fname += '.pine'
        if fname.endswith('.txt'):
            fname = fname[:-4] + '.pine'
            
        code = parts[i+1].strip()
        code = re.sub(r'##-- File Name: .*? \| File No: \d+ \| Ended --##', '', code)
        
        # Remove "/* --- FILE: ... --- */" if present at start
        code = re.sub(r'/\* --- FILE: .*? --- \*/', '', code).strip()
        
        with open(os.path.join(OUTPUT_DIR, fname), 'w', encoding='utf-8') as out:
            out.write(code)
        count += 1
        
    print(f"Extracted {count} scripts.")

if __name__ == "__main__":
    split_corpus()
