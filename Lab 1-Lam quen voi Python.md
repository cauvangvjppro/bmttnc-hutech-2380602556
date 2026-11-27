BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 1
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI
PYTHON
Bài học này sẽ giới thiệu về ngôn ngữ lập trình Python, cung cấp các kiến thức cơ
bản về các kiểu dữ liệu, biến, biểu thức, cấu trúc chương trình và lập trình hướng đối
tượng trong Python. Mục tiêu của bài này là giúp sinh viên quen thuộc với các khái
niệm Python cơ bản để có thể thực hành và sử dụng trong các bài tiếp theo. Ngoài ra,
bài này cũng giới thiệu và hướng dẫn sinh viên làm quen, thực hành với các công cụ
hỗ trợ khi lập trình Python, hệ thống kiểm soát phiên bản và sử dụng công cụ kiểm
thử cho các bài tập về bảo mật thông tin.
1.1 NGÔN NGỮ PYTHON
Python là một ngôn ngữ lập trình bậc cao được thông dịch, nổi bật với cú pháp rõ
ràng và dễ hiểu, giúp lập trình viên tập trung vào việc giải quyết vấn đề mà không
phải bận tâm quá nhiều về quy tắc ngữ pháp. Được phát triển bởi Guido van Rossum
vào đầu những năm 90, Python nhanh chóng trở thành một trong những ngôn ngữ
được ưa chuộng nhất toàn cầu.
Một trong những ưu điểm nổi bật của Python là tính linh hoạt, cho phép nó được
sử dụng cho nhiều mục đích khác nhau như phát triển ứng dụng web, trí tuệ nhân
tạo, khoa học dữ liệu, máy học, và phát triển game. Ngôn ngữ này còn có hàng loạt
thư viện phong phú như NumPy, Pandas, TensorFlow, và Django, giúp mở rộng khả
năng của nó.
Cộng đồng Python đóng vai trò quan trọng trong sự phát triển và lan tỏa của ngôn
ngữ này. Với một cộng đồng lớn mạnh, người dùng không chỉ có thể tiếp cận nhiều tài
nguyên phong phú mà còn nhận được sự hỗ trợ và chia sẻ kiến thức thông qua các
diễn đàn, trang web học tập, sự kiện và các dự án mã nguồn mở.
2 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
Không chỉ linh hoạt và có cộng đồng hỗ trợ mạnh mẽ, Python còn được đánh giá
cao về khả năng tích hợp dễ dàng với các ngôn ngữ và hệ thống khác. Nó cung cấp
```
giao diện ứng dụng (API) linh hoạt, hỗ trợ nhiều nền tảng, và có khả năng mở rộng
```
cao, điều này giúp việc phát triển các dự án phức tạp trở nên thuận lợi hơn.
So sánh độ phổ biến các ngôn ngữ lập trình
```
(Nguồn: https://cdn.statcdn.com)
```
Với tất cả những ưu điểm trên, Python là một ngôn ngữ thông dịch mạnh mẽ. Sự
kết hợp giữa cú pháp dễ đọc, tính linh hoạt, và cộng đồng mạnh mẽ đã đặt Python ở
vị thế dẫn đầu trong thế giới lập trình, khẳng định uy tín của mình trong nhiều lĩnh
vực công nghệ hiện đại.
1.2 THÀNH PHẦN CỦA PYTHON
1.2.1 Biến, từ khóa
```
“Trong Python, biến (variables) được hiểu là một tên gọi dùng để chỉ một giá trị nhất
```
định trong bộ nhớ. Có thể coi biến như một nhãn gán cho một giá trị dữ liệu cụ thể. Việc
tạo ra biến rất đơn giản và không yêu cầu khai báo kiểu dữ liệu. Kiểu dữ liệu của biến sẽ
được Python xác định tự động dựa trên giá trị mà chúng ta gán cho nó” [1].
Khi xem xét đoạn mã dưới đây, ta thấy rằng Python tự động nhận diện kiểu dữ liệu
của biến theo giá trị được gán. Ngoài ra, biến trong Python có khả năng thay đổi giá
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 3
trị trong suốt quá trình thực thi chương trình, nghĩa là ta có thể cập nhật giá trị mới
cho một biến đã được khởi tạo.
```
Từ khóa (keywords) trong Python là các từ đã được định nghĩa, có ý nghĩa đặc biệt
```
trong ngôn ngữ. Các từ khóa này đã được dành riêng thực hiện một số chức năng cụ
thể và không được sử dụng làm tên biến, nhãn khác trong chương trình. Ta không thể
sử dụng một từ khóa như tên biến:
Bảng dưới đây là danh sách các từ khóa của Python, các từ này đều có ý nghĩa đặc
biệt và đã được dành riêng cho việc thực hiện các chức năng cụ thể:
4 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHONBÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 5
1.2.2 Kiểu dữ liệu
“Python hỗ trợ nhiều loại dữ liệu khác nhau để lưu trữ và xử lý thông tin” [1], [2].
Dưới đây là một số kiểu dữ liệu cơ bản và thông dụng trong Python:
- Kiểu dữ liệu số (Numeric Types):
• “int”: Kiểu dữ liệu số nguyên, lưu trữ số nguyên không có dấu thập phân.
• “float”: Kiểu dữ liệu số thực, lưu trữ số có dấu thập phân.
• “complex”: Kiểu dữ liệu số phức, lưu trữ số phức với phần thực, phần ảo.
- Kiểu dữ liệu chuỗi (String Type):
• “str”: Kiểu dữ liệu chuỗi, lưu trữ chuỗi ký tự, được bao quanh bởi ' ' hoặc “ ”.
- Kiểu dữ liệu Boolean (Boolean Type):
• “bool”: Kiểu boolean chỉ có hai giá trị là True hoặc False. Được dùng để biểu
diễn các trạng thái logic.
- Kiểu dữ liệu danh sách (List Type):
• “list”: Kiểu dữ liệu danh sách lưu trữ tập hợp các phần tử có thứ tự và có thể
thay đổi.
6 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Kiểu dữ liệu tuple (Tuple Type):
• “tuple”: Kiểu dữ liệu tuple tương tự như danh sách nhưng không thể thay đổi
```
(immutable).
```
- Kiểu dữ liệu từ điển (Dictionary Type):
• “dict”: Kiểu dữ liệu lưu trữ các cặp key-value không có thứ tự. Key là duy nhất,
```
không thay đổi; value có thể thay đổi.
```
- Kiểu dữ liệu tập hợp (Set Type):
• “set”: Đây là kiểu dữ liệu dùng để lưu trữ một tập hợp các phần tử không trùng
lặp và không có thứ tự.
- Kiểu dữ liệu bộ nhớ đóng (Frozen Set Type):
• “frozenset”: Tương tự như kiểu dữ liệu set nhưng không thể thay đổi
```
(immutable).
```
- Kiểu dữ liệu nhị phân (Binary Types):
• “bytes”: Lưu trữ một chuỗi byte.
```
• “bytearray”: Tương tự như bytes nhưng có thể thay đổi (mutable).
```
- Kiểu dữ liệu None (None Type):
• NoneType: Chỉ có một giá trị là “None”, được dùng để biểu diễn giá trị rỗng
hoặc không tồn tại.
1.2.3 Các toán tử số học
“Trong Python, các toán tử số học được sử dụng để thực hiện các phép toán cơ bản
trên các số. Các toán tử này cho phép bạn thực hiện các phép cộng, trừ, nhân, chia,
các phép tính khác trên các biến hoặc giá trị số” [1], [2]. Sau đây là các toán tử số
học cơ bản trong Python:
- Cộng (+): Toán tử cộng được dùng để thực hiện phép cộng giữa hai số.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 7
- Trừ (-): Toán tử trừ được dùng để thực hiện phép trừ giữa hai số.
- Nhân (*): Toán tử nhân được dùng để thực hiện phép nhân giữa hai số.
- Chia (/): Toán tử chia được dùng để thực hiện phép chia.
- Chia lấy phần nguyên (//): Toán tử chia lấy phần nguyên trả về kết quả là
phần nguyên của phép chia.
- Chia lấy dư (%): Toán tử này sẽ cung cấp phần còn lại sau khi thực hiện phép
chia giữa hai số.
- Luỹ thừa (**): Toán tử luỹ thừa được sử dụng để tính toán lũy thừa của một số.
8 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
Các toán tử số học này có thể được dùng trong các biểu thức để thực hiện các
phép tính số học cơ bản. Đồng thời, Python cũng hỗ trợ việc sử dụng các dấu ngoặc
để xác định ưu tiên của các phép tính, giúp thực hiện các phép toán chính xác theo ý
muốn.
1.2.4 Các toán tử logic
“Trong Python, các toán tử logic được sử dụng để thực hiện phép toán logic trên
```
các giá trị boolean (True hoặc False) hoặc các biểu thức logic. Các toán tử logic cho
```
phép chúng ta kiểm tra và thực hiện các phép so sánh, kết hợp các điều kiện để quyết
định kết quả logic” [1], [2]. Sau đây sẽ trình bày một vài toán tử logic cơ bản trong
```
Python:
```
- Phép toán AND: Toán tử “and” trả về “True” nếu cả hai điều kiện đều đúng.
- Phép toán OR: Toán tử “or” trả về “True” nếu ít nhất một trong hai điều kiện đầu
vào là đúng.
- Phép toán NOT: Toán tử “not” trả về “True” nếu điều kiện là “False” và ngược lại.
- Phép so sánh bằng (==): Toán tử “==” sẽ so sánh hai giá trị có bằng nhau hay
không.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 9
- Phép so sánh không bằng (!=): Toán tử “!=” sẽ so sánh hai giá trị có khác
nhau hay không.
- Phép so sánh lớn hơn (>), nhỏ hơn (<): Toán tử “>” sẽ so sánh xem giá trị
bên trái lớn hơn giá trị bên phải hay không và toán tử “<” sẽ so sánh xem giá trị
bên trái nhỏ hơn giá trị bên phải hay không.
- Phép so sánh lớn hơn hoặc bằng (>=), nhỏ hơn hoặc bằng (<=): Toán tử
“>=” sẽ so sánh xem giá trị bên trái lớn hơn hoặc bằng giá trị bên phải hay không
và toán tử “<=” sẽ so sánh xem giá trị bên trái nhỏ hơn hoặc bằng giá trị bên phải
hay không.
1.2.5 Nhập, xuất dữ liệu
```
Trong Python, các hàm nhập và xuất dữ liệu chủ yếu là “input()” và “print()”.
```
- Hàm “input()” được dùng để nhập dữ liệu từ bàn phím. Nó cho phép nhập giá trị
```
và trả về một chuỗi (string) biểu diễn giá trị đã nhập. Ta có thể lưu giá trị này vào
```
biến để sử dụng sau này. Ví dụ:
- Hàm “print()” được sử dụng để hiển thị dữ liệu ra màn hình hoặc console. Ta có
```
thể truyền biến, chuỗi, hoặc giá trị cần hiển thị vào hàm “print()”. Ví dụ:
```
10 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
```
Ngoài ra, “print()” cũng cho phép định dạng hiển thị qua việc sử dụng các đối số
```
```
khác như “sep” (ký tự phân cách), “end” (ký tự kết thúc), và các chuỗi định dạng f-
```
string. Ví dụ:
1.2.6 Các cấu trúc điều khiển
Cấu trúc điều khiển là cách thức quản lý luồng của chương trình, quyết định việc
thực thi các khối mã khác nhau dựa trên điều kiện hoặc vòng lặp. Các cấu trúc này
cung cấp khả năng kiểm soát các điều kiện logic, lặp lại các hoạt động, thực hiện các
quyết định trong đoạn mã. Có ba kiểu cấu trúc điều khiển cơ bản trong Python:
- Câu lệnh điều kiện (Conditional Statements): Cho phép kiểm tra điều kiện, thực
hiện các hành động khác nhau dựa vào kết quả của điều kiện đó. Câu lệnh điều kiện
```
phổ biến nhất trong Python là câu lệnh “if”, “else”, và “elif” (else if). Ví dụ:
```
- Vòng lặp (Loops): Vòng lặp sẽ cho phép sự lặp lại việc thực hiện một khối mã
cho đến khi một điều kiện nào đó được thỏa mãn. Trong Python, hai loại vòng lặp
phổ biến nhất là vòng lặp “for” và “while”.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 11
• Vòng lặp “for” được dùng để duyệt qua một chuỗi hoặc một tập hợp các phần
tử. Ví dụ:
• Vòng lặp “while” thực hiện việc lặp lại mã đến khi điều kiện không còn đúng
nữa. Ví dụ:
- Câu lệnh nhảy (Jump Statements): Câu lệnh nhảy được dùng để thay đổi luồng
điều khiển của chương trình. Các câu lệnh nhảy phổ biến trong Python bao gồm
“break”, “continue” và “pass”.
• Sử dụng câu lệnh “break” để kết thúc một vòng lặp:
• Câu lệnh “continue” được dùng để bỏ qua phần còn lại của vòng lặp hiện tại và
chuyển sang vòng lặp kế tiếp:
• Sử dụng câu lệnh “pass” như là một tuyên bố rỗng:
12 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
1.2.7 Chuỗi
```
“Trong Python, chuỗi (String) được định nghĩa là một tập hợp các ký tự, được bao
```
```
bọc bởi cặp dấu nháy đơn (' ') hoặc cặp dấu nháy kép (" "). Chuỗi có thể bao gồm bất
```
kỳ loại ký tự nào, chẳng hạn như chữ cái, số và các ký tự đặc biệt” [1], [2].
- Khai báo chuỗi trong Python:
- Truy cập ký tự trong chuỗi: Chúng ta có thể truy cập các ký tự trong chuỗi bằng
cách sử dụng chỉ số của chúng trong cặp dấu ngoặc vuông []. Chú ý rằng chỉ số
trong Python bắt đầu từ 0. Ví dụ:
- Các phép xử lý chuỗi trong Python:
```
• Cắt chuỗi (Slicing): Cắt chuỗi là quá trình lấy một phần của chuỗi sử dụng chỉ
```
mục hoặc phạm vi chỉ mục.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 13
```
• Ghép chuỗi (Concatenation): Ghép chuỗi là quá trình nối chuỗi lại với nhau.
```
```
• Độ dài chuỗi (Length): Hàm “len()” được dùng để tính độ dài của chuỗi.
```
- Một số hàm dùng để xử lý các chuỗi trong Python:
```
• “upper()”: Chuyển đổi chuỗi thành chữ hoa.
```
```
• “lower()”: Chuyển đổi chuỗi thành chữ thường.
```
```
• “strip()”: Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
```
```
• “split()”: Phân tách chuỗi thành danh sách các từ hoặc phần tử.
```
```
• “replace()”: Thay thế một phần của chuỗi bằng một chuỗi khác.
```
14 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
```
1.2.8 Hàm (Function)
```
“Hàm trong Python là một đoạn mã có thể được gọi để thực hiện một nhiệm vụ
nhất định, cho phép tổ chức mã thành các phần nhỏ hơn, tái sử dụng mã và làm cho
chương trình trở nên dễ đọc hơn” [1], [2].
- Khai báo hàm: Để định nghĩa một hàm trong Python, ta sử dụng từ khóa "def",
```
tiếp theo là tên hàm và danh sách tham số (nếu có), sau đó là một khối mã được
```
thụt lề bên trong dấu hai chấm.
- Phân loại hàm:
• Hàm có giá trị trả về: Một hàm có khả năng trả lại giá trị thông qua từ khóa
"return". Nếu không có lệnh "return" trong hàm, nó sẽ tự động trả về "None"
như giá trị mặc định.
• Hàm không có giá trị nào trả về: Một số hàm chỉ thực hiện một công việc nhất
định mà không cần trả về bất kỳ giá trị nào.
- Cách sử dụng hàm:
• Gọi hàm: Để sử dụng hàm, chỉ cần gọi tên hàm cùng với các đối số cần thiết
```
(nếu có). Ví dụ:
```
• Tham số và đối số: “Tham số” là các biến được định nghĩa trong định nghĩa
hàm, còn “đối số” là giá trị được truyền cho tham số khi gọi hàm.
Ví dụ về khai báo và gọi hàm trong Python:
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 15
Ví dụ khai báo và gọi hàm không có giá trị trả về:
1.3 KIỂU DỮ LIỆU CÓ CẤU TRÚC
```
1.3.1 Mảng (Array)
```
“Trong Python, module “array” cung cấp một cấu trúc dữ liệu cơ bản gọi là mảng
```
(array) cho phép lưu trữ cùng loại dữ liệu. Mảng trong module array giới hạn các phần
```
tử bên trong mảng phải cùng kiểu dữ liệu” [1], [2].
- Để sử dụng mảng trong Python, chúng ta cần import module “array”:
- Khai báo mảng trong module “array”: Có hai tham số quan trọng khi khai báo một
mảng:
• Typecode: Đây là một ký tự xác định kiểu dữ liệu của các phần tử trong mảng.
• Initializer: Đây là danh sách các giá trị ban đầu của mảng.
Ví dụ:
16 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Các kiểu dữ liệu (Typecodes) trong module array:
```
• 'b': signed char (1 byte)
```
```
• 'B': unsigned char (1 byte)
```
```
• 'i': signed int (2 bytes)
```
```
• 'I': unsigned int (2 bytes)
```
```
• 'f': float (4 bytes)
```
```
• 'd': double (8 bytes)
```
• và nhiều typecodes khác.
- Phương thức và thuộc tính của mảng:
• Truy cập phần tử trong mảng: Truy cập các phần tử trong mảng bằng cách sử
dụng chỉ số của chúng.
• Cập nhật giá trị của phần tử trong mảng:
• Sử dụng các phương thức của mảng: Module “array” cung cấp một số phương
thức để thực hiện các thao tác với mảng:
```
o “append()”: Thêm một phần tử vào cuối mảng.
```
```
o “insert()”: Chèn một phần tử vào vị trí chỉ định.
```
```
o “remove()”: Xóa phần tử ở vị trí đầu tiên có giá trị xác định.
```
```
o “pop()”: Xóa phần tử ở vị trí chỉ định và trả về giá trị của phần tử đó.
```
```
o “extend()”: Mở rộng mảng bằng cách thêm các phần tử từ một mảng khác.
```
```
o “index()”: Trả về chỉ số đầu tiên của một phần tử cụ thể.
```
```
o “count()”: Đếm số lần xuất hiện của một phần tử trong mảng.
```
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 17
Ví dụ:
```
1.3.2 Danh sách (List)
```
```
“Trong Python, kiểu dữ liệu danh sách (List) thường được sử dụng để lưu trữ và
```
làm việc với các tập hợp dữ liệu có thứ tự. Mặc dù không có một kiểu dữ liệu mảng cố
định như trong một số ngôn ngữ khác, nhưng danh sách trong Python có thể được sử
dụng tương đương với mảng vì chúng có khả năng lưu trữ nhiều loại dữ liệu và có thể
```
thay đổi kích thước (động)” [1], [2].
```
- Khai báo một danh sách (List):
- Cách sử dụng danh sách:
• Truy cập vào một phần tử ở trong danh sách:
• Cập nhật giá trị của một phần tử ở trong danh sách:
• Thêm một phần tử vào danh sách:
• Xóa một phần tử khỏi danh sách:
18 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
• Duyệt qua từng phần tử trong danh sách:
- Lưu ý khi làm việc với danh sách trong Python:
• Chỉ số trong danh sách bắt đầu từ 0.
• Danh sách có thể chứa nhiều kiểu dữ liệu khác nhau.
• Có thể thay đổi kích thước danh sách bằng cách thêm, xóa, thay đổi phần tử.
• Có nhiều phương thức và hàm sẵn có trong Python để làm việc với danh sách
```
như append(), remove(), pop(), insert(), sort(), len(), và nhiều hơn nữa.
```
1.3.3 Kiểu Tuple
“Tuple là một dạng dữ liệu quan trọng dùng để lưu trữ các tập hợp thông tin không
```
thể thay đổi (immutable). Đặc điểm của nó là sử dụng dấu ngoặc đơn và các phần tử
```
trong Tuple sẽ được phân cách bằng dấu phẩy” [1], [2].
- Đặc điểm của Tuple:
```
• Không thay đổi (Immutable): Sau khi tạo tuple sẽ không thay đổi giá trị của
```
```
các phần tử trong tuple. Điều này khác với danh sách (list), nơi có thể thay đổi
```
giá trị của các phần tử.
• Có thứ tự: Các phần tử trong tuple được xác định bằng vị trí của chúng, giống
như danh sách.
• Có thể chứa nhiều kiểu dữ liệu: Tuple có thể chứa các phần tử với các kiểu dữ
liệu khác nhau.
- Ưu điểm của Tuple:
• Sử dụng Tuple khi muốn đảm bảo các dữ liệu không thay đổi và không bị sửa
đổi sau khi đã khởi tạo.
• Tốc độ truy cập phần tử trong Tuple thường nhanh hơn so với danh sách.
- Khai báo Tuple:
Có thể báo một tuple bằng cách sử dụng dấu ngoặc đơn và phân tách các phần tử
bằng dấu phẩy. Ví dụ:
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 19
- Truy cập vào phần tử trong Tuple:
Tương tự như danh sách, có thể truy cập các phần tử trong Tuple bằng cách sử
dụng chỉ số của chúng. Ví dụ:
- Các phương thức trong Tuple:
```
• count(value): Đếm số lần một giá trị cụ thể trong tuple xuất hiện. Ví dụ:
```
```
• index(value): Trả về chỉ số đầu tiên của một giá trị cụ thể trong tuple. Ví dụ:
```
Cần lưu ý rằng vì tính không thay đổi của Tuple, nó không cung cấp các phương
```
thức như thêm mới phần tử (“append()”), xóa phần tử (“remove()”), hoặc sắp xếp
```
```
(“sort()”) như danh sách (list) trong Python. Điều này làm cho Tuple không linh hoạt
```
nhưng an toàn khi cần bảo vệ các dữ liệu mà không muốn chúng bị thay đổi sau khi
đã khởi tạo.
1.3.4 Kiểu Dictionary
“Trong Python, “dictionary” là một kiểu dữ liệu cấu trúc, mạnh mẽ được sử dụng
để lưu trữ các cặp key-value không có thứ tự. Dictionary được biểu diễn bằng dấu
```
ngoặc nhọn “{}” và mỗi cặp key-value được phân tách bởi dấu hai chấm “:”. Key
```
trong dictionary phải là duy nhất và không thể thay đổi, trong khi value có thể là bất
kỳ kiểu dữ liệu nào” [1], [2].
20 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Khai báo dictionary:
- Truy cập vào giá trị trong dictionary:
Có thể truy cập giá trị trong dictionary bằng cách sử dụng key tương ứng, ví dụ:
- - Thêm hoặc cập nhật giá trị trong dictionary:
- Xóa một phần tử trong dictionary:
- Các phương thức và phương thức dành cho dictionary:
```
• “keys()”: Trả về tất cả các keys trong dictionary.
```
```
• “values()”: Trả về tất cả các values trong dictionary.
```
```
• “items()”: Trả về tất cả các cặp key-value trong dictionary dưới dạng tuple.
```
Ví dụ:
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 21
- Lưu ý:
• Dictionary trong Python không có thứ tự, nghĩa là không giữ trật tự của các
phần tử đã được thêm vào.
• Key trong dictionary phải là duy nhất, không thể thay đổi. Còn Value có thể là
bất kỳ một kiểu dữ liệu nào.
1.4 OOP TRONG PYTHON
```
1.4.1 Lớp (Class) và đối tượng (Object)
```
“Python hỗ trợ OOP hoàn toàn và có thể được sử dụng để viết mã sử dụng các khái
```
niệm hướng đối tượng như lớp (class), đối tượng (object), kế thừa (inheritance), đa
```
```
hình (polymorphism), trừu tượng hóa (abstraction) [1], [2]”.
```
```
Lớp (Class): Là một khuôn mẫu để tạo ra các đối tượng. Nó chứa các thuộc tính
```
```
(attributes) và phương thức (methods).
```
```
Đối tượng (Object): Là một thể hiện cụ thể của một lớp, có thể được tạo ra từ
```
lớp bằng cách sử dụng từ khóa class.
Ví dụ sau trình bày về lớp và đối tượng trong Python:
Ở ví dụ trên, “Car” là một lớp đại diện cho các đối tượng xe ô tô. “brand” và
“model” là các thuộc tính của lớp, và “get_info” là một phương thức để trả về thông
tin về xe ô tô.
22 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
```
1.4.2 Khởi tạo (Constructor)
```
```
Trong Python, constructor được định nghĩa bằng phương thức “__init__()” trong
```
lớp. Constructor này tự động được gọi khi khởi tạo một đối tượng từ lớp đó. Cú pháp
của Constructor trong Python:
Trong đó:
- “__init__()” là tên của constructor trong Python.
- “self” là tham số đặc biệt đại diện cho chính đối tượng được tạo ra từ lớp.
- “parameter1”, “parameter2”,... là các tham số bạn muốn truyền vào khi tạo đối
tượng.
Ví dụ sau trình bày về Constructor trong Python:
```
Trong ví dụ trên, “__init__()” là constructor của lớp Car. Khi một đối tượng được
```
tạo từ lớp Car, constructor này tự động được gọi. Trong constructor, “self.brand =
brand” và “self.model = model” được sử dụng để gán một giá trị cho các thuộc tính
của đối tượng “my_car”.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 23
```
1.4.3 Thuộc tính (Attributes)
```
```
Attribute (thuộc tính) là các biến được liên kết với đối tượng của một lớp.
```
- Phân loại thuộc tính trong Python:
```
• Thuộc tính instance (Instance Attributes): Là các thuộc tính chỉ thuộc về
```
một đối tượng cụ thể của một lớp.
```
• Thuộc tính lớp (Class Attributes): Là các thuộc tính thuộc về toàn bộ lớp,
```
không chỉ thuộc về một đối tượng cụ thể nào đó. Chúng được chia sẻ giữa tất
cả các đối tượng của lớp.
- Định nghĩa thuộc tính trong Python:
Trong đó:
• “attribute1”, “attribute2”: Là các thuộc tính instance, được gán giá trị khi
một đối tượng được tạo.
• “class_attribute”: Là một thuộc tính lớp, có thể truy cập thông qua tất cả các
đối tượng của lớp.
- Truy cập thuộc tính trong Python:
```
1.4.4 Phương thức (Methods)
```
```
Phương thức (methods) là chỉ các hàm được định nghĩa bên trong một lớp và được
```
gắn liền với các đối tượng của lớp đó.
24 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Định nghĩa một phương thức trong Python:
Trong đó:
• “method_name”: Tên của phương thức.
• “self”: Tham chiếu đến chính đối tượng của lớp. self là bắt buộc và được dùng
để truy cập các thuộc tính và phương thức khác trong cùng lớp.
```
• “parameter1”, “parameter2”: Các tham số mà phương thức có thể nhận (tùy
```
```
chọn).
```
• “return”: Cho biết phương thức trả về một giá trị nếu cần.
- Truy cập phương thức trong Python:
```
1.4.5 Kế thừa (Inheritance)
```
```
Trong Python, kế thừa (inheritance) là khả năng của một lớp con (child class) kế
```
```
thừa thuộc tính và phương thức từ một lớp cha (parent class). Tuy nhiên, đa kế thừa
```
```
(multiple inheritance) sẽ cho phép một lớp con kế thừa từ nhiều lớp cha.
```
- Kế thừa đơn (Single Inheritance):
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 25
- Đa kế thừa (Multiple Inheritance):
- Lợi ích của kế thừa:
• Tái sử dụng mã: Kế thừa cho phép sử dụng lại mã nguồn có sẵn từ lớp cha.
• Tính mở rộng: Lớp con có thể mở rộng hoặc thay đổi hành vi của lớp cha.
• Tổ chức mã nguồn: Kế thừa giúp tổ chức mã nguồn theo cấu trúc phân cấp, dễ
dàng hiểu và bảo trì.
```
1.4.6 Đa hình (Polymorphism)
```
```
Đa hình (Polymorphism) là khả năng của các đối tượng có thể hiện thực hành vi
```
khác nhau thông qua cùng một phương thức hoặc tên hàm. Phân loại:
- Đa hình ở thời điểm biên dịch (Compile-time Polymorphism):
Được triển khai thông qua kỹ thuật “overloading” và “overriding”:
```
• Overloading (Nạp chồng): Là khả năng có nhiều hàm hoặc phương thức cùng
```
tên nhưng có các tham số khác nhau hoặc kiểu dữ liệu khác nhau. Ví dụ:
```
• Overriding (Ghi đè): Là khả năng của một lớp con thay đổi triển khai của một
```
phương thức mà đã được định nghĩa trong lớp cha. Ví dụ:
26 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Đa hình ở thời điểm chạy (Runtime Polymorphism):
Được triển khai thông qua kỹ thuật gọi phương thức của đối tượng dựa trên lớp của
đối tượng đó. Ví dụ:
```
Ở ví dụ trên, hàm “animal_sound()” có thể nhận vào các đối tượng từ các lớp
```
```
khác nhau kế thừa từ Animal. Khi gọi “make_sound()”, nó sẽ thực thi phương thức
```
của đối tượng cụ thể tùy thuộc vào lớp của đối tượng được chuyển vào.
```
1.4.7 Trừu tượng hóa (Abstraction)
```
```
Trừu tượng hóa (Abstraction) là quá trình ẩn các chi tiết cài đặt nội tại của một đối
```
tượng và chỉ hiển thị các tính năng quan trọng hoặc cần thiết cho người sử dụng. Các
đặc điểm của trừu tượng hóa:
- Ứng dụng tập trung: Trừu tượng hóa cho phép người sử dụng tập trung vào việc
sử dụng đối tượng mà không cần biết chi tiết cài đặt bên trong của nó.
- Giảm sự phức tạp: Nó giúp giảm bớt sự phức tạp của hệ thống bằng cách che
giấu các chi tiết phức tạp và chỉ hiển thị những thông tin cần thiết.
- Tạo ra mô hình trừu tượng: Trừu tượng hóa cho phép tạo ra mô hình trừu tượng
cho các đối tượng trong thế giới thực, giúp trong việc phát triển và bảo trì mã
nguồn dễ dàng hơn.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 27
Ví dụ về trừu tượng hóa trong Python:
Trong ví dụ trên, lớp “Animal” là lớp trừu tượng và có một phương thức trừu
```
tượng “make_sound()”, không có triển khai cụ thể. Hai lớp con “Dog” và “Cat” kế
```
```
thừa từ lớp “Animal” và triển khai phương thức “make_sound()” một cách cụ thể
```
cho từng loài động vật.
1.5 CÔNG CỤ THỰC HÀNH
1.5.1 Trình biên dịch Python
Để bắt đầu lập trình với Python, chúng ta cần cài đặt Python vào máy tính. Sinh
viên thực hiện theo các bước sau:
❖ Trên Windows:
• Truy cập vào trang web https://www.python.org/ và chọn phiên bản Python phù
```
hợp với hệ điều hành Windows (32-bit hoặc 64-bit). Sau đó tải về và cài đặt.
```
• Chạy trình cài đặt: Đảm bảo đã chọn tùy chọn "Add Python to PATH" để thêm
vào biến môi trường PATH.
28 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
• Kiểm tra cài đặt: Hãy mở Command Prompt và nhập “python --version” hoặc
“python -V” để kiểm tra phiên bản Python đã cài đặt.
- Trên macOS:
• Cài đặt Python bằng Homebrew: Trong Terminal, nhập lệnh “brew install
python” và theo hướng dẫn để cài đặt Python.
• Kiểm tra cài đặt: Mở Terminal và nhập “python3 --version” để kiểm tra phiên
bản Python đã cài đặt.
- Trên Linux (phần lớn các bản phân phối):
• Mở Terminal và chạy lệnh sau: “sudo apt-get update && sudo apt-get
install python3”.
• Kiểm tra cài đặt: Mở Terminal và nhập “python3 --version” để kiểm tra.
1.5.2 IDE Visual Studio Code
```
“Visual Studio Code (VS Code) là trình soạn thảo mã nguồn (IDE) phổ biến được
```
sử dụng rộng rãi cho lập trình” [3]. Một số điểm mạnh của VS Code khi sử dụng cho
lập trình Python:
- Hỗ trợ ngôn ngữ Python: VS Code cung cấp hỗ trợ tốt cho Python.
- Extension và tích hợp: Có thể cài đặt các extension để cung cấp các tính năng mở
rộng như debugging, linting, phân tích code,….
- Debugging Python: VS Code cung cấp công cụ debugging tích hợp cho Python.
- Terminal tích hợp: Có terminal tích hợp giúp thực thi các lệnh Python và quản lý
môi trường làm việc một cách thuận tiện.
- Tích hợp Git: Cung cấp tích hợp với Git để quản lý phiên bản và hợp tác với các dự
án Python trong quá trình phát triển.
- Mở rộng và tùy chỉnh: Có thể mở rộng VS Code thông qua các extension.
```
1.5.3 Hệ thống kiểm soát phiên bản (Git)
```
“Các dự án trong thực tế thường có nhiều lập trình viên làm việc song song. Vì
vậy, cần có một hệ thống kiểm soát phiên bản như Git là cần thiết để đảm bảo không
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 29
có xung đột mã giữa các lập trình viên. Ngoài ra, những yêu cầu trong dự án thay đổi
thường xuyên. Vì vậy, cần có một hệ thống có thể cho phép nhà phát triển quay lại
phiên bản cũ hơn của mã” [4].
Một số khái niệm trong Git:
- Repository (Kho hoặc repo): Là nơi lưu trữ tất cả các file, thư mục và lịch sử thay
đổi của dự án.
- Commit: Là hành động lưu trữ các thay đổi trong mã nguồn vào repo. Dùng lệnh
“git commit” để tạo ra một commit trong Git.
- Branch (Nhánh): Là một phiên bản song song của mã nguồn trong repo, giúp phát
triển các tính năng, sửa lỗi mà không làm ảnh hưởng đến nhánh chính.
- Merge và Pull Request (PR): Merge là quá trình hợp nhất các thay đổi từ một
```
nhánh vào nhánh khác. Pull Request (PR) là một yêu cầu được tạo ra để hợp nhất
```
các thay đổi từ một nhánh vào nhánh chính.
- Remote: Là các repo trên máy chủ từ xa như GitHub, GitLab, nơi có thể chia sẻ và
đồng bộ hóa code.
- Staging Area (Index): Là nơi lưu trữ các thay đổi đã được chuẩn bị để commit.
Trước khi commit, các thay đổi cần được thêm vào staging area.
- Conflict (Xung đột): Xảy ra khi có sự mâu thuẫn giữa các thay đổi trên cùng một
dòng trong mã nguồn từ các nhánh khác nhau.
1.6 BÀI TẬP THỰC HÀNH
1.6.1 Bài thực hành 01: Cài đặt môi trường
Sinh viên tiến hành cài đặt môi trường lập trình cho ngôn ngữ Python và tạo các
tài khoản cần thiết, bao gồm các phần sau:
1. Cài đặt Python:
- Truy cập trang web https://www.python.org/ ➔ Download và chọn phiên bản phù
hợp với hệ điều hành.
30 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Chạy trình cài đặt: Đảm bảo rằng đã tích chọn tùy chọn "Add Python to PATH" để
thêm Python vào trong biến môi trường PATH.
- Kiểm tra cài đặt: Hãy mở Command Prompt và nhập vào “python –version” hoặc
“python -V”.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 31
2. Tạo tài khoản Github, cài đặt Git, tạo và kéo repo về local:
- Truy cập https://github.com/ ➔ Chọn “Sign up” để đăng ký tài khoản.
- Sau khi xác thực thông tin thành công, tiến hành đăng nhập, chúng ta được giao
diện như sau:
- Truy cập https://git-scm.com/downloads và chọn phiên bản phù hợp với hệ điều
hành.
32 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Chạy file vừa tải về, tiến hành cài đặt phần mềm vào máy tính.
- Kiểm tra cài đặt: Hãy mở Command Prompt và nhập “git –-version”.
- Vào địa chỉ https://github.com/ ➔ Chọn “+” ➔ Chọn “New Repository”.
• Repository name: Nhập “bmttnc-hutech-<MSSV>”.
• Description: Nhập “<họ_tên_SV>_<MSSV>”.
• Chọn “Private”.
• Chọn “Add a README file”.
• Chọn “Create repository” để tạo mới repo.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 33
- Chọn “<> Code” ➔ HTTPS ➔ Nhấn copy đường dẫn tới repo.
34 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Vào https://github.com/settings/profile ➔ Chọn “Developer Settings” ➔ Chọn
```
“Personal access tokens” ➔ “Tokens (classic)” ➔ Chọn “Generate a personal
```
access token”.
- Nhập Note là “bmtt-hutech”, ở Expiration chọn “60 days”. Chọn các mục trong
“Select scopes” ➔ Chọn “Generate token” để tạo mới token.
- Lưu trữ “Personal access tokens (classic)” tránh thất lạc cho các lần dùng tiếp
theo.
- Tại máy tính thực hành, tiến hành clone repo về local. Mở Command Prompt (lưu ý
```
chuyển ở đĩa hiện thời sang ổ đĩa thực hành):
```
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 35
- Cửa sổ “Connect to Github” hiện ra ➔ Chọn “Token” ➔ Nhập “Personal access
token” vừa được tạo ở bước trên vào. Repo được clone về thành công.
3. Cài đặt Visual Studio Code và cấu hình:
- Vào trang https://code.visualstudio.com/download và tải phiên bản phù hợp với hệ
điều hành.
- Sau khi tải file cài đặt về, tiến hành cài đặt phần này mềm vào máy tính.
- Mở VS Code, chọn “Accounts” ➔ Chọn “Sign in to Sync Settings”. Chọn “Authorize
Visual-Studio-Code”. Hệ thống sẽ đưa trở về giao diện VS Code. Kiểm tra tại mục
“Accounts” xem đã có tài khoản được kết nối hay chưa.
36 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Vào thẻ “Extensions”, tiến hành cài đặt các extension sau: Python, Pylance, Python
Indent, Python Snippets.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 37
4. Ví dụ cơ bản với Python:
- Mở VS Code ➔ Chọn “File” ➔ “Open Folder…”. Chọn đường dẫn đến project được
clone về từ Github ở bước trên ➔ Chọn “Yes, I trust the authors”.
- Tạo mới thư mục “lab-01”. Trong thư mục “lab-01” tạo file “hello.py”.
- Lưu file. Vào menu “Terminal” ➔ “New Terminal” hoặc nhấn tổ hợp phím Ctrl +
Shift + `. Kiểm tra chương trình vừa tạo.
38 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Cài đặt thông tin “Git account's default identity”:
- Đưa các thay đổi lên remote repo:
- Kiểm tra trên website https://github.com:
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 39
1.6.2 Bài thực hành 02: Lập trình Python cơ bản
- Câu 01: Viết chương trình yêu cầu người dùng nhập vào họ tên và tuổi của họ,
sau đó in ra màn hình thông điệp chào mừng với thông tin vừa nhập.
Hướng dẫn: Tạo file “ex02_01.py” trong “lab_01”.
Kết quả:
- Câu 02: Viết chương trình thực hiện tính diện tích của hình tròn với bán kính được
nhập từ người dùng. Sử dụng giá trị Pi là 3.14.
Hướng dẫn: Tạo file “ex02_02.py” trong “lab_01”.
- Kết quả:
40 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Câu 03: Viết chương trình kiểm tra một số nhập vào từ người dùng có phải là số
chẵn hay không.
Hướng dẫn: Tạo file “ex02_03.py” trong “lab_01”.
Kết quả:
- Câu 04: Xây dựng một chương trình nhằm tìm tất cả các số nằm trong khoảng từ
```
2000 đến 3200 (bao gồm cả 2000 và 3200) mà chia hết cho 7 và không phải là bội
```
số của 5. Các số tìm được sẽ được in ra trên một dòng, ngăn cách bởi dấu phẩy.
Hướng dẫn: Tạo file “ex02_04.py” trong “lab_01”.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 41
Kết quả:
- Câu 05: Xây dựng một chương trình nhằm nhập số giờ làm việc hàng tuần của
nhân viên và mức lương theo giờ tiêu chuẩn. Từ đó, thực hiện tính toán số tiền
thực nhận của nhân viên. Cần lưu ý rằng số giờ tiêu chuẩn mỗi tuần là 44 giờ, và
mỗi giờ làm thêm sẽ được trả 150% so với mức lương theo giờ tiêu chuẩn.
Hướng dẫn: Tạo file “ex02_05.py” trong “lab_01”.
42 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
Kết quả:
- Câu 06: Tạo một chương trình để nhập vào hai số X và Y; từ đó, xây dựng một
mảng hai chiều. Giá trị của mỗi phần tử tại hàng i và cột j của mảng sẽ là i*j, với i
chạy từ 0 đến X-1 và j từ 0 đến Y-1. Chẳng hạn, nếu X và Y được nhập là 3 và 5,
thì kết quả sẽ là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]].
Hướng dẫn: Tạo file “ex02_06.py” trong “lab_01”.
Kết quả:
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 43
- Câu 07: Xây dựng một chương trình để nhận các chuỗi đầu vào là những dòng
được nhập, sau đó chuyển đổi các dòng này thành chữ hoa và hiển thị kết quả lên
màn hình.
Hướng dẫn: Tạo file “ex02_07.py” trong “lab_01”.
Kết quả:
44 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Câu 08: Hãy phát triển một chương trình để nhập vào một chuỗi các số nhị phân
với 4 chữ số, phân cách bằng dấu phẩy. Chương trình sẽ kiểm tra từng số để xác
định xem chúng có chia hết cho 5 hay không, sau đó in ra những số thỏa mãn điều
kiện này, cũng được phân tách bằng dấu phẩy. Ví dụ, nếu đầu vào là: ‘0100’,
‘0011’, ‘1010’, ‘1001’, thì kết quả đầu ra sẽ là: ‘1010’.
Hướng dẫn: Tạo file “ex02_08.py” trong “lab_01”.
Kết quả:
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 45
- Câu 09: Viết hàm kiểm tra xem một số được nhập vào có phải là số nguyên tố hay
không.
Hướng dẫn: Tạo file “ex02_09.py” trong “lab_01”.
Kết quả:
46 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Câu 10: Viết một hàm nhận vào một chuỗi và trả về chuỗi đảo ngược của nó.
Hướng dẫn: Tạo file “ex02_10.py” trong “lab_01”.
Kết quả:
```
Cập nhật thư mục theo các bài tập (nhập lệnh vào cửa sổ Terminal của VS Code):
```
Kết quả:
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 47
```
Đưa các thay đổi lên Git (tách nhánh lab01 từ nhánh master, đưa các thay đổi hiện
```
```
tại vào stash):
```
48 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
1.6.3 Bài thực hành 03: List, Tuple, Dictionary
- Câu 01: Viết một chương trình để tính tổng của tất cả các số chẵn trong một List.
Hướng dẫn: Tại folder “lab-01”, tạo folder “ex03”. Tạo file “ex03_01.py” trong
“ex03”.
Kết quả:
- Câu 02: Viết chương trình để đảo ngược vị trí của các phần tử trong một danh
sách.
Hướng dẫn: Tạo file “ex03_02.py” trong “ex03”.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 49
Kết quả:
- Câu 03: Viết chương trình để tạo một Tuple từ một List nhập vào từ bàn phím.
Hướng dẫn: Tạo file “ex03_03.py” trong “ex03”.
50 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
Kết quả:
- Câu 04: Viết chương trình để truy cập các phần tử đầu tiên và cuối cùng trong
một Tuple.
Hướng dẫn: Tạo file “ex03_04.py” trong “ex03”.
Kết quả:
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 51
- Câu 05: Viết chương trình để đếm số lần xuất hiện của mỗi phần tử trong một List
và lưu kết quả vào một Dictionary.
Hướng dẫn: Tạo file “ex03_05.py” trong “ex03”.
Kết quả:
- Câu 06: Viết chương trình để xóa một phần tử từ Dictionary theo key đã cho.
Hướng dẫn: Tạo file “ex03_06.py” trong “ex03”.
52 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
Kết quả:
Đưa các thay đổi lên Git repo:
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 53
1.6.4 Bài thực hành 04: OOP trong Python
Hãy xây dựng một chương trình Python quản lý thông tin sinh viên. Mỗi sinh viên
```
sẽ có các thuộc tính: mã sinh viên (id), tên, giới tính, chuyên ngành, và điểm trung
```
```
bình (hệ 10). Trong đó, mã sinh viên sẽ tự động tăng cho mỗi đối tượng mới.
```
Học lực được tính như sau:
- Loại Giỏi: nếu điểm trung bình từ 8 trở lên.
- Loại Khá: nếu điểm trung bình từ 6,5 đến dưới 8.
- Loại Trung bình: nếu điểm trung bình từ 5 đến dưới 6,5.
- Loại Yếu: nếu điểm trung bình dưới 5.
Yêu cầu: Tạo ra một menu với các chức năng sau:
- Thêm sinh viên.
- Cập nhật thông tin sinh viên theo ID.
- Xóa sinh viên theo ID.
- Tìm kiếm sinh viên qua tên.
- Sắp xếp danh sách sinh viên theo điểm trung bình.
- Sắp xếp danh sách sinh viên theo tên chuyên ngành.
- Hiển thị danh sách sinh viên.
Hướng dẫn:
- Tại folder “lab-01”, tạo folder “ex04”. Tạo file “SinhVien.py” trong “ex04”.
54 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Tạo file “QuanLySinhVien.py” trong “ex04”.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 5556 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Tạo file “Main.py” trong “ex04”.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 5758 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
Kết quả: Chạy file “Main.py” và kiểm tra chương trình.
Thêm file “.gitignore” tại thư mục gốc để không đưa các file cache trong thư mục
“__pycache__” lên Git repo.
BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON 59
Đưa các thay đổi lên Git repo:
Tạo PR từ branch lab01 về branch main trên Git repo:
- Vào địa chỉ của Git repo. Chọn menu “Pull requests”. Chọn “New pull request”.
- Chọn compare branch là “lab01”. Chọn base branch là “main”. Kiểm tra các thay
đổi và nhấn “Create pull request”.
60 BÀI 1: LẬP TRÌNH CƠ BẢN VỚI PYTHON
- Một lần nữa, kiểm tra lại các thay đổi đã phù hợp hay chưa. Sau đó chọn “Merge
pull request” để hoàn tất.
Kết quả:
1.7 BÀI TẬP MỞ RỘNG
- Câu 01: Hãy phát triển một chương trình để liệt kê tất cả các hoán vị của danh
```
sách [1, 2, 3]. Bạn có thể tham khảo việc sử dụng “itertools.permutations()” để
```
thu thập tất cả các hoán vị có thể của danh sách này.
- Câu 02: Hãy xây dựng một chương trình để tính tổng của tất cả các số nguyên
dương và âm có trong một chuỗi được nhập vào. Ví dụ:
Chuỗi ban đầu là “-100#^sdfkj8902w3ir021@swf-20”.
Kết quả: Giá trị dương: 9046. Giá trị âm: -120.