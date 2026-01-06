![alt text](../images/task3/classical-cryptography.png)
---
# Thuật toán mật mã cổ điển
Thuật toán mật mã cổ điển là các phương pháp mã hóa ra đời sớm, chủ yếu trước thời kỳ xuất hiện máy tính hiện đại, nó dựa trên toán học đơn giản và xử lý ký tự (chữ cái), thường để che giấu nội dung hơn là bảo mật.

👉 Các thuật toán này thường sử dụng:
- Bảng chữ cái A-Z
- Phép thay thế (substitution) hoặc hoán vị (transposition)
- Không sử dụng khóa lớn hay phép toán phức tạp

Tuy nhiên, dễ bị phá bằng phân tích tần suất (frequency analysis)

📌 Mục đích chính:
- Truyền tin bí mật trong quân sự, ngoại giao
- Và là nền tảng để hiểu mật mã học hiện đại

# Tìm hiểu một số loại mật mã học cổ điển
| Thuật toán     | Thuộc loại                   | Mô tả                                     |
| -------------- | ---------------------------- | ----------------------------------------- |
| Caesar         | Substitution                 | Dịch chữ cái cố định                      |
| Affine         | Substitution                 | Công thức toán học tuyến tính             |
| Vigenere       | Polyalphabetic Substitution  | Dùng nhiều bảng Caesar                    |
| Playfair       | Digraph Substitution         | Mã hóa theo cặp chữ cái                   |
| Hill           | Matrix-based Substitution    | Thay thế dựa trên ma trận                 | 

Chúng ta sẽ tìm hiểu 5 loại thuật toán này dựa trên các tiêu chí sau:
- Nguyên lý hoạt động
- Cách thức mã hóa - giải mã
- Các điểm yếu bảo mật

## 1. Caesar
![alt text](../images/task3/caesar.png)
### 🔹Nguyên lý hoạt động:  
Caesar là thuật toán thay thế đơn bảng. Mỗi chữ cái được dịch đi một số bước cố định so với bảng chữ cái gốc.

### 🔹Mã hóa  
- E(x) = (x + k) mod 26

Ví dụ:  
- Chọn khóa k = 3
- Quy ước A = 0, B = 1,..., Z = 25  
- Plaintext: **HELLO**

| Chữ gốc | Giá trị   | +3 | Chữ mã hóa |
|---------|-----------|----|------------|
| H       | 7         | 10 | K          |
| E       | 4         | 7  | H          |
| L       | 11        | 14 | O          |
| L       | 11        | 14 | O          |
| O       | 14        | 17 | R          |

> 👉 Ciphertext: **KHOOR**  

### 🔹Giải mã:  
- D(x) = (x - k) mod 26

Ví dụ:  
- Ciphertext: **KHOOR**
- Khóa: k = 3

| Chữ mã hóa | Giá trị   | +3 | Chữ gốc |
|------------|-----------|----|---------|
| H          | 10        | 7  | H       |
| E          | 7         | 4  | E       |
| L          | 14        | 11 | L       |
| L          | 14        | 11 | L       |
| O          | 17        | 14 | O       |

> 👉 Plaintext: **HELLO**

### 🔹Điểm yếu bảo mật:
- Không gian khóa rất nhỏ (25 khóa)
- Dễ dễ brute-force
- Phân tích tần suất phá được ngay

## 2. Affine Cipher
![alt text](../images/task3/affine.png)
### 🔹Nguyên lý hoạt động
Affine là mở rộng của Caesar, sử dụng hàm tuyến tính thay vì chỉ dịch cố định. Mỗi chữ cái được ánh xạ thông qua hai tham số a và b.

Trong đó: 
- a phải nguyên tố cùng nhau với 26 (gcd(a, 26)=1)
- b là hằng số dịch

### 🔹Mã hóa
- E(x) = (ax + b) mod 26

Ví dụ:
- Chọn khóa: a = 5, b = 8  
- Quy ước: A = 0, B = 1, ..., Z = 25
- Plaintext: **HELLO**

| Chữ gốc | Giá trị | (5x + 8) mod 26 | Chữ mã hóa |
| ------- | ------- | --------------- | ---------- |
| H       | 7       | 17              | R          |
| E       | 4       | 2               | C          |
| L       | 11      | 11              | L          |
| L       | 11      | 11              | L          |
| O       | 14      | 0               | A          |

> 👉 Ciphertext: RCLLA

### 🔹Giải mã
- D(x) = a<sup>-1</sup>(x - b) mode 26  
- Trong đó a<sup>-1</sup> là nghịch đảo modulo 26 của a

Với a = 5 => a<sup>-1</sup> = 21 vì 5.21 = 1 (mod 26)  
Có R = 17,
- x = 21(17-8) mod 26 = 21.9 mod 26 = 189 mod 26 = 7 => H  
> Giải tương tự ta sẽ dò ra được chuỗi gốc là : **HELLO**

### 🔹Điểm yếu bảo mật
- Vẫn là thay thế đơn bảng
- Dễ bị phân tích tần suất (frequency analysis)
- Không gian khóa nhỏ

## 3. Vigenère
![alt text](../images/task3/vigenère.png)
### 🔹Nguyên lý hoạt động
- Là mật mã thay thế đa bảng (polyalphabetic cipher)
- Sử dụng từ khóa (key) để xác định độ dịch cho từng ký tự
- Mỗi chữ cái trong bản rõ được mã hóa bằng một Caesar Cipher khác nhau dựa trên ký tự tương ứng của khóa

### 🔹Mã hóa
- Lặp lại cho đến khi độ dài bằng bản rõ
- C = (P + K) mod 26

> Trong đó
> - P: ký tự bản rõ
> - K: ký tự khóa
> - C: ký tự mã hóa

### 🔹Giải mã
- Sử dụng cùng khóa đã dùng để mã hóa
- P = (C - K) mod 26

### 🔹Điểm yếu bảo mật
- Nếu khóa ngắn, có thể bị phá bằng Kasiski Examination hoặc Frequency Analysis.
- Không an toàn trước các phương pháp tấn công hiện đại.
- Chỉ mang tính lịch sử và học thuật, không dùng trong thực tế.

## 4. Playfair
![alt text](../images/task3/playfair.png)
### 🔹Nguyên lý hoạt động
- Là mật mã thay thế đa ký tự (digraph cipher).
- Sử dụng bảng 5×5 tạo từ khóa (gộp I/J).
- Mã hóa theo từng cặp chữ cái thay vì từng ký tự đơn lẻ.

### 🔹Mã hóa
- Chia rõ thành các cặp chữ cái
- Quy tắc mã hóa: 
    - Cùng hàng -> Lấy chữ bên phải
    - Cùng cột -> Lấy chữ bên dưới
    - Khác hàng & cột -> tạo hình chữ nhật và lấy chữ cùng hàng
- Thêm ký tự đệm (thường là X) nếu cần

### 🔹Giải mã
- Áp dụng ngược lại các quy tắc mã hóa
    - Cùng hàng -> lấy chữ bên trái
    - Cùng cột -> lấy chữ bên trên
    - Hình chữ nhật -> lấy chữ tương ứng
-  Loại bỏ ký tự đệm sau khi giải mã

### 🔹Điểm yếu bảo mật
- Dễ bị phá bằng phân tích tần suất cặp chữ.
- Không an toàn trước tấn công hiện đại.
- Không phù hợp cho bảo mật thực tế.

## 5. Hill
![alt text](../images/task3/hill.png)
### 🔹Nguyên lý hoạt động
- Là mật mã thay thế đa ký tự dựa trên đại số tuyến tính.
- Sử dụng ma trận khóa vuông kích thước n×n.
- Mã hóa theo từng khối ký tự.

### 🔹Mã hóa
- Chuyển chữ cái thành số (A=0, B=1, ..., Z=25).
- Nhân vector bản rõ với ma trận khóa:
    - C = K × P mod 26
- Kết quả được chuyển ngược lại thành chữ cái

### 🔹Giải mã
- Tính ma trân nghịch đảo của khóa (mod 26)
- Công thức:
    - P = K⁻¹ × C mod 26
- Chỉ giải mã được nếu ma trận khóa khả nghịch

### 🔹Điểm yếu bảo mật
- Dễ bị phá nếu có plaintext–ciphertext pairs.
- Quản lý khóa phức tạp.
- Không an toàn trong các hệ thống hiện đại.
