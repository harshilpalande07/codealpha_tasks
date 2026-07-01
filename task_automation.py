import os
import shutil
from datetime import datetime

# --- TERMINAL COLOR TUNING MATRICES ---
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RED = "\033[31m"
WHITE = "\033[37m"

def automate_universal_image_sorting(source_dir: str, destination_dir: str):
    """Scans the target lockscreen folder and automatically relocates ALL image formats."""
    print(f"\n{BOLD}{CYAN}╔═════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}         {BOLD}{MAGENTA}📂 CODEALPHA AUTOMATED FILE MANAGEMENT SYSTEM{RESET}        {BOLD}{CYAN}║{RESET}")
    print(f"{BOLD}{CYAN}╚═════════════════════════════════════════════════════════════╝{RESET}")
    
    # 1. Verification: Check if your custom lockscreen folder exists
    if not os.path.exists(source_dir):
        print(f"\n{BOLD}{RED}❌ Automation Aborted: Source path '{source_dir}' not found.{RESET}")
        print(f"{BOLD}{YELLOW}💡 Tip: Double check that your 'LOCKSCREEN' folder is spelled correctly on your Desktop!{RESET}")
        return

    # 2. Automation: Create the destination folder if it doesn't exist yet
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"\n{BOLD}{YELLOW}📁 Destination folder absent. Created path: '{destination_dir}'{RESET}")

    print(f"\n{BOLD}{YELLOW}📡 Scanning Lockscreen directory for all valid file formats...{RESET}")
    
    # 🌟 Multi-Format Tuple: Tracks every single image type you requested!
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.tiff')
    
    file_list = os.listdir(source_dir)
    moved_count = 0
    
    # 3. Automation File Processing Loops
    for filename in file_list:
        # Check if the file matches any of our format extensions
        if filename.lower().endswith(image_extensions):
            source_file_path = os.path.join(source_dir, filename)
            destination_file_path = os.path.join(destination_dir, filename)
            
            try:
                # Automate the physical move command
                shutil.move(source_file_path, destination_file_path)
                print(f"   {BOLD}{GREEN}⚡ Migrated Asset:{RESET} {WHITE}{filename:<30}{RESET} ➔ {CYAN}[Organized_Images/]{RESET}")
                moved_count += 1
            except Exception as e:
                print(f"   {BOLD}{RED}❌ Fault moving {filename}: {e}{RESET}")

    # 4. Final Verification Summary
    print(f"\n{BOLD}{CYAN}─────────────────────────────────────────────────────────────{RESET}")
    if moved_count > 0:
        print(f"{BOLD}{GREEN}🎉 [AUTOMATION SUCCESS]: {moved_count} total images (.png, .jpg, etc.) moved cleanly!{RESET}")
    else:
        print(f"{BOLD}{YELLOW}📭 Operation Complete: No matching image file signatures detected.{RESET}")
    print(f"{BOLD}{CYAN}─────────────────────────────────────────────────────────────{RESET}")

def main():
    # 🔒 Targeted system paths configured directly to your computer paths!
    source_folder = r"C:\Users\User\Desktop\LOCKSCREEN"
    destination_folder = r"C:\Users\User\Desktop\Organized_Images"
    
    automate_universal_image_sorting(source_folder, destination_folder)

if __name__ == "__main__":
    main()