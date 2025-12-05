import os
import glob
import subprocess
import json
from dataclasses import dataclass
from typing import List

@dataclass
class TestResult:
    filename: str
    exit_code: int
    errors: int
    warnings: int
    output: str

def run_harness(directory):
    files = glob.glob(os.path.join(directory, "*.pine"))
    results = []
    
    print(f"Running harness on {len(files)} files in {directory}...")
    
    for fpath in files:
        # Run pinelint via module
        cmd = ["python3", "-m", "pinelint.cli", "check", fpath, "--format", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        try:
            data = json.loads(result.stdout)
            err_count = data.get("error_count", 0)
            warn_count = data.get("warning_count", 0)
        except json.JSONDecodeError:
            err_count = -1
            warn_count = -1
            
        results.append(TestResult(
            filename=os.path.basename(fpath),
            exit_code=result.returncode,
            errors=err_count,
            warnings=warn_count,
            output=result.stdout
        ))
        
    # Analyze
    total = len(results)
    if total == 0:
        print("No files found.")
        return

    passed = sum(1 for r in results if r.exit_code == 0)
    failed = total - passed
    
    print(f"\nBaseline Results:")
    print(f"Total: {total}")
    print(f"Passed (Exit 0): {passed}")
    print(f"Failed (Exit 1): {failed}")
    print(f"Success Rate: {passed/total*100:.1f}%")
    
    # List sample failures (first 10)
    print("\nSample Failures:")
    count = 0
    for r in results:
        if r.exit_code != 0:
            print(f"{r.filename}: Errors={r.errors}")
            count += 1
            if count >= 10: break

import sys

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "tests/corpus/valid_tv_pass"
    run_harness(path)
