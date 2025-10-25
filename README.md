# Tối ưu hóa lộ trình du lịch - Thuật toán nhánh cận

Ứng dụng web sử dụng thuật toán nhánh cận (Branch and Bound) để giải quyết bài toán TSP (Traveling Salesman Problem) - tìm lộ trình ngắn nhất cho nhóm khách du lịch.

## Tính năng

- **Giao diện web thân thiện**: Nhập dữ liệu trực tiếp hoặc upload file CSV/JSON
- **Thuật toán nhánh cận**: Tìm lộ trình tối ưu với độ phức tạp được tối ưu
- **Dữ liệu mẫu**: Các thành phố Việt Nam với khoảng cách thực tế
- **Kết quả trực quan**: Hiển thị lộ trình, tổng khoảng cách và thời gian xử lý

## Cài đặt

1. **Cài đặt Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Chạy ứng dụng:**
```bash
python app.py
```

3. **Truy cập ứng dụng:**
Mở trình duyệt và truy cập: `http://localhost:5000`

## Cách sử dụng

### 1. Nhập dữ liệu thủ công
- Thêm các thành phố cần thăm
- Nhập khoảng cách giữa các thành phố
- Nhấn "Tìm lộ trình tối ưu"

### 2. Upload file
- **File CSV**: Định dạng với cột `city`, `from`, `to`, `distance`
- **File JSON**: Định dạng với `cities` và `distances` arrays

### 3. Sử dụng dữ liệu mẫu
- Nhấn tab "Dữ liệu mẫu"
- Chọn "Tải dữ liệu mẫu" để sử dụng dữ liệu các thành phố Việt Nam

## Cấu trúc dự án

```
├── app.py                 # Ứng dụng Flask chính
├── tsp_solver.py         # Thuật toán nhánh cận TSP
├── templates/
│   └── index.html        # Giao diện web
├── requirements.txt      # Dependencies Python
└── README.md            # Hướng dẫn sử dụng
```

## Thuật toán nhánh cận

### Đặc điểm:
- **Cận dưới**: Sử dụng cận dưới đơn giản để loại bỏ các nhánh không tối ưu
- **Cắt nhánh**: Dừng khám phá khi cận dưới >= chi phí tốt nhất hiện tại
- **Tìm kiếm ưu tiên**: Khám phá các nhánh có cận dưới thấp nhất trước

### Độ phức tạp:
- **Thời gian**: O(n!) trong trường hợp xấu nhất, nhưng được tối ưu đáng kể nhờ cắt nhánh
- **Không gian**: O(n²) cho ma trận kề và O(n) cho stack đệ quy

## Tối ưu hóa

### 1. Cắt nhánh sớm
- So sánh cận dưới với chi phí tốt nhất hiện tại
- Dừng khám phá nhánh nếu cận dưới >= chi phí tốt nhất

### 2. Sắp xếp ưu tiên
- Khám phá các nhánh có cận dưới thấp nhất trước
- Tăng khả năng tìm thấy lời giải tối ưu sớm

### 3. Cận dưới hiệu quả
- Sử dụng cận dưới đơn giản nhưng hiệu quả
- Tính toán nhanh để không làm chậm quá trình cắt nhánh

## Ví dụ sử dụng

### Dữ liệu mẫu (các thành phố Việt Nam):
- Hà Nội, TP. Hồ Chí Minh, Đà Nẵng, Hải Phòng, Cần Thơ, Nha Trang, Huế, Vũng Tàu
- Khoảng cách thực tế giữa các thành phố

### Kết quả:
- Lộ trình tối ưu: Hà Nội → Hải Phòng → Đà Nẵng → Nha Trang → TP. Hồ Chí Minh → Vũng Tàu → Cần Thơ → Huế → Hà Nội
- Tổng khoảng cách: ~3,500 km
- Thời gian xử lý: < 1 giây

## Mở rộng

### Các tối ưu hóa có thể thêm:
1. **Heuristic khởi tạo**: Sử dụng thuật toán tham lam để tìm lời giải ban đầu tốt
2. **Cận dưới nâng cao**: Sử dụng cận dưới Held-Karp hoặc cận dưới dựa trên cây khung nhỏ nhất
3. **Song song hóa**: Chia nhỏ không gian tìm kiếm cho nhiều luồng xử lý
4. **Cache kết quả**: Lưu trữ kết quả trung gian để tránh tính toán lại

### Tích hợp thêm:
- **Bản đồ trực quan**: Hiển thị lộ trình trên bản đồ
- **Xuất kết quả**: Lưu kết quả ra file PDF hoặc Excel
- **So sánh thuật toán**: So sánh với các thuật toán khác (GA, SA, ACO)

## Tác giả

Dự án bài tập lớnlớn - Tối ưu hóa lộ trình du lịch sử dụng thuật toán nhánh cận.
