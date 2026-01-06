![alt text](../images/task3/cryptography-overview.png)
---

# Tổng quan về mật mã học

## 📘Mật mã học là gì? 
Mật mã học (Cryptography) là ngành khoa học nghiên cứu các kỹ thuật bảo vệ thông tin bằng cách biến đổi dữ liệu sao cho chỉ những thực thể được phép mới có thể hiểu và sử dụng được thông tin đó.

---

Mật mã học gồm 2 mảng chính:
1. 🔐Cryptography
- Chuyên thiết kế và xây dựng thuật toán mã hóa
- Ví dụ:
    - Mã hóa đối xứng: AES, DES, 3DES
    - Mã hóa bất đối xứng: RSA, ECC
    - Hàm băm (hash): SHA-256, SHA-3
    - Chữ ký số (Digital Signature)

> Cryptography tập trung vào xây dựng các hệ thống bảo mật an toàn.

2. 🧠Cryptanalysis
- Nghiên cứu điểm yếu của các hệ thống bảo mật
- Tìm cách:
    - Giải mã
    - Phát hiện lỗ hỏng
    - Đánh giá mức độ an toàn của thuật toán
- Ví dụ một số dạng tấn công phổ biến:
    - Brute-force
    - Known-plaintext
    - Chosen-plaintext / Chosen-ciphertext
    - Side-channel (timming, power, cache)
    - Mathematical (khai thác điểm yếu toán học)

>Cryptanalysis không phải để phá hoại mà để kiểm tra độ an toàn, cải tiến và nâng cấp hệ thống mã hóa.

## 🎭Mối quan hệ giữa Cryptography & Cryptanalysis

| Cryptography | Cryptanalysis |
| ----------------- | -------------------------- |
| Xây dựng          | Phân tích, tấn công        |
| Phòng thủ         | Kiểm thử                   |
| Tạo thuật toán    | Tìm điểm yếu               |
| Mục tiêu: An toàn | Mục tiêu: Đánh giá an toàn |

Trong quá tình phát triển 2 mảng này có sự bổ trợ rất lớn với nhau, giúp hệ thống bảo mật ngày càng mạng hơn.

## 🎯Mục tiêu chính
- Tính bí mật (Confidentiality)
- Tính toán vẹn (Integrity)
- Tính xác thực (Authentication)
- Non-repudiation (Chống chối bỏ - chống phủ nhận)

Không chỉ `ngăn bên thứ ba đọc được`, mà còn đảm bảo tính toàn vẹn và xác thực của dữ liệu.

> Đây chính là cốt lõi trong mô hình hình CIA + Authentication + Non-repudiation của an toàn thông tin

## 🧩Vai trò
* Là nền tảng cho các hệ thống an toàn thông tin hiện đại
* Bảo mật dữ liệu lưu trữ và truyền thông mạng
* Hỗ trợ xác thực, chữ ký số và giao dịch điện tử
* Ứng dụng trong HTTPS, VPN, Blockchain, Clound Security