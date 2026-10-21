# Minh — Profile design system

Một hệ thống gọn với **hai màu chủ đạo**, áp dụng cho các hình minh họa trong GitHub profile README.

## Màu sắc

| Vai trò | Màu | Cách dùng |
| --- | --- | --- |
| Primary — cobalt | `#3155F5` | Tiêu đề nhấn, nút chính, đường nối, biểu tượng |
| Accent — coral | `#BD422A` | Chi tiết nhấn, thẻ Sân Ngon, trạng thái slot đã qua |

Các nền xanh nhạt `#EEF2FF`, cam nhạt `#FFF0EB` và viền tương ứng là sắc độ của hai màu trên. Không thêm màu thương hiệu thứ ba cho công nghệ hay từng bước quy trình.

Nền trắng `#FFFFFF`, nền tổng `#F8FAFC`, chữ `#182230`, chữ phụ `#566171` và viền `#D8DFE8` là màu trung tính. Ưu tiên diện tích nền trung tính, xanh xuất hiện thường xuyên hơn cam; dùng cam ở một vài điểm có chủ đích.

Xanh và cam dùng làm chữ đều đạt tương phản tối thiểu 4.5:1 trên nền trắng và nền nhạt tương ứng. Trạng thái luôn có nhãn chữ, không chỉ phân biệt bằng màu.

## Chữ và bố cục

- Font: Arial, sans-serif. Hai trọng lượng: regular 400 và bold 700.
- Thứ bậc: tên trong banner → tên dự án → mô tả → thông tin phụ.
- Cỡ chữ SVG theo kích thước gốc: tên 72, tên dự án 52, tiêu đề 24–28, mô tả 22, nhãn 14–18. SVG thu phóng theo khung; nội dung chính cũng có chữ HTML bên dưới.
- Khoảng cách theo thang 4 / 8 / 16 / 24 / 32 / 48.
- Bo góc: nút 12, panel 20, banner 24; badge dạng pill.
- Minh họa dùng nền phẳng, viền mảnh và sơ đồ đơn giản. Không dùng hiệu ứng động hoặc gradient nhiều màu.

## Thành phần

| Thành phần | Quy tắc |
| --- | --- |
| Banner | Nền trung tính, tiêu đề xanh, cam ở nét gạch chân và chi tiết trang trí |
| Nút chính | Nền xanh, chữ trắng; chỉ một nút chính trong nhóm |
| Nút phụ | Nền trắng, viền và chữ xanh; cùng kích thước với nút chính |
| Badge công nghệ | Cùng kiểu pill và cùng họ màu xanh, không gán mỗi công nghệ một màu |
| Thẻ dự án | Chung bố cục và kiểu chữ; Pageforce dùng sắc xanh, Sân Ngon dùng sắc cam |
| Quy trình | Dùng nền trung tính/xanh nhạt; cam nhấn bước cuối |
| Trạng thái | Slot đã qua: cam + nhãn; slot sắp tới: xanh + nhãn |

Màu từ ảnh chụp sản phẩm và giao diện GitHub nằm ngoài phạm vi hệ thống này. Không đổi màu ảnh chụp bằng bộ lọc vì ảnh cần phản ánh đúng sản phẩm.

## Nguồn duy nhất và cập nhật

- [tokens.json](./tokens.json): màu sắc, font, khoảng cách, bo góc và nét viền.
- [templates/](./templates): SVG tham chiếu token thay vì tự chọn mã màu.
- [build.py](./build.py): sinh các SVG đang dùng trong README; kiểm tra XML, mã màu ngoài hệ thống và tương phản chữ.

Chạy từ thư mục gốc của repo, với Python 3:

```sh
python design-system/build.py
git diff --check
```

Thay token hoặc template rồi chạy lại lệnh. Các hình PNG/GIF cũ được giữ để bảo toàn liên kết trong bài viết; profile README dùng bộ SVG hiện tại.

## Basketball artwork

Banner và `basketball-court.svg` dùng cùng token xanh–cam. `assets/basketball-avatar.png` là ảnh bóng rổ 3D tự dựng, được lưu để dùng làm avatar; màu ánh sáng và texture nằm ngoài bảng màu SVG.
