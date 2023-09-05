# DACN
 
## Meetings note

### 18/7/2023

- Bắt đầu được giao bài báo để đọc và tìm hiểu

### 1/8/2023

- Đã đọc nhưng chưa dịch hết bài báo, chỉ dịch được tầm 40%
- Tìm hiểu các khái niệm/ công nghệ xuất hiện trong bài báo như: SDN network, traffic analyzer, deep packet inspection, IDPS,  deep deterministic policy gradient, deep reinforcement learning (chưa nắm rõ được)
- Được giao xây dựng một mạng SDN đơn giản với mininet/containernet và Ryu controller/OpenDaylight  

### 22/8/2023

- Tìm hiểu về SDN, Ryu Controller, Mininet, Containernet, OpenFlow (Chưa nắm rõ về Ryu Controller cho lắm)
- Triển khai mạng SDN đơn giản với Ryu Controller và Mininet
  - Dùng flow-manager để làm giao diện quản lý
  - Hiểu được cách dùng mininet để tạo các host và switch
  - Hiểu được cách kiểm tra kết nối ICMP, TCP, UDP cho mininet
  - Triển khai được topology linear gồm 4 switch, mỗi switch chứa 1 host (các host có thể ping được tới nhau)
  - Triển khai topology ring gồm 4 switch, mỗi switch chứa 1 host (các host có thể ping tới nhau nhưng chưa kết nối được udp, tcp)
- Được giao:
  - Tìm hiểu về add flow cho các giao thức ngoài icmp
  - Tìm hiểu về rest api của ryu, gửi request add flow qua api

### 5/9/2023