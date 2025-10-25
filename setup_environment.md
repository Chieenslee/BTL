# Hướng dẫn thiết lập môi trường

## 🚀 Cách chạy ứng dụng

### **Phương pháp 1: Sử dụng file batch (Windows)**
```bash
# Chạy file run.bat
run.bat
```

### **Phương pháp 2: Chạy thủ công**

#### **Bước 1: Tạo môi trường ảo**
```bash
python -m venv venv
```

#### **Bước 2: Kích hoạt môi trường ảo**

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

#### **Bước 3: Cài đặt dependencies**
```bash
pip install -r requirements.txt
```

#### **Bước 4: Chạy ứng dụng**
```bash
python app.py
```

### **Phương pháp 3: Sử dụng file shell (Linux/Mac)**
```bash
# Cấp quyền thực thi
chmod +x run.sh

# Chạy
./run.sh
```

## 📋 Kiểm tra cài đặt

Sau khi chạy thành công, bạn sẽ thấy:
```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://[::1]:5000
```

## 🌐 Truy cập ứng dụng

Mở trình duyệt và truy cập:
- **Local**: http://localhost:5000
- **Network**: http://127.0.0.1:5000

## 🔧 Xử lý lỗi

### **Lỗi "ModuleNotFoundError: No module named 'flask'"**
```bash
# Đảm bảo môi trường ảo đã được kích hoạt
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Cài đặt lại dependencies
pip install -r requirements.txt
```

### **Lỗi port đã được sử dụng**
```bash
# Thay đổi port trong app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

### **Lỗi quyền truy cập**
```bash
# Windows: Chạy Command Prompt as Administrator
# Linux/Mac: Sử dụng sudo nếu cần
```

## 📁 Cấu trúc thư mục sau khi cài đặt

```
NCKH/
├── venv/                 # Môi trường ảo Python
├── app.py               # Ứng dụng Flask chính
├── tsp_solver.py        # Thuật toán nhánh cận
├── templates/
│   └── index.html       # Giao diện web
├── requirements.txt     # Dependencies
├── run.bat             # Script chạy Windows
├── run.sh              # Script chạy Linux/Mac
├── sample_data.csv     # Dữ liệu mẫu CSV
├── sample_data.json    # Dữ liệu mẫu JSON
└── README.md           # Hướng dẫn chi tiết
```

## 🎯 Tính năng ứng dụng

- ✅ **Giao diện web thân thiện**
- ✅ **Nhập dữ liệu thủ công**
- ✅ **Upload file CSV/JSON**
- ✅ **Dữ liệu mẫu Việt Nam**
- ✅ **Thuật toán nhánh cận tối ưu**
- ✅ **Kết quả trực quan**

## 🚀 Bắt đầu sử dụng

1. **Chạy ứng dụng** theo một trong các phương pháp trên
2. **Mở trình duyệt** và truy cập http://localhost:5000
3. **Chọn cách nhập dữ liệu**:
   - Nhập thủ công
   - Upload file CSV/JSON
   - Sử dụng dữ liệu mẫu
4. **Nhấn "Tìm lộ trình tối ưu"**
5. **Xem kết quả** với lộ trình và thống kê
