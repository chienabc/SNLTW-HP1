'''
Kiến thức sử dụng trong sản phẩm
1. Biến và các kiểu dữ liệu
2. Các phép so sánh
3. Vòng lặp
4. Lệnh điều kiên
5. chuỗi
6. List
'''
print("******************PHẦN MỀM QUẢN LÝ QUÁN CƠM GÀ *****************")
monan = ['Cơm gà xối mỡ đùi măm tỏi', 'Mì xào bò', ' Hủ tiếu Xào']
gia = [5000, 2500,  3000]

trangchu = 1

while trangchu == 1 :
    chucNang = int(input("Mời bạn chọn các chức năng sau đây :\n1. Hiển thị danh sách: \n2. Nhập thông tin danh sách: \n3. Sửa thông tin: \n4. Gọi món: \n5. Chọn chức năng:"))

    while chucNang < 1 and chucNang > 4 :
          print("Không có thông tin mà bạn đã chọn, Mời bạn chọn lại")
          chucNang = int(input("Mời bạn chọn các chức năng sau đây\n1. Hiển thị danh sách\n2. Nhập thông tin danh sách\n3. Sửa thông tin \n4. Gọi món\n5. Chọn chức năng"))

    thoat = 1

    while thoat == 1:
       if chucNang ==1:
         temp=0
         while temp <len(monan):
            print("Món ăn : " , monan[temp])
            print("Giá" ,gia[temp], "VNĐ" )
            temp = temp + 1
            print("-------------------------------------------------")
         break
       elif chucNang ==2:
            monan.append(input("Nhập tên món ăn : "))
            gia.append(float(input("Nhập giá : ")))
            print("------------------------------------")
            break
       elif chucNang == 3:
          a = 1
          for x in monan :
            print("Tên món ăn")
            print(a , ".",x)
            print("-----------------------------------")
            a+=1
          chinhsua = int(input("Chọn thông tin mà bạn cần chỉnh sửa : "))
          monan[chinhsua - 1] = input("Nhập tên món ăn : ")
          gia[chinhsua -1] = int(input("Nhập giá tiền món ăn : "))
          break
       else:
        if len(monan) == 0:
            print("****")
            break
        khachHang = input("Nhập tên khách hàng : ")
        banId = int(input("Nhập số bàn mà khách đặt món : "))
        temp = 0
        print("Danh sách gọi món : ")
        while temp < len(monan):
            print(temp + 1, " . " , monan[temp])
            print("Giá:" , gia[temp], "VNĐ")
            temp = temp + 1
            print("------------------------------")
        inBill = int(input("Chọn món ăn mà bạn cần : "))
        print("-----------------------Hoá Đơn----------------------------")
        print("Tên khách hàng" , khachHang)
        print("Số Bàn" , banId)
        print("Tên món ăn",monan[inBill - 1])
        print("Giá món ăn" , gia[inBill - 1])
        print("---------------------------------------------------------")
        break
trangchu = int(input("Bạn có muốn tiếp tục chức năng không? 1.Yes - 0.No : " ))
thoat = int(input("Bạn có muốn tiếp tục chương trình không? 1.Yes - 0.No : " ))