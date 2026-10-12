# Mục tiêu bài toán

# Kiểm tra một chuỗi có hợp lệ mặt cấu trúc dấu ngoặc hay không. Một chuỗi được coi là hợp lệ nếu:
# 1. Mỗi dấu ngoặc mở phải có một dấu ngoặc đóng tương ứng (ngoặc tròn '()', ngoặc vuông '[]', ngoặc nhọn '{}')
# 2. Dấu ngoặc mở phải có dấu ngoặc đóng, nghĩa là phải có cặp dấu đúng theo cặp
# Ví dụ
# "()", "() []", "{[]}"
# "({)}" đây là sai vì ngoặc tròn có trước nhưng không đóng trước

# Cách tiếp cận bài toán

# 1. Sử dụng Stack (Ngăn xếp): 
# Nguyên lý cơ bản là chúng ta sẽ sử dụng một stack để theo dõi các dấu ngoặc mở.
# Mỗi khi gặp một dấu ngoặc đóng, chúng ta sẽ kiểm tra xem dấu ngoặc mở tương ứng có nằm trên đỉnh stack không.

# Stack là một cấu trúc dữ liệu hoạt động theo nguyên lý "LIFO" (Last In, First Out),nghĩa là phần tử được thêm vào sau cùng sẽ được lấy ra trước tiên.
# Đây là cách để kiểm tra cặp ngoặc vì mỗi "dấu ngoặc đóng" phải tương ứng với "dấu ngoặc mở" gần nhất chưa được đóng.

# 2. Bước giải quyết:
# Khởi tạo stack: Ta sẽ khởi tạo một stack rỗng.
# Duyệt chuỗi: Ta sẽ duyệt qua từng ký tự trong chuỗi

# Nếu ký tự là dấu ngoặc mở ('(', '{', '['), ta đẩy nó vào stack. Nếu ký tự là dấu ngoặc đóng (')', '}', ']'), ta sẽ làm các bước sau:
# B1 Kiểm tra xem stack có rỗng không. Nếu rỗng, có nghĩa là không có dấu ngoặc mở tương ứng, chuỗi không hợp lệ.

# B2 Nếu stack không rỗng, ta lấy phần tử trên đỉnh của stack ra và kiểm tra xem nó có phải là dấu ngoặc mở tương ứng với dấu ngoặc đóng hiện tại không.
# Nếu không khớp, chuỗi không hợp lệ.
# Cuối cùng: Sau khi duyệt hết chuỗi, nếu stack vẫn còn phần tử nào (có dấu ngoặc mở chưa được đóng), chuỗi không hợp lệ. Nếu stack rỗng, chuỗi hợp lệ.

def isValid(s: str) -> bool:
    stack = []  # Khởi tạo stack rỗng
    # Tạo một từ điển cho các dấu ngoặc đóng và mở
    mapping = {')': '(', '}': '{', ']': '['}
    
    # Duyệt qua từng ký tự trong chuỗi
    for char in s:
        if char in mapping:  # Nếu gặp dấu ngoặc đóng
            top_element = stack.pop() if stack else '#'  # Lấy phần tử trên đỉnh stack (nếu có)
            if mapping[char] != top_element:  # Kiểm tra xem dấu ngoặc đóng có khớp với dấu ngoặc mở không
                return False  # Nếu không khớp, trả về False
        else:  # Nếu gặp dấu ngoặc mở
            stack.append(char)  # Đẩy dấu ngoặc mở vào stack
    
    return not stack  # Nếu stack rỗng, trả về True (chuỗi hợp lệ), nếu không, trả về False

# Giải thích 
# 1. Khởi tạo stack và mapping
# stack = []
# mapping = {')': '(', '}': '{', ']': '['}
# stack: Là nơi chúng ta sẽ lưu trữ các dấu ngoặc mở.
# mapping: Là từ điển các dấu ngoặc đóng với dấu ngoặc mở tương ứng. Ví dụ, nếu gặp ')', chúng ta cần tìm '(' trên đỉnh của stack.

# Dưới đây là giải thích chi tiết hơn về cách giải bài toán Valid Parentheses sử dụng stack (ngăn xếp) trong Python.

# Mục tiêu bài toán:
# Bạn cần kiểm tra một chuỗi có hợp lệ về mặt cấu trúc dấu ngoặc hay không. Một chuỗi được coi là hợp lệ nếu:

# Mỗi dấu ngoặc mở ('(', '{', '[') phải có một dấu ngoặc đóng tương ứng (')', '}', ']') theo đúng thứ tự.
# Dấu ngoặc mở phải được đóng đúng vị trí (tức là phải theo đúng cặp ngoặc).
# Ví dụ:
# "()" -> hợp lệ
# "()[]" -> hợp lệ
# "([)]" -> không hợp lệ, vì ngoặc ( được mở trước nhưng không đóng đúng theo thứ tự.
# "{[]}" -> hợp lệ
# "(" -> không hợp lệ, vì có dấu ngoặc mở mà không có dấu ngoặc đóng.
# Cách tiếp cận giải quyết bài toán:
# 1. Sử dụng Stack (Ngăn xếp):
# Nguyên lý cơ bản là chúng ta sẽ sử dụng một stack để theo dõi các dấu ngoặc mở. Mỗi khi gặp một dấu ngoặc đóng, chúng ta sẽ kiểm tra xem dấu ngoặc mở tương ứng có nằm trên đỉnh stack không.

# Stack là một cấu trúc dữ liệu hoạt động theo nguyên lý "LIFO" (Last In, First Out), nghĩa là phần tử được thêm vào sau cùng sẽ được lấy ra trước tiên. Đây là lý tưởng để kiểm tra cặp ngoặc vì mỗi dấu ngoặc đóng phải tương ứng với dấu ngoặc mở gần nhất chưa được đóng.
# 2. Bước giải quyết:
# Khởi tạo stack: Ta sẽ khởi tạo một stack rỗng.
# Duyệt chuỗi: Ta sẽ duyệt qua từng ký tự trong chuỗi.
# Nếu ký tự là dấu ngoặc mở ('(', '{', '['), ta đẩy nó vào stack.
# Nếu ký tự là dấu ngoặc đóng (')', '}', ']'), ta sẽ làm các bước sau:
# Kiểm tra xem stack có rỗng không. Nếu rỗng, có nghĩa là không có dấu ngoặc mở tương ứng, chuỗi không hợp lệ.
# Nếu stack không rỗng, ta lấy phần tử trên đỉnh của stack ra và kiểm tra xem nó có phải là dấu ngoặc mở tương ứng với dấu ngoặc đóng hiện tại không. Nếu không khớp, chuỗi không hợp lệ.
# Cuối cùng: Sau khi duyệt hết chuỗi, nếu stack vẫn còn phần tử nào (có dấu ngoặc mở chưa được đóng), chuỗi không hợp lệ. Nếu stack rỗng, chuỗi hợp lệ.
# 3. Mã nguồn:
# Dưới đây là mã Python với giải thích từng phần:

# Dùng Type hinting 
class Solution:
   def isValid(s: str) -> bool:
    stack = []  # Khởi tạo stack rỗng
    # Tạo một từ điển để ánh xạ các dấu ngoặc đóng và mở
    mapping = {')': '(', '}': '{', ']': '['}
    
    # Duyệt qua từng ký tự trong chuỗi
    for char in s:
        if char in mapping:  # Nếu gặp dấu ngoặc đóng
            top_element = stack.pop() if stack else '#'  # Lấy phần tử trên đỉnh stack (nếu có)
            if mapping[char] != top_element:  # Kiểm tra xem dấu ngoặc đóng có khớp với dấu ngoặc mở không
                return False  # Nếu không khớp, trả về False
        else:  # Nếu gặp dấu ngoặc mở
            stack.append(char)  # Đẩy dấu ngoặc mở vào stack
    
    return not stack  # Nếu stack rỗng, trả về True (chuỗi hợp lệ), nếu không, trả về False

# Không dung Type hinting:
class Solution:
    def isValid(self, s):  # Không khai báo kiểu dữ liệu
        stack = []  # Khởi tạo stack rỗng
        mapping = {')': '(', '}': '{', ']': '['}  # Tạo từ điển ánh xạ dấu ngoặc đóng với dấu ngoặc mở
        
        # Duyệt qua từng ký tự trong chuỗi
        for char in s:
            if char in mapping:  # Nếu gặp dấu ngoặc đóng
                top_element = stack.pop() if stack else '#'  # Lấy phần tử trên đỉnh stack (nếu có)
                if mapping[char] != top_element:  # Kiểm tra dấu ngoặc đóng có khớp với dấu ngoặc mở không
                    return False
            else:  # Nếu gặp dấu ngoặc mở
                stack.append(char)  # Đẩy dấu ngoặc mở vào stack
        
        return not stack  # Nếu stack rỗng, chuỗi hợp lệ, nếu không, không hợp lệ

# Type hinting là gì
# Type hinting là cách bạn chỉ rõ kiểu dữ liệu của biến hoặc tham số trong hàm.
# Mục đích của nó là giúp mã dễ đọc hơn, dễ hiểu hơn và hỗ trợ công cụ kiểm tra lỗi.

# Ví dụ:
# Bạn có thể nói rõ rằng tham số của hàm là một chuỗi (string) hoặc một số nguyên (integer) thay vì để Python tự đoán.
# def greet(name: str) -> str:
#    return "Hello, " + name
# Ở đây:

# name: str có nghĩa là name phải là một chuỗi.
# -> str có nghĩa là hàm này sẽ trả về một chuỗi.

# Giải thích chi tiết:

# 1. Khởi tạo stack và mapping:
# stack = []
# mapping = {')': '(', '}': '{', ']': '['}
# stack: Là nơi chúng ta sẽ lưu trữ các dấu ngoặc mở.
# mapping: Là từ điển các dấu ngoặc đóng với dấu ngoặc mở tương ứng. Ví dụ, nếu gặp ')', chúng ta cần tìm '(' trên đỉnh của stack.

# 2.Duyệt qua chuỗi:
# for char in s:  Ta duyệt qua từng chuỗi s

# 3. Nếu gặp dấu ngoặc đóng:
# if char in mapping:
#    top_element = stack.pop() if stack else '#'
#    if mapping[char] != top_element:
#        return False

# Nếu ký tự là dấu ngoặc đóng (ví dụ: ), }, ]), ta thực hiện:

# Lấy phần tử trên đỉnh của stack: Nếu stack không rỗng, ta lấy phần tử trên đỉnh (dấu ngoặc mở) ra,
# nếu stack rỗng thì ta gán top_element là # (một giá trị không hợp lệ, chỉ để xử lý trường hợp không có phần tử nào trong stack).

# Kiểm tra khớp: Nếu phần tử trên đỉnh stack không khớp với dấu ngoặc mở tương ứng trong mapping, trả về False (chuỗi không hợp lệ).

# 4. Nếu gặp dấu ngoặc mở:
# else:
#    stack.append(char)

# Nếu ký tự là dấu ngoặc mở (ví dụ: (, {, [), ta thêm nó vào stack để theo dõi.

# 5. Kết thúc chuỗi
# return not stack

# Nếu stack rỗng sau khi duyệt hết chuỗi, có nghĩa là tất cả dấu ngoặc mở đã được đóng hợp lệ, ta trả về True.
# Nếu stack không rỗng, có nghĩa là vẫn còn dấu ngoặc mở chưa được đóng, ta trả về False.

