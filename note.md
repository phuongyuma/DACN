# Note for paper

- Tên bài báo: [Reinforcement Learning-Based Traffic Sampling for Multiple Traffic Analyzers  Software-Defined ](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9385142)

## SDN network

- Kiến trúc mạng hiện đại và tiên tiến có khả năng tách biệt hoàn toàn giữa các phần mềm điều khiển (control plane) và phần cứng chuyển tiếp dữ liệu (data plane)

- Trong truyền thống: điều khiển và chuyển tiếp dữ liệu được tích hợp chặt chẽ trong các thiết bị mạng như switch và router. Điều này làm cho việc quản lý và điều khiển mạng phức tạp, đòi hỏi sự tương tác trực tiếp với từng thiết bị. Mạng SDN thay đổi cách tiếp cận này bằng cách tách biệt hai phần này.
  - Control Plane (Phần mềm điều khiển): Là trung tâm quản lý và quyết định cho toàn bộ mạng. Nó bao gồm các ứng dụng và phần mềm điều khiển, chịu trách nhiệm quản lý và theo dõi toàn bộ mạng. Phần mềm điều khiển tạo ra các chính sách (policy) và quyết định cách dữ liệu mạng phải được chuyển tiếp thông qua các thiết bị mạng.
  - Data Plane (Phần cứng chuyển tiếp dữ liệu): Là nơi thực hiện chuyển tiếp dữ liệu theo hướng dẫn từ phần mềm điều khiển. Phần cứng này có thể là các switch, router hoặc các thiết bị mạng khác. Chúng chỉ thực hiện việc chuyển tiếp dữ liệu mà không tham gia vào việc quyết định về cách xử lý dữ liệu.

- Giao thức OpenFlow: cho phép các ứng dụng trong phần mềm điều khiển gửi các yêu cầu và chỉ thị trực tiếp xuống phần cứng của chuyển tiếp dữ liệu

- Các lợi ích của mạng SDN:
  - Quản lý mạng nhanh chóng và linh hoạt hơn
  - Tích hợp dễ dàng với các ứng dụng và dịch vụ mạng
  - Tăng tính tin cậy và bảo mật của mạng
  - Tối ưu hóa việc sử dụng tài nguyên mạng

- Tham khảo thêm:
  - https://www.geeksforgeeks.org/software-defined-networking/
  - https://vietnix.vn/sdn-la-gi/

## TRAFFIC SAMPLING

## Deep reinforcement learning (DRL)

### Q-Learning
### Deep deterministic policy gradient (DDPG)