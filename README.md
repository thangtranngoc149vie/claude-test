# PostgreSQL Table List Exporter

Chương trình Python để kết nối PostgreSQL và xuất danh sách bảng ra file text.

## Yêu cầu

- Python 3.6+
- PostgreSQL database

## Cài đặt

1. Clone repository này:
```bash
git clone <repository-url>
cd claude-test
```

2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

## Cấu hình

Mở file `list_postgres_tables.py` và chỉnh sửa thông tin kết nối database trong phần `DB_CONFIG`:

```python
DB_CONFIG = {
    'host': 'localhost',      # Địa chỉ database server
    'database': 'mydb',       # Tên database
    'user': 'postgres',       # Tên user
    'password': 'password',   # Mật khẩu
    'port': 5432              # Cổng (mặc định: 5432)
}
```

## Sử dụng

Chạy script:
```bash
python list_postgres_tables.py
```

Kết quả sẽ được lưu vào file `tables_list.txt` trong thư mục hiện tại.

## Output

File `tables_list.txt` sẽ chứa:
- Tổng số bảng trong database
- Danh sách tên các bảng (được sắp xếp theo alphabet)

## Ví dụ output

```
PostgreSQL Tables List
==================================================

Total tables: 5

1. customers
2. orders
3. products
4. users
5. transactions
```

## Lưu ý

- Script chỉ liệt kê các bảng trong schema `public`
- Đảm bảo user có quyền truy cập vào `information_schema`