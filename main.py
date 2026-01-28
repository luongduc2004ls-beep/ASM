import protduct_manager as pm
    
def menu():
    print("\n==========QUẢN LÝ SẢN PHẨM========")
    print("1.Hiển thị danh sách sản phẩm")
    print("2.Cập nhật danh sách sản phẩm")
    print("3.Sửa danh sách sản phẩm")
    print("4.Xóa sản phẩm")
    print("0.Thoát")

while True:
    menu()

    choice = input("Chọn chức năng:")
   
    if choice == "1":
        pm.show_product()
    elif choice == "2":
        pm.add_product()
    elif choice == "3":
        pm.update_product()
    elif choice == "4":
        pm.delete_product
    elif choice == "0":
        print("Thoát chương trình!")
        break
    else:
     print("Lựa chọn không hợp lệ!")

    