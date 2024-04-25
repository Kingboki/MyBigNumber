class MyBigNumber: #tạo lớp MyBigNumber
    def sum(self, stn1, stn2): #tạo hàm sum với 2 chuỗi stn1 và stn2
        result = ""  #tạo biến kết quả
        carry = 0    #tạo biến nhớ
        i = len(stn1) - 1 #tạo biến i
        j = len(stn2) - 1 #tạo biến j
        

        while i >= 0 or j >= 0: #Bắt đầu 1 vòng lặp để duyệt qua các ký tự của 2 chuỗi cho đến khi cả 2 chuỗi đều được duyệt hết
            digit1 = int(stn1[i]) if i >= 0 else 0 #tạo biến tên digit1 
            digit2 = int(stn2[j]) if j >= 0 else 0 #tạo biến tên digit2
            total = digit1 + digit2 + carry  #tạo biến total 

            result = str(total % 10) + result #Lấy total đã cộng được chia 10 và lấy phần dư  
            carry = total // 10 #Lấy total đã cộng được chia 10 và lấy phần nguyên

            if total >= 10: #gọi lệnh if
                print(f"Bước {len(stn1) - i}: Lấy {digit1} cộng với {digit2} được {total}. Lưu {total % 10} vào kết quả và nhớ {total // 10}.")
            else:
                print(f"Bước {len(stn1) - i}: Lấy {digit1} cộng với {digit2} được {total}. Lưu {total} vào kết quả.")

            i -= 1 #di chuyển về phía trước trong chuỗi để duyệt các ký tự tiếp theo
            j -= 1 #di chuyển về phía trước trong chuỗi để duyệt các ký tự tiếp theo

        if carry: #gọi lệnh if kiểm tra xem có giá trị nhớ cuối cùng hay không
            result = str(carry) + result #Nếu có giá trị nhớ thì sẽ thêm vào kết quả
            print(f"Lưu {carry} vào kết quả cuối cùng.")

        
        return "Vậy tổng là:" + result

# Sử dụng lớp MyBigNumber
my_calculator = MyBigNumber()
print(my_calculator.sum("1234", "897"))
