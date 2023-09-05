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

- Hiểu và tiến hành dùng RYU OFCTL REST API:
  - OFCTL - Openflow control using REST Interface
  - Ứng dụng ryu.app.ofctl_rest có sẵn của RYU cung cấp REST API cho ta để có thể cấu hình, cập nhật các giá trị và luồng của switch (https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html)

- Hiểu và tiến hành add flow cho switch:
  - Dùng lệnh curl để add flow
  - Dùng flow-manager để add flow
  - Dùng thư viện request của python để add nhiều flow 1 lúc 
    - [Ví dụ](SDN\add_flow.py)

- Khi add flow, ta không thêm giá trị ip_proto thì RYU sẽ nhận định là match với tất cả giao thức
- Tiến độ triển khai: 
  - Add flow cho topology linear thành công, các host có thể ping được với nhau
  - Đối với topology ring gồm 5 switch, mỗi switch gồm 1 host
    - Add flow cho 1 host ping được với 1 host khác, nhưng khi add flow cho tất cả host như vậy thì lại không host nào ping được tới nhau
    - Với [add_flow_2.py](SDN\add_flow_2.py) thì ban đầu khi ping thì xuất hiện tình trạng Duplicate, sau đó thì các host không ping được tới nhau (có lúc được có lúc không)