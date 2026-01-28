product = []

def show_product():
    if not product:
        print("Danh sách sản phẩm đang trống!")
        return
    for p in product:
        print(p)
def add_product():
    products = {
        "id": input("Nhập mã sản phẩm: "),
        "name": input("Nhập tên sản phẩm: "),
        "brand": input("Nhập thương hiệu: "),
        "price": int(input("Nhập giá: ")),
        "quantity": int(input("Nhập số lượng: "))
    }
    product.append(products)
    print("Thêm sản phẩm thành công")
def update_product():
    product_id = input("Nhập mã sản phẩm cần sửa: ")
    products = product_id
    if product:
        product["name"] = input("Tên mới")
        
        product["brand"] = input("Thương hiệu mới")
        product["price"] = int(input("Giá mới"))
        product["quantity"] = int(input("Số lượng mới"))
        print("Cập nhật sản phẩm thành công")
    else:
        print("Không tìm thấy sản phẩm")
def delete_product():
    product_id = input("Nhập mã sản phẩm cần xóa")
    products = product_id
    if product:
        product.remove(products)
        
        print("Xóa sản phẩm thành công!")
    else:
        print("Không tìm thấy sản phẩm.")