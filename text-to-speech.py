import os
import sys
import subprocess


# =========================================================
# CẤU HÌNH
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(BASE_DIR, ".venv")
VENV_PYTHON = os.path.join(VENV_DIR, "Scripts", "python.exe")


# =========================================================
# TỰ ĐỘNG CHẠY BẰNG PYTHON TRONG .venv
# =========================================================

def run_in_venv():
    current_python = os.path.abspath(sys.executable)

    # Nếu chưa chạy bằng Python trong .venv
    if os.path.abspath(current_python) != os.path.abspath(VENV_PYTHON):

        if not os.path.exists(VENV_PYTHON):
            print("❌ Không tìm thấy Python trong .venv!")
            print()
            print("Hãy tạo môi trường bằng:")
            print()
            print(f'"{sys.executable}" -m venv .venv')
            input("\nNhấn Enter để thoát...")
            sys.exit(1)

        print("🔄 Đang chuyển sang môi trường .venv...")
        print()

        # Chạy lại chính file này bằng Python của .venv
        result = subprocess.run(
            [VENV_PYTHON, os.path.abspath(__file__)],
            cwd=BASE_DIR
        )

        sys.exit(result.returncode)


# =========================================================
# CHẠY TRONG .VENV
# =========================================================

run_in_venv()


# =========================================================
# IMPORT gTTS
# =========================================================

try:
    from gtts import gTTS

except ModuleNotFoundError:
    print("❌ Chưa cài gTTS trong .venv!")
    print()
    print("Đang tự động cài gTTS...")
    print()

    subprocess.check_call([
        VENV_PYTHON,
        "-m",
        "pip",
        "install",
        "gTTS"
    ])

    from gtts import gTTS


# =========================================================
# THÔNG TIN
# =========================================================

print("=" * 60)
print("          TEXT TO SPEECH - gTTS")
print("=" * 60)

print()
print(f"📂 Thư mục project:")
print(f"   {BASE_DIR}")

print()
print(f"🐍 Python:")
print(f"   {sys.executable}")

print()


# =========================================================
# CHỌN NGÔN NGỮ
# =========================================================

print("Chọn ngôn ngữ:")
print()
print("  1. 🇻🇳 Tiếng Việt")
print("  2. 🇬🇧 Tiếng Anh")
print("  3. 🇨🇳 Tiếng Trung")
print()

while True:
    choice = input("👉 Nhập lựa chọn (1/2/3): ").strip()

    if choice == "1":
        language = "vi"
        language_name = "Tiếng Việt"
        break

    elif choice == "2":
        language = "en"
        language_name = "Tiếng Anh"
        break

    elif choice == "3":
        language = "zh-CN"
        language_name = "Tiếng Trung"
        break

    else:
        print("❌ Lựa chọn không hợp lệ! Hãy nhập 1, 2 hoặc 3.")


# =========================================================
# NHẬP NỘI DUNG
# =========================================================

print()
print(f"🌐 Ngôn ngữ: {language_name}")
print()

print("Nhập nội dung cần chuyển thành giọng nói.")
print("Bạn có thể nhập nhiều dòng.")
print("Nhấn Enter 2 lần để kết thúc.")
print()

lines = []

while True:
    line = input()

    if line == "":
        break

    lines.append(line)

text = "\n".join(lines).strip()


if not text:
    print()
    print("❌ Bạn chưa nhập nội dung!")
    input("\nNhấn Enter để thoát...")
    sys.exit(1)


# =========================================================
# TÊN FILE
# =========================================================

print()
filename = input(
    "💾 Tên file audio (Enter = output.mp3): "
).strip()

if not filename:
    filename = "output.mp3"

if not filename.lower().endswith(".mp3"):
    filename += ".mp3"


# =========================================================
# ĐƯỜNG DẪN LƯU FILE
# =========================================================

output_path = os.path.join(BASE_DIR, filename)


# =========================================================
# TẠO AUDIO
# =========================================================

print()
print("=" * 60)
print("⏳ Đang chuyển văn bản thành giọng nói...")
print("=" * 60)

try:

    tts = gTTS(
        text=text,
        lang=language,
        slow=False
    )

    tts.save(output_path)

    print()
    print("✅ HOÀN TẤT!")
    print()
    print(f"🌐 Ngôn ngữ : {language_name}")
    print(f"🎵 File      : {filename}")
    print(f"📁 Vị trí    : {output_path}")
    print()

except Exception as e:

    print()
    print("❌ Có lỗi xảy ra!")
    print()
    print(str(e))
    print()

    print("💡 Kiểm tra:")
    print("   - Máy có kết nối Internet không?")
    print("   - Nội dung có hợp lệ không?")
    print()


input("Nhấn Enter để thoát...")